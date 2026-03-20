# Kawaii Effects

## Wave Divider Border

- type: svg wave path
- height: 60px
- width: 100%
- wave-amplitude: 20px
- wave-frequency: 2 periods per viewport width
- fill: accent-primary or bg-secondary
- position: between sections
- overflow: hidden
- line-height: 0

## Star and Heart Particles

- symbols: heart star flower hollow-heart sparkle
- particle-count: moderate density
- spawn-interval: 800ms
- spawn-position: top edge random x (0-100vw)
- particle-size-min: 12px
- particle-size-max: 26px
- particle-colors: accent-primary accent-secondary accent-warm accent-tertiary
- fall-duration-min: 4s
- fall-duration-max: 8s
- fall-timing: linear
- opacity: 0.6
- pointer-events: none
- z-index: 9999
- horizontal-drift: subtle sine wave +/- 30px
- rotation: random 0-360deg during fall
- cleanup-delay: 8000ms

## Candy Gloss

- type: pseudo-element overlay
- position: absolute top-left
- width: 60%
- height: 50%
- background: linear-gradient(135deg, rgba(255,255,255,0.4) 0%, rgba(255,255,255,0) 60%)
- border-radius: inherit
- pointer-events: none

## Rainbow Gradient Bar

- height: 3px
- background: linear-gradient(90deg, accent-primary, accent-secondary, accent-tertiary, accent-warm, accent-primary)
- background-size: 200% 100%
- animation-name: rainbow-flow
- animation-duration: 4s
- animation-timing: linear
- animation-iteration: infinite
- keyframe-0: background-position 0% 50%
- keyframe-100: background-position 200% 50%
- border-radius: 2px

## Bubble Effect

- type: floating circles
- count: 8-12 per container
- size-range: 4px to 20px
- background: accent-primary-at-0.08 to accent-primary-at-0.15
- border: 1px solid accent-primary-at-0.1
- border-radius: 50%
- animation: float upward with slight horizontal wobble
- duration-range: 6s to 12s
- delay-range: 0s to 4s
- opacity-range: 0.3 to 0.7
- pointer-events: none

## Floral Decoration

- type: pseudo-element or absolute positioned element
- content: flower emoji or svg flower
- positions: corners of containers or flanking titles
- size: 1rem to 2rem
- animation: twinkle scale pulse
- twinkle-keyframe-0: opacity 1 scale(1)
- twinkle-keyframe-50: opacity 0.5 scale(0.8)
- twinkle-keyframe-100: opacity 1 scale(1)
- twinkle-duration: 2s
- twinkle-timing: ease-in-out
- twinkle-iteration: infinite
- stagger-delay: 0.5s between adjacent decorations

## Twinkling Stars

- type: pseudo-elements or generated spans
- content: sparkle symbols
- size: 0.5rem to 1.2rem
- color: accent-warm or accent-primary
- animation-name: twinkle
- animation-duration: 1.5s to 3s
- animation-timing: ease-in-out
- animation-iteration: infinite
- random-delay: 0s to 2s
- opacity-range: 0.3 to 1.0
- scale-range: 0.6 to 1.0
- position: scattered across background or near interactive elements

## Sparkle Trail on Hover

- trigger: mousemove over interactive elements
- particle-type: small star or dot
- particle-size: 4px to 8px
- particle-color: accent-warm
- particle-lifetime: 600ms
- fade-out: opacity 1 to 0
- scale-out: scale(1) to scale(0)
- spread: random offset +/- 10px from cursor
