# Western Fantasy Typography

## Font Stack

### Title
- primary: MedievalSharp, cursive
- alt: Uncial Antiqua, cursive
- source: Google Fonts

### Body
- primary: Crimson Text, serif
- alt: EB Garamond, serif
- source: Google Fonts

### Rune / Decorative
- primary: Noto Sans Symbols, sans-serif
- source: Google Fonts

### CJK Fallback
- Noto Serif SC, SimSun, serif

## Font Sizes

- hero: clamp(2.5rem, 6vw, 4.5rem)
- h1: clamp(2rem, 4vw, 3rem)
- h2: clamp(1.5rem, 3vw, 2.2rem)
- h3: clamp(1.2rem, 2.5vw, 1.6rem)
- h4: clamp(1rem, 2vw, 1.3rem)
- body-lg: 1.125rem
- body: 1rem
- body-sm: 0.875rem
- caption: 0.75rem
- button: 1rem
- nav: 1rem
- brand: 1.3rem
- rune-decoration: 0.8em relative to parent

## Font Weights

- hero: 400 (MedievalSharp is single weight)
- heading: 400
- body-normal: 400
- body-bold: 600
- body-semibold: 600
- button: 400 (title font)
- nav: 400

## Line Heights

- hero: 1.2
- heading: 1.3
- body: 1.8
- compact: 1.5
- button: 1.2

## Letter Spacing

- hero: 0.05em
- heading: 0.04em
- body: 0.01em
- button: 0.08em
- uppercase-label: 0.12em
- nav: 0.02em

## Text Shadow

- hero: 0 0 20px rgba(accent-primary, 0.3), 0 2px 4px rgba(0,0,0,0.5)
- heading: 0 0 10px rgba(accent-primary, 0.2), 0 1px 3px rgba(0,0,0,0.4)
- glow-hover: 0 0 8px rgba(accent-primary, 0.5)
- rune: 0 0 5px rgba(accent-secondary, 0.3)
- none: none (body text)

## Drop Cap (First Letter)

- selector: p.drop-cap::first-letter
- font-family: title-font
- font-size: 3.5em
- float: left
- line-height: 0.8
- margin-right: 8px
- margin-top: 4px
- color: accent-highlight
- text-shadow: hero text-shadow

## Border Radius

- none: 0px (stone/medieval feel)
- minimal: 2px
- small: 4px (scrollbar thumb, tooltips)
- medium: 6px (rare, soft elements)
- round: 50% (particles, avatars)
- shield-clip: polygon via clip-path

## Text Decoration

- link-underline: none by default
- link-hover: underline with text-decoration-color rgba(accent-primary, 0.5)
- heading-ornament-before: pseudo-element sword symbol U+2694 with margin-right 15px
- heading-ornament-after: pseudo-element sword symbol U+2694 with margin-left 15px
- ornament-size: 0.8em relative

## Paragraph

- margin-bottom: 1.5em
- max-width: 70ch
- text-align: left (body), center (hero/section-title)
- text-indent: 0 (default), 1.5em (optional book-style)

## Lists

- list-style-type: U+25C6 (diamond) or U+2726 (star)
- list-item-spacing: 0.5em
- marker-color: accent-primary
