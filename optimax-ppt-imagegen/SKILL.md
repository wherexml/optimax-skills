---
name: optimax-ppt-imagegen
description: Generate or redesign 21:9 PowerPoint main visuals in the consistent OptiMax enterprise AI decision-product infographic style. Use when creating Chinese PPT architecture diagrams, implementation roadmaps, problem-solution-value visuals, risk operations pipelines, Agent orchestration diagrams, or a series of presentation images that must share the same pale-blue background, navy/cobalt structure, semantically controlled status accents, short labels, and ImageGen workflow.
---

# OptiMax PPT ImageGen

Generate polished raster PPT main visuals with a stable visual system and one of four reusable information architectures.

## Workflow

1. Read [references/prompt-template.md](references/prompt-template.md) completely.
2. Extract the page topic, one core conclusion, 3–7 main modules, their relationships, exact short labels, and the intended role of every accent color.
3. Choose one primary color-encoding mode before choosing colors:
   - **Functional mode**: colors distinguish stages, domains, or module families. Define one consistent color-role map for the page. Pair color with a stage number, heading, icon, or spatial group so the meaning never depends on color alone.
   - **Status mode**: colors communicate actual state. Green means verified or successful, orange means pending or attention, and red means risk or failure. Pair every state color with a status word or icon.
   - Do not mix functional and status meanings for the same color on one page.
4. Choose one layout family:
   - **Stage rollout**: diagnosis, access, pilot, rollout, or other sequential phases. Use `assets/stage-rollout.png`.
   - **Problem–solution–value**: customer pain, solution engine, business value, and user roles. Use `assets/problem-solution-value.png`.
   - **Operations pipeline**: signal inputs, central processing, supporting capabilities, and result outputs. Use `assets/operations-pipeline.png`.
   - **Agent orchestration**: requests, task decomposition, Agent collaboration, human approval, reusable capabilities, and results. Use `assets/agent-orchestration.png`.
5. Treat the selected image as a style, component-language, density, and composition reference—not an edit target or content source.
6. Fill the variables in the prompt template. Preserve user wording exactly and do not invent metrics, customers, outcomes, or product maturity.
7. Use the installed `imagegen` skill and built-in image generation tool. Pass the selected asset as a reference image. Generate one distinct image per call.
8. Save project-bound output to the user's workspace with a descriptive, versioned PNG filename. Do not overwrite existing assets unless explicitly requested.
9. Inspect the result. Iterate with one targeted change if any acceptance check fails.

## Acceptance checks

- Keep an ultra-wide ratio close to 21:9.
- Leave the top 15% calm and free of page title, logo, page number, footer, or website address.
- Render every requested Chinese label verbatim; reject乱码, fake glyphs, extra English subtitles, and invented text.
- Use navy and cobalt as the visual anchor, not as the only colors. Avoid a large uninterrupted saturated-blue field when lighter containers, white cards, pale tints, and distributed accents can create clearer hierarchy.
- Use at most three accent families beyond neutral blue-gray. Prefer restrained green and orange from the OptiMax palette; red is reserved for genuine high risk or failure.
- In functional mode, green and orange may identify stages or module families when the page's color-role map explicitly defines them. Use the color consistently across the matching heading, icon, connector, and pale tint; do not scatter isolated accents.
- In status mode, use green only for verified or successful state, orange for pending or attention, and red for risk or failure. Keep state color accents compact.
- Preserve ample white space and white cards. Prefer colored header bars, icon circles, thin rules, connector accents, and 4–10% pale tints over filling every card or the whole canvas with saturated color.
- Never rely on color alone: pair it with a stage number, heading, icon, status label, or spatial grouping.
- Reference-image colors may guide balance and rhythm, but the generated page must follow its declared color-role map.
- Keep 3–7 major modules and readable presentation-scale text; split dense content instead of shrinking labels.
- Make the main relationship understandable within three seconds with clear arrows and no confusing crossings.
- Avoid photography, people, 3D, cartoons, robots, marketing-poster effects, glowing spheres, strong or purple gradients, dark full-canvas backgrounds, and complex decoration.

## Fallback

If no image-generation tool is available, produce the fully populated final prompt and identify the selected reference asset. Do not claim that an image was generated.
