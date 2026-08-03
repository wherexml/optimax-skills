# OptiMax Skills

Reusable AI skills maintained by OptiMax.

## Available skills

### `optimax-ppt-imagegen`

Generate three structurally different 21:9 enterprise AI PPT main visuals by default from a page topic, audience, content relationships, and concise Chinese labels.

Install globally for all supported agents:

```bash
npx --yes skills add wherexml/optimax-skills -g --skill optimax-ppt-imagegen --agent '*' -y
```

Use it with:

```text
Use $optimax-ppt-imagegen to generate three distinct 21:9 PPT main-visual options for a supply-chain risk response loop. Keep one shared OptiMax style and concise natural Chinese labels.
```

The target AI must provide an image-generation tool to render the PNGs. Without one, the skill returns three complete production prompts and their selected reference assets.
