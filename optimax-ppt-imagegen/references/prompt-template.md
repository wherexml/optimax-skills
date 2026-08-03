# Prompt template

Fill these variables before generating:

```text
PAGE_TOPIC: page subject
CORE_MESSAGE: one conclusion the viewer should understand
LAYOUT_FAMILY: Stage rollout | Problem–solution–value | Operations pipeline | Agent orchestration
MODULES_AND_FLOW: 3–7 modules and their directional relationships
EXACT_LABELS: exact short Chinese labels to render
STATUS_MODE: neutral | status-aware (default: neutral)
VERIFIED_SUCCESS_ITEMS: only items explicitly confirmed as completed, passed, verified, or successful; otherwise none
PENDING_RISK_ITEMS: only items explicitly marked pending approval, warning, risk, reminder, or adverse consequence; otherwise none
TITLE_SAFE_AREA: default top 15%
```

Use this completed prompt with the selected reference asset:

```text
Use case: productivity-visual
Asset type: 21:9 ultra-wide PowerPoint main infographic for an enterprise AI decision-product presentation.

Input images: Use Image 1 only as a style, component-language, layout-density, and composition reference. Do not copy its company logo, footer, website address, page title, or exact business content. The selected layout family is “{{LAYOUT_FAMILY}}”.

Primary request: Create one polished PPT main visual about “{{PAGE_TOPIC}}”. The single conclusion the viewer should understand is: “{{CORE_MESSAGE}}”. Express these modules and relationships clearly: {{MODULES_AND_FLOW}}.

Scene/backdrop: white to extremely pale blue background, clean generous whitespace, subtle fine blue grid or thin blueprint lines. Reserve the upper {{TITLE_SAFE_AREA}} as calm negative space for a PowerPoint title added later. Do not place a title, logo, page number, footer, or website address in the image.

Style/medium: enterprise-grade AI decision-product infographic, premium flat vector-like visual rendered as a crisp raster image. Use rounded 8px white module cards, fine pale-blue borders, subtle shadows, clear flow arrows, node networks, simple consistent line icons, and restrained dashboard-style information blocks. No photography, no 3D, no cartoon, no marketing-poster styling.

Composition/framing: exact 21:9 ultra-wide landscape feel, balanced and presentation-ready. Use strong hierarchy, consistent spacing, generous outer margins, clear directional relationships, and long-distance readability. Keep 3–7 major modules. Do not solve density by shrinking text.

Layout behavior:
- Stage rollout: arrange 3–5 numbered stage cards left to right, connect them with one main arrow, show one short output strip per stage, and add a slim validation or value band below.
- Problem–solution–value: arrange a left problem column, a dominant central solution engine or network, a right value or user column, and one concise bottom value strip.
- Operations pipeline: arrange signal inputs across the top, a dominant horizontal processing band in the center, supporting graph, Agent, or approval cards below, and 3–4 result cards on the right.
- Agent orchestration: arrange requests on the left, task decomposition next, a central orchestration hub with surrounding Agent nodes, human approval above, reusable capabilities below, and result cards on the right.

Color palette: deep navy #173F5F and cobalt blue #2F6FED for all status-neutral structure; support green #2E8B57 only as a small verified-success status accent; orange #D98A00 only as a small pending, approval, warning, risk, reminder, or adverse-consequence accent; white cards; very pale blue background; cool blue-gray outlines. Avoid purple and strong gradients.

Typography: modern Chinese sans-serif appearance, bold deep-navy headings, short labels only, large enough for presentation readability. Render only the supplied text and render it verbatim. Do not invent English subtitles, paragraphs, placeholder copy, fake glyphs, or extra labels.

Text (verbatim): {{EXACT_LABELS}}

Semantic color rules: status mode is {{STATUS_MODE}}. All architecture, process, gate, capability, output, publication, feedback, future-step, and value nodes are status-neutral by default and must use navy or cobalt blue. Green does not mean category or importance: use it only for these explicitly verified success items: {{VERIFIED_SUCCESS_ITEMS}}. Orange does not mean visual variety: use it only for these explicitly pending or risk items: {{PENDING_RISK_ITEMS}}. When either list is empty, do not use that accent color. Apply status colors only to a small badge, check, dot, or short status label—never to the full card, stage heading, main label, or primary icon. Pair color with a status word or icon. The reference image may contain green or orange modules; ignore that usage when it conflicts with these rules.

Constraints: preserve the selected reference image's polish, card language, icon language, spacing discipline, information density, and enterprise tone while creating an original composition. Ensure the main relationship is visually obvious within three seconds. Keep the title-safe area empty.

Avoid: page title inside the image, real company logo, watermark, page number, browser frame, PowerPoint toolbar, website address, footer slogan, people, photographs, 3D objects, cartoon characters, robots, exaggerated gradients, glowing spheres, complex decoration, dark full-canvas background, dense tiny text, long paragraphs, invented text, fake glyphs, and purple gradients.
```
