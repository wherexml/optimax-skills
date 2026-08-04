#!/usr/bin/env node

import crypto from "node:crypto";
import fs from "node:fs";
import path from "node:path";

const ignoredDirectories = new Set([
  ".git",
  ".venv",
  "__pycache__",
  "dist",
  "node_modules",
]);

function usage() {
  return [
    "Usage:",
    "  node scripts/inventory_skills.mjs --root PATH [--root PATH ...] [--max-depth N] [--json] [--pretty]",
    "",
    "At least one explicit --root is required. The command is read-only.",
  ].join("\n");
}

function parseArgs(argv) {
  const options = { roots: [], maxDepth: 4, json: false, pretty: false };
  for (let index = 0; index < argv.length; index += 1) {
    const arg = argv[index];
    if (arg === "--root") {
      if (!argv[index + 1]) throw new Error("--root requires a path");
      options.roots.push(path.resolve(argv[++index]));
    } else if (arg === "--max-depth") {
      const value = Number(argv[++index]);
      if (!Number.isInteger(value) || value < 0 || value > 20) {
        throw new Error("--max-depth must be an integer between 0 and 20");
      }
      options.maxDepth = value;
    } else if (arg === "--json") {
      options.json = true;
    } else if (arg === "--pretty") {
      options.pretty = true;
    } else if (arg === "--help" || arg === "-h") {
      process.stdout.write(`${usage()}\n`);
      process.exit(0);
    } else {
      throw new Error(`Unknown argument: ${arg}`);
    }
  }
  if (options.roots.length === 0) throw new Error("at least one --root is required");
  return options;
}

function safeLstat(target) {
  try {
    return fs.lstatSync(target);
  } catch (error) {
    if (error?.code === "ENOENT") return null;
    throw error;
  }
}

function safeRealpath(target) {
  try {
    return fs.realpathSync(target);
  } catch {
    return null;
  }
}

function findSkillFile(directory) {
  for (const name of ["SKILL.md", "SKILL.MD"]) {
    const candidate = path.join(directory, name);
    try {
      if (fs.statSync(candidate).isFile()) return candidate;
    } catch {
      // Missing or unreadable candidates are handled by the caller's report.
    }
  }
  return null;
}

function readFrontmatter(skillFile) {
  try {
    const content = fs.readFileSync(skillFile, "utf8");
    const block = content.match(/^---\s*\n([\s\S]*?)\n---/);
    if (!block) return { name: null, description: null };
    const readField = (field) => {
      const match = block[1].match(new RegExp(`^\\s*${field}\\s*:\\s*(.+?)\\s*$`, "m"));
      return match ? match[1].replace(/^["']|["']$/g, "").trim() : null;
    };
    return { name: readField("name"), description: readField("description") };
  } catch {
    return { name: null, description: null };
  }
}

function hashDirectory(directory) {
  const hash = crypto.createHash("sha256");
  const walk = (current, relative = "") => {
    const entries = fs.readdirSync(current, { withFileTypes: true })
      .filter((entry) => !ignoredDirectories.has(entry.name) && entry.name !== ".DS_Store")
      .sort((left, right) => left.name.localeCompare(right.name));
    for (const entry of entries) {
      const absolute = path.join(current, entry.name);
      const childRelative = path.join(relative, entry.name);
      hash.update(childRelative);
      if (entry.isSymbolicLink()) {
        hash.update(`link:${fs.readlinkSync(absolute)}`);
      } else if (entry.isDirectory()) {
        walk(absolute, childRelative);
      } else if (entry.isFile()) {
        hash.update(fs.readFileSync(absolute));
      }
    }
  };
  walk(directory);
  return hash.digest("hex");
}

function scanRoot(root, maxDepth) {
  const rootResult = {
    path: root,
    exists: fs.existsSync(root),
    errors: [],
  };
  const skills = [];
  const brokenLinks = [];
  const visited = new Set();

  if (!rootResult.exists) return { root: rootResult, skills, brokenLinks };

  const visit = (entryPath, depth) => {
    const stat = safeLstat(entryPath);
    if (!stat) return;

    if (stat.isSymbolicLink()) {
      const linkTarget = fs.readlinkSync(entryPath);
      const resolvedPath = safeRealpath(entryPath);
      if (!resolvedPath) {
        brokenLinks.push({ path: entryPath, linkTarget });
        return;
      }
      const skillFile = findSkillFile(resolvedPath);
      if (skillFile) {
        const metadata = readFrontmatter(skillFile);
        skills.push({
          entryPath,
          resolvedPath,
          kind: "symlink",
          linkTarget,
          skillFile,
          frontmatterName: metadata.name,
          description: metadata.description,
          contentHash: hashDirectory(resolvedPath),
        });
      }
      return;
    }

    if (!stat.isDirectory()) return;
    const resolvedPath = safeRealpath(entryPath) || entryPath;
    if (visited.has(resolvedPath)) return;
    visited.add(resolvedPath);

    const skillFile = findSkillFile(entryPath);
    if (skillFile) {
      const metadata = readFrontmatter(skillFile);
      skills.push({
        entryPath,
        resolvedPath,
        kind: "directory",
        linkTarget: null,
        skillFile,
        frontmatterName: metadata.name,
        description: metadata.description,
        contentHash: hashDirectory(entryPath),
      });
      return;
    }

    if (depth >= maxDepth) return;
    for (const child of fs.readdirSync(entryPath, { withFileTypes: true })) {
      if (ignoredDirectories.has(child.name)) continue;
      if (!child.isDirectory() && !child.isSymbolicLink()) continue;
      visit(path.join(entryPath, child.name), depth + 1);
    }
  };

  try {
    visit(root, 0);
  } catch (error) {
    rootResult.errors.push(error.message);
  }
  return { root: rootResult, skills, brokenLinks };
}

function duplicateGroups(skills) {
  const groups = new Map();
  for (const skill of skills) {
    const key = skill.frontmatterName || path.basename(skill.entryPath);
    if (!groups.has(key)) groups.set(key, []);
    groups.get(key).push(skill);
  }
  return [...groups.entries()]
    .filter(([, entries]) => entries.length > 1)
    .map(([name, entries]) => ({
      name,
      entries: entries.length,
      physicalCopies: new Set(entries.map((entry) => entry.resolvedPath)).size,
      distinctContentHashes: new Set(entries.map((entry) => entry.contentHash)).size,
      paths: entries.map((entry) => entry.entryPath),
    }))
    .sort((left, right) => left.name.localeCompare(right.name));
}

function main() {
  const options = parseArgs(process.argv.slice(2));
  const scans = options.roots.map((root) => scanRoot(root, options.maxDepth));
  const skills = scans.flatMap((scan) => scan.skills);
  const brokenLinks = scans.flatMap((scan) => scan.brokenLinks);
  const duplicates = duplicateGroups(skills);
  const report = {
    generatedAt: new Date().toISOString(),
    readOnly: true,
    roots: scans.map((scan) => scan.root),
    skills,
    brokenLinks,
    duplicates,
    summary: {
      rootsRequested: options.roots.length,
      rootsPresent: scans.filter((scan) => scan.root.exists).length,
      skillEntries: skills.length,
      uniquePhysicalCopies: new Set(skills.map((skill) => skill.resolvedPath)).size,
      symlinkEntries: skills.filter((skill) => skill.kind === "symlink").length,
      brokenLinks: brokenLinks.length,
      duplicateNames: duplicates.length,
    },
  };

  if (options.json) {
    process.stdout.write(`${JSON.stringify(report, null, options.pretty ? 2 : 0)}\n`);
    return;
  }

  process.stdout.write(`roots=${report.summary.rootsRequested} skills=${report.summary.skillEntries} `
    + `copies=${report.summary.uniquePhysicalCopies} broken=${report.summary.brokenLinks} `
    + `duplicate_names=${report.summary.duplicateNames}\n`);
  for (const skill of skills) {
    process.stdout.write(`${skill.frontmatterName || "(unnamed)"}\t${skill.kind}\t${skill.entryPath}\n`);
  }
}

try {
  main();
} catch (error) {
  process.stderr.write(`inventory_skills: ${error.message}\n${usage()}\n`);
  process.exitCode = 1;
}
