# JetBrains ThinkRail

An Obsidian theme that follows the design of [ThinkRail](https://github.com/JetBrains/thinkrail), the JetBrains IDE-style app.

Unofficial and not affiliated with JetBrains.

Site: https://khaister.github.io/obsidian-jetbrains-thinkrail/

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
- ThinkRail's fonts, Geist and JetBrains Mono, when installed.

## Fonts

The theme uses ThinkRail's fonts, Geist for text and JetBrains Mono for code. It does not bundle them. Install them on your system and the theme picks them up; without them it falls back to your system fonts.

- [Geist on Google Fonts](https://fonts.google.com/specimen/Geist)
- [JetBrains Mono on Google Fonts](https://fonts.google.com/specimen/JetBrains+Mono)

Recommended: download the whole family from each page and install the variable font along with its italic. ThinkRail's body text uses weight 370, and the theme also uses weights 400, 500 and 600. A variable font can render all of them, while a static Regular only gives 400. If the download includes variable font files, install those. Restart Obsidian after installing.

On macOS you can install both with Homebrew instead:

```sh
brew install --cask font-jetbrains-mono
brew install --cask font-geist
```

## Font size

Obsidian sets the body font size itself (16px by default), which overrides a theme. To match ThinkRail's 14px body text, set Settings > Appearance > Font size to 14.

## Install

Obsidian needs the folder name to match the `name` in `manifest.json`.

```sh
ln -s /path/to/obsidian-jetbrains-thinkrail "<vault>/.obsidian/themes/JetBrains ThinkRail"
```

Then choose **JetBrains ThinkRail** under Settings > Appearance > Themes.

## Status

Version 1.0.0. Tested by eye in Obsidian only. Open an issue or inspect with Cmd+Opt+I (Ctrl+Shift+I elsewhere) if a surface looks off.

## License

Copyright 2026 Khai. [Apache License 2.0](LICENSE). See [NOTICE](NOTICE) for attribution to ThinkRail.
