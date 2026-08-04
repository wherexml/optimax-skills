# Prompt template

Create one completed prompt for each of A, B, and C.

```text
PROPOSAL_ID: A | B | C
PROPOSAL_NAME: short concept name
PROPOSAL_ROLE: clarity-first | executive-story | system-view
CONTENT_ARCHETYPE: process | architecture | decision/risk | value | roadmap | comparison | operating model | data/performance
PAGE_TOPIC: page subject
AUDIENCE: intended viewer
CORE_MESSAGE: one conclusion the viewer should understand
LAYOUT_LOGIC: unique information architecture and reading path
DISTINCTNESS: how this composition differs from the other two proposals
MODULES_AND_FLOW: 3–7 major modules and their relationships
FINAL_LABELS: final concise Chinese labels to render verbatim
COLOR_ENCODING_MODE: functional | status
COLOR_ROLE_MAP: page-specific mapping for navy, cobalt, green, orange, and optional red
ACCENT_TARGETS: headings, icons, connectors, badges, or pale tints that receive accents
REFERENCE_ASSET: selected reference image
TITLE_SAFE_AREA: default top 15%
```

Use the completed variables with this generation prompt:

```text
Use case: productivity-visual
Asset type: 21:9 ultra-wide PowerPoint main infographic for an enterprise AI decision-product presentation.

Input image: use Image 1 only as a style, component-language, icon-weight, spacing, and polish reference. Do not copy its logo, footer, title, or business content.

This is proposal {{PROPOSAL_ID}} of three: “{{PROPOSAL_NAME}}”. Its role is {{PROPOSAL_ROLE}}. Create one original visual about “{{PAGE_TOPIC}}” for {{AUDIENCE}}. The viewer should understand: “{{CORE_MESSAGE}}”.

Composition: use this unique layout and reading path: {{LAYOUT_LOGIC}}. Express these modules and relationships: {{MODULES_AND_FLOW}}. This proposal must differ from the other two in this way: {{DISTINCTNESS}}.

Scene/backdrop: exact 21:9 ultra-wide landscape feel; white to extremely pale-blue background; clean generous whitespace; subtle blueprint grid or thin blue-gray lines. Reserve the upper {{TITLE_SAFE_AREA}} as calm empty space for a PowerPoint title added later. Place no title, logo, page number, footer, or website address inside the image.

Style: enterprise-grade AI decision-product infographic, premium flat vector-like raster, rounded 8px white cards, fine pale-blue borders, subtle shadows, clear arrows, consistent line icons, restrained node networks, and dashboard-style blocks. Keep 3–7 major groups and long-distance readability.

Color: deep navy #173F5F and cobalt #2F6FED as anchors; support green #2E8B57 and orange #D98A00 as controlled accents; optional red only for genuine high risk or failure. Use {{COLOR_ENCODING_MODE}} encoding with this map: {{COLOR_ROLE_MAP}}. Apply accents only to: {{ACCENT_TARGETS}}. Avoid random color and large saturated slabs; prefer white cards, pale 4–10% tints, header rules, icon circles, and connector accents.

Typography: modern Chinese sans-serif, bold deep-navy headings, short labels, presentation-readable size. Render only these labels and render them verbatim: {{FINAL_LABELS}}. Do not invent English subtitles, paragraphs, placeholder copy, extra labels, or fake glyphs.

Constraints: preserve the OptiMax visual system while making this proposal structurally distinct. The primary relationship must be understandable within three seconds.

Avoid: page title inside the image, real company logo, watermark, page number, browser frame, PowerPoint toolbar, website address, footer slogan, people, photography, 3D, cartoons, robots, exaggerated gradients, glowing spheres, purple gradients, dark full-canvas backgrounds, dense tiny text, long paragraphs, invented facts, or garbled Chinese.
```

Generate A, B, and C in separate ImageGen calls. Reuse the same verified facts and final labels, but do not reuse the same information architecture.
