# JetBrains ThinkRail

An Obsidian theme that follows the design of [ThinkRail](https://github.com/JetBrains/thinkrail), the JetBrains IDE-style app.


> [!NOTE]
> Unofficial and not affiliated with JetBrains.

![JetBrains ThinkRail, dark](docs/screenshot-dark.png)

![JetBrains ThinkRail, light](docs/screenshot-light.png)

## Fonts

The theme uses ThinkRail's fonts, Geist for text and JetBrains Mono for code. It does not bundle them. Install them on your system and the theme picks them up; without them it falls back to your system fonts.

- [Geist on Google Fonts](https://fonts.google.com/specimen/Geist)
- [JetBrains Mono on Google Fonts](https://fonts.google.com/specimen/JetBrains+Mono)

> [!NOTE]
> Recommended: download the whole family from each page and install the variable font along with its italic. ThinkRail's body text uses weight 370, and the theme also uses weights 400, 500 and 600. A variable font can render all of them, while a static Regular only gives 400. If the download includes variable font files, install those. Restart Obsidian after installing.

On macOS you can install both with Homebrew instead:

```sh
brew install --cask font-jetbrains-mono
brew install --cask font-geist
```

### Font size

Obsidian sets the body font size itself (16px by default), which overrides a theme. To match ThinkRail's 14px body text, set Settings > Appearance > Font size to 14.

## Install

Obsidian needs the folder name to match the `name` in `manifest.json`.

```sh
ln -s /path/to/obsidian-jetbrains-thinkrail "<vault>/.obsidian/themes/JetBrains ThinkRail"
```

Then choose **JetBrains ThinkRail** under Settings > Appearance > Themes.
