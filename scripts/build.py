#!/usr/bin/env python3
"""Build theme.css: embed the fonts in fonts/ as base64 data URLs, then append src/theme.css.

Obsidian themes cannot load remote assets or extra files, so everything ships in one theme.css.
Run from anywhere: python3 scripts/build.py
"""
import base64
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent

# Latin subset range, as published by @fontsource-variable/geist and /jetbrains-mono
LATIN = (
    "U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,"
    "U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD"
)

FONTS = [
    ("Geist Variable", "normal", "geist-latin-wght-normal.woff2"),
    ("Geist Variable", "italic", "geist-latin-wght-italic.woff2"),
    ("JetBrains Mono Variable", "normal", "jetbrains-mono-latin-wght-normal.woff2"),
    ("JetBrains Mono Variable", "italic", "jetbrains-mono-latin-wght-italic.woff2"),
]


def font_face(family: str, style: str, filename: str) -> str:
    data = base64.b64encode((ROOT / "fonts" / filename).read_bytes()).decode("ascii")
    return (
        "@font-face {\n"
        f'  font-family: "{family}";\n'
        f"  font-style: {style};\n"
        "  font-display: swap;\n"
        "  font-weight: 100 900;\n"
        f'  src: url("data:font/woff2;base64,{data}") format("woff2");\n'
        f"  unicode-range: {LATIN};\n"
        "}\n"
    )


def main() -> None:
    header = (
        "/*\n"
        " * GENERATED FILE, DO NOT EDIT. Edit src/theme.css and run scripts/build.py.\n"
        " *\n"
        " * Embedded fonts (SIL Open Font License 1.1, see fonts/*-OFL.txt):\n"
        " *   Geist, Copyright 2024 The Geist Project Authors (https://github.com/vercel/geist-font)\n"
        " *   JetBrains Mono, Copyright 2020 The JetBrains Mono Project Authors\n"
        " *   (https://github.com/JetBrains/JetBrainsMono)\n"
        " * Latin subset of the variable fonts, as packaged by Fontsource.\n"
        " */\n"
    )
    faces = "\n".join(font_face(*f) for f in FONTS)
    body = (ROOT / "src" / "theme.css").read_text()
    out = ROOT / "theme.css"
    out.write_text(f"{header}\n{faces}\n{body}")
    print(f"wrote {out} ({out.stat().st_size / 1024:.0f} KiB)")


if __name__ == "__main__":
    main()
