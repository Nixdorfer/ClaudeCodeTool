# Western Fantasy Base

## Page

- background: deep stone gray base with subtle radial gradients simulating torchlight
- stone texture overlay via SVG feTurbulence filter (opacity 0.03)
- vignette: radial-gradient dark corners
- min-height: 100vh
- overflow-x: hidden
- position: relative

## Fonts

title: 'MedievalSharp', cursive (Google Fonts)
body: 'Crimson Text', 'EB Garamond', serif (Google Fonts)
rune: 'Noto Sans Symbols', sans-serif
chinese-fallback: 'Noto Serif SC', 'SimSun', serif
gothic-alt: 'Uncial Antiqua', cursive

## Icons

- shield: U+1F6E1
- sword: U+2694
- crossed-swords: U+2694 FE0F
- dragon: U+1F409
- castle: U+1F3F0
- fleur-de-lis: U+269C
- magic-star: U+2728
- diamond: U+25C8
- diamond-small: U+25C6
- diamond-dot: U+2666
- decorative: U+2726

## Buttons

primary:
  background: linear-gradient(180deg, #3a3344 0%, #252030 100%)
  border: 2px solid gold-accent
  color: bright-gold
  padding: 14px 36px
  font-family: title-font
  font-size: 1rem
  letter-spacing: 0.08em
  border-radius: 2px
  pseudo-before: diamond ornament at top center (8px)
  hover: gold glow box-shadow + text-shadow
  active: inset shadow + scale(0.98)
  disabled: opacity 0.5 grayscale

secondary:
  background: transparent
  border: 1px solid rgba(text-color, 0.4)
  color: text-color
  padding: 14px 36px
  font-family: title-font
  hover: purple glow border + purple text

danger:
  background: linear-gradient(180deg, #4a2020 0%, #2a1515 100%)
  border: 2px solid #e86833
  color: #ff9966

## Modal

overlay: rgba(10, 10, 15, 0.85)
content:
  background: linear-gradient(135deg, #252030, #1c1c24)
  border: 2px solid gold-accent
  padding: 44px
  max-width: 520px
  width: 90%
  box-shadow: 0 0 40px rgba(gold, 0.1)
  corner-ornaments: diamond symbols at four corners (pseudo-elements)
  close-button: top-right, text color, hover dragon-fire orange

## Scrollbar

width: 8px
track: background-primary
thumb: linear-gradient(180deg, gold-accent, dark-gold)
thumb-border-radius: 4px

## Card

background: linear-gradient(135deg, rgba(37,32,48,0.9), rgba(28,28,36,0.9))
border: 1px solid rgba(gold, 0.2)
padding: 28px
border-radius: 2px
hover: gold border + gold glow + translateY(-3px)
hover-top-line: linear-gradient gold bar (opacity transition)

## Divider

flex center layout with gap 15px
lines: linear-gradient(90deg, transparent, gold, transparent) height 1px max-width 200px
center-icon: gold accent 1.3rem (sword/diamond/fleur-de-lis)

## Navbar

position: fixed top
background: rgba(28, 28, 36, 0.95)
border-bottom: 1px solid rgba(gold, 0.15)
padding: 14px 40px
brand: title-font bright-gold 1.3rem
links: body-font text-color 1rem hover gold

## Form Input

background: rgba(37, 32, 48, 0.6)
border: 1px solid rgba(text-color, 0.3)
color: text-color
padding: 12px 16px
font-family: body-font
font-size: 1rem
border-radius: 2px
focus: gold border + gold glow shadow
