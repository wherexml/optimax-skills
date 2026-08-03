---
name: optimax-ppt-imagegen
description: Generate or redesign 21:9 PowerPoint main visuals in the consistent OptiMax enterprise AI infographic style. Use for Chinese PPT architecture, workflow, roadmap, decision, comparison, operating-model, product-value, risk, data, or Agent visuals. For new visuals, default to three materially different design proposals with shared brand language, concise natural Chinese labels, and separate ImageGen outputs.
---

# OptiMax PPT ImageGen

Turn PPT content into polished raster main visuals while preserving one OptiMax visual system across different business scenarios.

## Default deliverable

- Generate **three design proposals** for every new visual or broad redesign unless the user explicitly requests one.
- Make A, B, and C differ in information architecture and reading path—not merely color, icon, or decoration.
- Keep one output only for a precise repair, text correction, localization, or other narrowly scoped edit.
- If generation is unavailable, return three complete prompts and their selected reference assets.

## Workflow

1. Read [references/prompt-template.md](references/prompt-template.md) and [references/design-variants.md](references/design-variants.md) completely.
2. Extract the audience, page goal, one core conclusion, factual content, relationships, and final short labels.
3. Unless verbatim wording is required, rewrite internal or translated phrases into natural executive Chinese. Prefer 4–8-character action or outcome labels; preserve facts and product meaning. For example: “更新门” → “知识更新”, “待办门” → “待办同步”, “优先级抑制” → “优先排序”.
4. Classify the content archetype, then select three suitable directions from the variant matrix. Do not force the same three layouts onto every topic.
5. Apply these proposal roles flexibly:
   - **A — clarity-first**: the most direct and easily understood structure.
   - **B — executive-story**: a more synthesized methodology, comparison, or value narrative.
   - **C — system-view**: a more memorable system, loop, network, dashboard, or portfolio view.
6. Reject a proposal set if two options have the same silhouette, card hierarchy, and arrow pattern. Redesign one option until the three reading paths are visibly distinct.
7. Select the closest reference asset for each proposal. Treat it as a style, component-language, density, and composition reference—not a content source or edit target.
8. Fill one prompt per proposal with the same verified content and shared visual system, but a unique composition and emphasis.
9. Use the installed `imagegen` skill and built-in image-generation tool. Generate A, B, and C in three separate calls.
10. Save project-bound outputs with descriptive versioned names ending in `-A-<concept>.png`, `-B-<concept>.png`, and `-C-<concept>.png`.
11. Inspect all three. Repair any option with incorrect text, weak 21:9 framing, crowded labels, unclear flow, or insufficient distinction.
12. Present all three together with one sentence describing the strength of each option.

## Shared visual system

- Use a 21:9 ultra-wide landscape with the top 15% reserved as calm title-safe space.
- Use a white to extremely pale-blue background, generous whitespace, subtle blueprint lines, rounded 8px white cards, pale-blue borders, restrained shadows, clean arrows, consistent line icons, and dashboard-style blocks.
- Use deep navy `#173F5F` and cobalt `#2F6FED` as anchors; use green `#2E8B57` and orange `#D98A00` as controlled functional or status accents.
- Choose one color-encoding logic per proposal. Do not use color randomly or rely on color alone.
- Avoid a large uninterrupted saturated-blue field. Prefer white cards, pale 4–10% tints, header bars, icon circles, thin rules, and connector accents.
- Keep all three proposals recognizably in the same design family even when their structures differ.

## Acceptance checks

- Produce three outputs by default and confirm they are structurally distinct.
- Keep every output close to 21:9 and presentation-readable.
- Render final Chinese labels verbatim; reject garbled text, fake glyphs, invented copy, or unrequested English subtitles.
- Keep 3–7 major modules or groups; simplify or split dense content rather than shrinking text.
- Make the primary relationship understandable within three seconds.
- Leave out page title, company logo, page number, footer, website address, browser or PowerPoint chrome, watermark, photography, people, 3D, cartoons, robots, glowing spheres, purple gradients, dark full-canvas backgrounds, and complex decoration.
