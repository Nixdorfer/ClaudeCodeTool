# Kawaii Animation

## Bounce In

- name: bounceIn
- duration: 0.6s
- timing: ease-out
- keyframe-0: opacity 0 scale(0.3)
- keyframe-50: scale(1.05)
- keyframe-70: scale(0.95)
- keyframe-100: opacity 1 scale(1)
- use: element entry modal appearance card reveal

## Float

- name: float
- duration: 3s
- timing: ease-in-out
- iteration: infinite
- keyframe-0: translateY(0)
- keyframe-50: translateY(-10px)
- keyframe-100: translateY(0)
- use: decorative elements icons idle state indicators

## Particle Fall

- name: particleFall
- duration-min: 4s
- duration-max: 8s
- timing: linear
- fill-mode: forwards
- keyframe-0: translateY(0) rotate(0deg) opacity 0.6
- keyframe-100: translateY(100vh) rotate(360deg) opacity 0
- horizontal-drift: translateX with sine wave amplitude 30px period 2s
- use: falling stars hearts flowers sparkles

## Swing

- name: swing
- duration: 2s
- timing: ease-in-out
- iteration: infinite
- keyframe-0: rotate(0deg)
- keyframe-25: rotate(8deg)
- keyframe-50: rotate(0deg)
- keyframe-75: rotate(-8deg)
- keyframe-100: rotate(0deg)
- use: hanging decorations pendants tags

## Twinkle

- name: twinkle
- duration: 2s
- timing: ease-in-out
- iteration: infinite
- keyframe-0: opacity 1 scale(1)
- keyframe-50: opacity 0.5 scale(0.8)
- keyframe-100: opacity 1 scale(1)
- use: star decorations sparkle effects floral ornaments

## Rainbow Flow

- name: rainbow
- duration: 4s
- timing: linear
- iteration: infinite
- keyframe-0: background-position 0% 50%
- keyframe-100: background-position 200% 50%
- use: dividers progress bars decorative borders

## Jelly

- name: jelly
- duration: 0.5s
- timing: ease
- keyframe-0: scale(1, 1)
- keyframe-25: scale(0.9, 1.1)
- keyframe-50: scale(1.1, 0.9)
- keyframe-75: scale(0.95, 1.05)
- keyframe-100: scale(1, 1)
- use: button press feedback icon interaction tap response

## Pulse Glow

- name: pulseGlow
- duration: 2s
- timing: ease-in-out
- iteration: infinite
- keyframe-0: box-shadow 0 0 0 0 accent-primary-at-0.4
- keyframe-50: box-shadow 0 0 20px 10px accent-primary-at-0.1
- keyframe-100: box-shadow 0 0 0 0 accent-primary-at-0.4
- use: notification badges active states attention indicators

## Wobble

- name: wobble
- duration: 1s
- timing: ease-in-out
- keyframe-0: rotate(0deg)
- keyframe-15: rotate(-5deg)
- keyframe-30: rotate(4deg)
- keyframe-45: rotate(-3deg)
- keyframe-60: rotate(2deg)
- keyframe-75: rotate(-1deg)
- keyframe-100: rotate(0deg)
- use: error feedback attention-grab playful hover

## Scale Pop

- name: scalePop
- duration: 0.3s
- timing: cubic-bezier(0.175, 0.885, 0.32, 1.275)
- keyframe-0: scale(0)
- keyframe-100: scale(1)
- use: tooltip appearance badge count update popover entry

## Slide Up Fade

- name: slideUpFade
- duration: 0.4s
- timing: ease-out
- keyframe-0: opacity 0 translateY(20px)
- keyframe-100: opacity 1 translateY(0)
- use: list item stagger card grid reveal content sections

## Heartbeat

- name: heartbeat
- duration: 1.2s
- timing: ease-in-out
- iteration: infinite
- keyframe-0: scale(1)
- keyframe-14: scale(1.15)
- keyframe-28: scale(1)
- keyframe-42: scale(1.15)
- keyframe-70: scale(1)
- keyframe-100: scale(1)
- use: like buttons favorite indicators love-themed decorations

## Transition Defaults

- hover-duration: 0.3s
- hover-timing: ease
- active-duration: 0.15s
- active-timing: ease-out
- modal-enter: bounceIn 0.6s ease-out
- modal-exit: opacity 0.2s ease-in + scale(0.95)
- page-transition: slideUpFade 0.4s ease-out
- stagger-delay: 0.08s per item
- max-stagger-items: 12

## Performance Rules

- prefer transform and opacity for animations
- use will-change sparingly only on actively animating elements
- remove will-change after animation completes
- particle limit: max 20 simultaneous particles
- disable animations when prefers-reduced-motion is set
- use requestAnimationFrame for JS-driven animations
