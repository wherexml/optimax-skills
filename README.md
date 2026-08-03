# OptiMax Skills

Reusable AI skills maintained by OptiMax.

## Available skills

### `optimax-ppt-imagegen`

Generate consistent 21:9 enterprise AI PPT main visuals from a page topic, module relationships, and exact Chinese labels.

Install globally for all supported agents:

```bash
npx --yes skills add wherexml/optimax-skills -g --skill optimax-ppt-imagegen --agent '*' -y
```

Use it with:

```text
Use $optimax-ppt-imagegen to generate a 21:9 PPT main visual for a supply-chain risk response loop. Use the Operations pipeline layout and keep all labels in concise Chinese.
```

The target AI must provide an image-generation tool to render the PNG. Without one, the skill returns a complete production prompt and the selected reference asset.

