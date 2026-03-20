# Western Fantasy Animations

## Torchlight Flicker

- name: flicker
- keyframes:
  - 0%: opacity 1
  - 50%: opacity 0.85
  - 75%: opacity 0.95
  - 100%: opacity 1
- duration: 3s
- timing: ease-in-out
- iteration: infinite
- apply-to: torch-glow radial gradient elements
- glow-size: 300px circle
- glow-color: radial-gradient(circle, rgba(accent-primary, 0.06), transparent 70%)

## Magic Particle Float

- name: magicFloat
- keyframes:
  - 0%: opacity 0, translateY(20px) scale(0)
  - 50%: opacity 1
  - 100%: opacity 0, translateY(-40px) scale(1)
- duration: 2s to 4s (randomized per particle)
- timing: ease-in-out
- iteration: infinite
- delay: random 0s to 3s per particle
- particle-size: 3px to 6px
- particle-glow: box-shadow 0 0 6px accent-primary

## Rune Glow Pulse

- name: runeGlow
- keyframes:
  - 0%: text-shadow 0 0 5px rgba(accent-secondary, 0.3)
  - 50%: text-shadow 0 0 15px rgba(accent-secondary, 0.6), 0 0 30px rgba(accent-secondary, 0.3)
  - 100%: text-shadow 0 0 5px rgba(accent-secondary, 0.3)
- duration: 3s
- timing: ease-in-out
- iteration: infinite

## Treasure Chest Open

- name: chestOpen
- keyframes:
  - 0%: rotateX(0deg), opacity for glow 0
  - 40%: rotateX(-100deg)
  - 60%: rotateX(-90deg)
  - 100%: rotateX(-95deg), opacity for glow 1
- duration: 1.2s
- timing: cubic-bezier(0.34, 1.56, 0.64, 1)
- iteration: 1
- fill: forwards
- lid-transform-origin: top center
- glow-burst: radial-gradient gold at 60% keyframe opacity 0 -> 1
- particle-burst: 6-10 gold particles scatter upward at 50% keyframe

## Scroll Unfurl

- name: scrollUnfurl
- keyframes:
  - 0%: scaleY(0.02), opacity 0.5, transform-origin top
  - 30%: scaleY(0.3), opacity 0.8
  - 100%: scaleY(1), opacity 1
- duration: 0.8s
- timing: cubic-bezier(0.22, 0.61, 0.36, 1)
- iteration: 1
- fill: forwards
- border-reveal: border opacity 0 -> 1 synchronized
- content-fade: inner content opacity delayed 0.3s duration 0.4s

## Magic Circle Rotation

- name: magicCircleSpin
- keyframes:
  - 0%: rotate(0deg), opacity 0.6
  - 50%: opacity 1
  - 100%: rotate(360deg), opacity 0.6
- duration: 12s
- timing: linear
- iteration: infinite
- circle-size: 200px to 400px
- circle-border: 1px solid rgba(accent-secondary, 0.3)
- inner-ring: counter-rotate at 8s duration
- rune-symbols: positioned at 60deg intervals on circle edge
- glow: box-shadow 0 0 20px rgba(accent-secondary, 0.1)

## Fade In Rise

- name: fadeInRise
- keyframes:
  - 0%: opacity 0, translateY(20px)
  - 100%: opacity 1, translateY(0)
- duration: 0.6s
- timing: ease-out
- iteration: 1
- fill: forwards
- stagger-delay: 0.1s per child element

## Gold Shimmer

- name: goldShimmer
- keyframes:
  - 0%: background-position -200% center
  - 100%: background-position 200% center
- duration: 3s
- timing: linear
- iteration: infinite
- background: linear-gradient(90deg, accent-primary, accent-highlight, accent-primary)
- background-size: 200% 100%
- background-clip: text
- -webkit-text-fill-color: transparent

## Border Trace

- name: borderTrace
- keyframes:
  - 0%: stroke-dashoffset 100%
  - 100%: stroke-dashoffset 0%
- duration: 1.5s
- timing: ease-in-out
- iteration: 1
- fill: forwards
- method: SVG rect with stroke-dasharray or CSS border-image animation

## Ember Float

- name: emberFloat
- keyframes:
  - 0%: opacity 0, translateY(0) scale(1)
  - 20%: opacity 1
  - 80%: opacity 0.6
  - 100%: opacity 0, translateY(-80px) translateX(var(--drift)) scale(0.3)
- duration: 3s to 5s
- timing: ease-out
- iteration: infinite
- delay: random 0s to 4s
- color: rgba(255, 140, 40, 0.8) to rgba(255, 80, 20, 0.6)
- size: 2px to 4px
- drift: random -20px to 20px (CSS custom property)

## Entrance Sequence (Page Load)

- step-1: vignette fade-in 0.5s
- step-2: background gradient appear 0.3s delay 0.2s
- step-3: stone texture overlay fade 0.4s delay 0.4s
- step-4: hero title fadeInRise 0.6s delay 0.6s
- step-5: content sections fadeInRise staggered 0.1s per item delay 0.8s
- step-6: torch/particle effects start delay 1.2s

## Hover Transitions

- default-duration: 0.3s
- default-timing: ease
- button-hover: box-shadow expand + border brighten + text-shadow glow
- card-hover: translateY(-3px) + border-color change + top-line opacity
- link-hover: color shift to accent
- nav-hover: color shift to gold
- close-hover: color shift to dragon-fire orange
