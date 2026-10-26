# JetBrains ThinkRail

An Obsidian theme that follows the design of [ThinkRail](https://github.com/JetBrains/thinkrail), the JetBrains IDE-style app.

Unofficial and not affiliated with JetBrains.

![JetBrains ThinkRail, dark](docs/screenshot-dark.png)

![JetBrains ThinkRail, light](docs/screenshot-light.png)

## What it copies

- Dark and light palettes from ThinkRail's bundled themes: zinc surfaces with a neon green accent in dark, white with a darker green in light.
- Links in the info blue, callouts in the info, success, warning and danger colors, tags as a light accent tint.
- Flat surfaces, hairline borders, and 4 / 6 / 8px corner radii.
- Code styled like ThinkRail: borderless, 2px inline and 4px block corners.
- Type scale: 14px body, 13px code, headings from 24px down to an uppercase 12px h6.
- Editor tabs: square, with a divider between them, a hover-gray active tab with a 2px accent bar, and a close button that shows on hover.
- Thin scrollbars that only appear on hover.
- ThinkRail's fonts, Geist and JetBrains Mono, embedded.

## Fonts

Geist and JetBrains Mono (the Latin subset of the variable fonts, with italics) are embedded in `theme.css` as base64, so nothing needs installing and nothing is loaded over the network. Both are licensed under the SIL Open Font License 1.1, see `fonts/`.

## Font size

Obsidian sets the body font size itself (16px by default), which overrides a theme. To match ThinkRail's 14px body text, set Settings > Appearance > Font size to 14.

## Development

Edit `src/theme.css`, then run `python3 scripts/build.py` to regenerate `theme.css` (the file Obsidian loads). Commit both.

## Install

Obsidian needs the folder name to match the `name` in `manifest.json`.

```sh
ln -s /path/to/obsidian-jetbrains-thinkrail "<vault>/.obsidian/themes/JetBrains ThinkRail"
```

Then choose **JetBrains ThinkRail** under Settings > Appearance > Themes.

## Status

Version 0.0.1. Early work, tested by eye in Obsidian only. Open an issue or inspect with Cmd+Opt+I (Ctrl+Shift+I elsewhere) if a surface looks off.

## License

Copyright 2026 Khai. [Apache License 2.0](LICENSE). See [NOTICE](NOTICE) for attribution to ThinkRail.
