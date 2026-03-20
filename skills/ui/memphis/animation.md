# Memphis Design Animation

## bounce-rotate-in

```
@keyframes bounceRotateIn
  0%: opacity: 0; transform: scale(0) rotate(-20deg)
  60%: transform: scale(1.1) rotate(3deg)
  80%: transform: scale(0.95) rotate(-1deg)
  100%: opacity: 1; transform: scale(1) rotate(0deg)

duration: 0.5s
timing: ease-out
fill: forwards
```

## bounce-in-up

```
@keyframes bounceInUp
  0%: opacity: 0; transform: translateY(40px) scale(0.9)
  50%: transform: translateY(-8px) scale(1.02)
  70%: transform: translateY(4px) scale(0.99)
  100%: opacity: 1; transform: translateY(0) scale(1)

duration: 0.6s
timing: ease-out
fill: forwards
```

## bounce-in-scale

```
@keyframes bounceInScale
  0%: transform: scale(0)
  60%: transform: scale(1.15)
  80%: transform: scale(0.92)
  100%: transform: scale(1)

duration: 0.5s
timing: ease-out
fill: forwards
```

## slow-spin

```
@keyframes slowSpin
  0%: transform: rotate(0deg)
  100%: transform: rotate(360deg)

duration: 20s
timing: linear
iteration: infinite
```

## reverse-spin

```
@keyframes reverseSpin
  0%: transform: rotate(360deg)
  100%: transform: rotate(0deg)

duration: 25s
timing: linear
iteration: infinite
```

## wiggle

```
@keyframes wiggle
  0%: transform: rotate(0deg)
  25%: transform: rotate(-3deg)
  50%: transform: rotate(0deg)
  75%: transform: rotate(3deg)
  100%: transform: rotate(0deg)

duration: 0.3s
timing: ease-in-out
trigger: hover
```

## shake

```
@keyframes shake
  0%: transform: translateX(0)
  20%: transform: translateX(-6px) rotate(-1deg)
  40%: transform: translateX(6px) rotate(1deg)
  60%: transform: translateX(-4px) rotate(-0.5deg)
  80%: transform: translateX(4px) rotate(0.5deg)
  100%: transform: translateX(0) rotate(0deg)

duration: 0.4s
timing: ease-in-out
```

## color-cycle

```
@keyframes colorCycle
  0%: background-color: var(--accent-primary)
  25%: background-color: var(--accent-secondary)
  50%: background-color: var(--accent-tertiary)
  75%: background-color: var(--accent-quaternary)
  100%: background-color: var(--accent-primary)

duration: 8s
timing: linear
iteration: infinite
```

## color-cycle-text

```
@keyframes colorCycleText
  0%: color: var(--accent-primary)
  25%: color: var(--accent-secondary)
  50%: color: var(--accent-tertiary)
  75%: color: var(--accent-quaternary)
  100%: color: var(--accent-primary)

duration: 6s
timing: linear
iteration: infinite
```

## shadow-shift

```
@keyframes shadowShift
  0%: box-shadow: 5px 5px 0 var(--shadow-card)
  25%: box-shadow: -5px 5px 0 var(--shadow-accent)
  50%: box-shadow: -5px -5px 0 var(--shadow-card)
  75%: box-shadow: 5px -5px 0 var(--shadow-accent)
  100%: box-shadow: 5px 5px 0 var(--shadow-card)

duration: 4s
timing: ease-in-out
iteration: infinite
```

## shadow-pulse

```
@keyframes shadowPulse
  0%: box-shadow: 5px 5px 0 var(--shadow-card)
  50%: box-shadow: 8px 8px 0 var(--shadow-accent)
  100%: box-shadow: 5px 5px 0 var(--shadow-card)

duration: 2s
timing: ease-in-out
iteration: infinite
```

## geo-float

```
@keyframes geoFloat
  0%: transform: translateY(0) rotate(0deg)
  25%: transform: translateY(-15px) rotate(5deg)
  50%: transform: translateY(-8px) rotate(-3deg)
  75%: transform: translateY(-20px) rotate(7deg)
  100%: transform: translateY(0) rotate(0deg)

duration: 6s
timing: ease-in-out
iteration: infinite
```

## geo-float-alt

```
@keyframes geoFloatAlt
  0%: transform: translateY(0) translateX(0) rotate(0deg)
  33%: transform: translateY(-12px) translateX(8px) rotate(-8deg)
  66%: transform: translateY(-18px) translateX(-5px) rotate(5deg)
  100%: transform: translateY(0) translateX(0) rotate(0deg)

duration: 8s
timing: ease-in-out
iteration: infinite
```

## elastic-scale

```
@keyframes elasticScale
  0%: transform: scale(1)
  30%: transform: scale(1.15)
  50%: transform: scale(0.92)
  70%: transform: scale(1.05)
  85%: transform: scale(0.98)
  100%: transform: scale(1)

duration: 0.6s
timing: ease-out
trigger: hover
```

## elastic-press

```
@keyframes elasticPress
  0%: transform: scale(1)
  50%: transform: scale(0.88)
  100%: transform: scale(1)

duration: 0.25s
timing: ease-out
trigger: active
```

## pop-in

```
@keyframes popIn
  0%: transform: scale(0) rotate(-10deg); opacity: 0
  70%: transform: scale(1.08) rotate(2deg); opacity: 1
  100%: transform: scale(1) rotate(0deg); opacity: 1

duration: 0.35s
timing: cubic-bezier(0.175, 0.885, 0.32, 1.275)
fill: forwards
```

## slide-rotate-in

```
@keyframes slideRotateIn
  0%: transform: translateX(-100%) rotate(-15deg); opacity: 0
  100%: transform: translateX(0) rotate(0deg); opacity: 1

duration: 0.5s
timing: ease-out
fill: forwards
```

## stagger-config

```
stagger-delay-base: 0.08s
stagger-delay-fast: 0.05s
stagger-delay-slow: 0.12s
max-stagger-items: 20
```

## transition-defaults

```
transition-fast: 0.15s ease
transition-normal: 0.25s ease
transition-slow: 0.4s ease
transition-bounce: 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275)
transition-elastic: 0.6s cubic-bezier(0.68, -0.55, 0.265, 1.55)
```

## reduced-motion

```
@media (prefers-reduced-motion: reduce)
  animation-duration: 0.01ms
  animation-iteration-count: 1
  transition-duration: 0.01ms
```

