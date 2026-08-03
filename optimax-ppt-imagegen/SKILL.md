---
name: optimax-ppt-imagegen
description: Generate or redesign 21:9 PowerPoint main visuals in the consistent OptiMax enterprise AI decision-product infographic style. Use when creating Chinese PPT architecture diagrams, implementation roadmaps, problem-solution-value visuals, risk operations pipelines, Agent orchestration diagrams, or a series of presentation images that must share the same pale-blue background, navy/cobalt cards, green value states, orange risk states, short labels, and ImageGen workflow.
---

# OptiMax PPT ImageGen

Generate polished raster PPT main visuals with a stable visual system and one of four reusable information architectures.

## Workflow

1. Read [references/prompt-template.md](references/prompt-template.md) completely.
2. Extract the page topic, one core conclusion, 3–7 main modules, their relationships, exact short labels, green value items, and orange risk or approval items.
3. Choose one layout family:
   - **Stage rollout**: diagnosis, access, pilot, rollout, or other sequential phases. Use `assets/stage-rollout.png`.
   - **Problem–solution–value**: customer pain, solution engine, business value, and user roles. Use `assets/problem-solution-value.png`.
   - **Operations pipeline**: signal inputs, central processing, supporting capabilities, and result outputs. Use `assets/operations-pipeline.png`.
   - **Agent orchestration**: requests, task decomposition, Agent collaboration, human approval, reusable capabilities, and results. Use `assets/agent-orchestration.png`.
4. Treat the selected image as a style, component-language, density, and composition reference—not an edit target or content source.
5. Fill the variables in the prompt template. Preserve user wording exactly and do not invent metrics, customers, outcomes, or product maturity.
6. Use the installed `imagegen` skill and built-in image generation tool. Pass the selected asset as a reference image. Generate one distinct image per call.
7. Save project-bound output to the user's workspace with a descriptive, versioned PNG filename. Do not overwrite existing assets unless explicitly requested.
8. Inspect the result. Iterate with one targeted change if any acceptance check fails.

## Acceptance checks

- Keep an ultra-wide ratio close to 21:9.
- Leave the top 15% calm and free of page title, logo, page number, footer, or website address.
- Render every requested Chinese label verbatim; reject乱码, fake glyphs, extra English subtitles, and invented text.
- Use navy and cobalt for primary structure, green for completed/value states, and orange only for risk, warning, consequence, or approval.
- Keep 3–7 major modules and readable presentation-scale text; split dense content instead of shrinking labels.
- Make the main relationship understandable within three seconds with clear arrows and no confusing crossings.
- Avoid photography, people, 3D, cartoons, robots, marketing-poster effects, glowing spheres, strong or purple gradients, dark full-canvas backgrounds, and complex decoration.

## Fallback

If no image-generation tool is available, produce the fully populated final prompt and identify the selected reference asset. Do not claim that an image was generated.
