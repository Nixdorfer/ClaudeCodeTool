# Western Fantasy Effects

## Stone Texture Overlay

- method: SVG feTurbulence via data URI on pseudo-element ::after
- baseFrequency: 0.65
- numOctaves: 3
- stitchTiles: stitch
- opacity: 0.03
- position: fixed full-screen
- pointer-events: none
- z-index: 0

## Metal Embossed Border

- border-style: double or ridge
- border-width: 3px outer + 1px inner (box-shadow inset simulation)
- outer-glow: 0 0 8px rgba(accent, 0.2)
- inner-highlight: inset 0 1px 0 rgba(255,255,255,0.05)
- inner-shadow: inset 0 -1px 0 rgba(0,0,0,0.3)
- corner-ornament: pseudo-element diamond/fleur symbols at corners

## Magic Particles

- element-size: 3px to 6px
- shape: border-radius 50%
- color: accent-primary
- glow: box-shadow 0 0 6px accent-primary
- float-distance-y: 60px upward
- float-distance-x: random -10px to 10px
- duration: 2s to 4s
- timing: ease-in-out
- opacity: 0 -> 1 -> 0
- scale: 0 -> 1 -> 0.5
- count: 8-15 particles per container
- stagger: random delay 0s to 3s

## Rune Glow Pulse

- base: text-shadow 0 0 5px rgba(accent-secondary, 0.3)
- peak: text-shadow 0 0 15px rgba(accent-secondary, 0.6), 0 0 30px rgba(accent-secondary, 0.3)
- duration: 3s
- timing: ease-in-out
- iteration: infinite

## Torchlight Flicker

- element: radial-gradient circle 300px
- color: rgba(accent-primary, 0.06) center to transparent 70%
- opacity-range: 0.85 to 1.0
- duration: 3s
- timing: ease-in-out
- position: fixed corners or edges
- pointer-events: none

## Parchment Texture

- background-color: rgba(180, 160, 120, 0.08)
- noise-overlay: SVG feTurbulence baseFrequency 0.9 numOctaves 4 opacity 0.04
- border: 1px solid rgba(160, 140, 100, 0.2)
- box-shadow: inset 0 0 40px rgba(0,0,0,0.15)
- edge-burn: radial-gradient at edges with rgba(0,0,0,0.1)

## Shield Emblem Decoration

- shape: pseudo-element with CSS clip-path shield shape
- clip-path: polygon(50% 0%, 100% 15%, 100% 65%, 50% 100%, 0% 65%, 0% 15%)
- size: 40px to 80px
- border: 2px solid accent-primary
- inner-gradient: linear-gradient(180deg, bg-elevated, bg-primary)
- icon: centered symbol (sword/crown/star)

## Vignette

- method: pseudo-element ::before on body
- background: radial-gradient(ellipse at center, transparent 50%, rgba(0,0,0,0.4) 100%)
- position: fixed full-screen
- pointer-events: none
- z-index: 1

## Gold Accent Line

- height: 2px
- background: linear-gradient(90deg, transparent 0%, accent-primary 50%, transparent 100%)
- opacity: 0.6
- position: top or bottom of container

## Candlelight Ambient

- radial-gradient-1: ellipse at 30% 20% rgba(accent-primary, 0.04) to transparent 50%
- radial-gradient-2: ellipse at 70% 80% rgba(accent-secondary, 0.03) to transparent 50%
- applied-to: body background-image
- layered under stone texture

## Frosted Glass (Frost Northlands variant)

- backdrop-filter: blur(12px) saturate(1.2)
- background: rgba(bg-secondary, 0.6)
- border: 1px solid rgba(accent-primary, 0.15)
- ice-crystal-overlay: SVG feTurbulence baseFrequency 1.2 opacity 0.02
