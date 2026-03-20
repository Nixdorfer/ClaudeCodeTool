# Memphis Design Effects

## geometric-decorations

### circle

```
width: 80px
height: 80px
border-radius: 50%
border: 4px solid var(--accent-primary)
position: absolute
background: transparent
```

### circle-filled

```
width: 60px
height: 60px
border-radius: 50%
background: var(--accent-tertiary)
opacity: 0.2
position: absolute
```

### triangle

```
width: 0
height: 0
border-left: 40px solid transparent
border-right: 40px solid transparent
border-bottom: 70px solid var(--accent-secondary)
position: absolute
```

### triangle-outline

```
clip-path: polygon(50% 0%, 0% 100%, 100% 100%)
border: 4px solid var(--accent-quaternary)
width: 60px
height: 60px
background: transparent
position: absolute
```

### square

```
width: 50px
height: 50px
border: 4px solid var(--accent-primary)
background: transparent
position: absolute
transform: rotate(15deg)
```

### square-filled

```
width: 40px
height: 40px
background: var(--accent-secondary)
opacity: 0.15
position: absolute
transform: rotate(45deg)
```

### cross

```
width: 40px
height: 40px
position: absolute
background: linear-gradient(var(--accent-primary), var(--accent-primary)) center/8px 100% no-repeat, linear-gradient(var(--accent-primary), var(--accent-primary)) center/100% 8px no-repeat
```

### semicircle

```
width: 60px
height: 30px
border-radius: 60px 60px 0 0
background: var(--accent-tertiary)
position: absolute
```

## pattern-zigzag

```
background: repeating-linear-gradient(-45deg, var(--accent-tertiary), var(--accent-tertiary) 10px, transparent 10px, transparent 20px)
height: 20px
width: 200px
position: absolute
```

## pattern-dots

```
background-image: radial-gradient(var(--accent-primary) 3px, transparent 3px)
background-size: 15px 15px
position: absolute
```

## pattern-dots-large

```
background-image: radial-gradient(var(--accent-secondary) 5px, transparent 5px)
background-size: 25px 25px
position: absolute
opacity: 0.3
```

## pattern-stripes

```
background: repeating-linear-gradient(0deg, var(--accent-primary), var(--accent-primary) 4px, transparent 4px, transparent 12px)
position: absolute
opacity: 0.2
```

## pattern-diagonal-stripes

```
background: repeating-linear-gradient(45deg, var(--accent-secondary), var(--accent-secondary) 3px, transparent 3px, transparent 15px)
position: absolute
opacity: 0.15
```

## pattern-checkerboard

```
background-image: linear-gradient(45deg, var(--accent-tertiary) 25%, transparent 25%), linear-gradient(-45deg, var(--accent-tertiary) 25%, transparent 25%), linear-gradient(45deg, transparent 75%, var(--accent-tertiary) 75%), linear-gradient(-45deg, transparent 75%, var(--accent-tertiary) 75%)
background-size: 20px 20px
background-position: 0 0, 0 10px, 10px -10px, -10px 0px
opacity: 0.1
position: absolute
```

## wave-line

```
background: url("data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 width=%2780%27 height=%2720%27%3E%3Cpath d=%27M0 10 Q20 0 40 10 Q60 20 80 10%27 fill=%27none%27 stroke=%27%233366ff%27 stroke-width=%273%27/%3E%3C/svg%3E")
background-repeat: repeat-x
height: 20px
position: absolute
```

## wave-line-thick

```
background: url("data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 width=%2780%27 height=%2724%27%3E%3Cpath d=%27M0 12 Q20 2 40 12 Q60 22 80 12%27 fill=%27none%27 stroke=%27%23ff3366%27 stroke-width=%275%27/%3E%3C/svg%3E")
background-repeat: repeat-x
height: 24px
position: absolute
```

## thick-border-system

```
border-width-sm: 2px
border-width-md: 3px
border-width-lg: 4px
border-width-xl: 6px
border-style: solid
border-color: var(--border-primary)
```

## offset-shadow

```
shadow-sm: 3px 3px 0 var(--shadow-card)
shadow-md: 5px 5px 0 var(--shadow-card)
shadow-lg: 8px 8px 0 var(--shadow-card)
shadow-xl: 12px 12px 0 var(--shadow-card)
shadow-accent-sm: 3px 3px 0 var(--shadow-accent)
shadow-accent-md: 5px 5px 0 var(--shadow-accent)
shadow-accent-lg: 8px 8px 0 var(--shadow-accent)
```

## offset-shadow-hover

```
shadow-sm-hover: 5px 5px 0 var(--shadow-card)
shadow-md-hover: 7px 7px 0 var(--shadow-card)
shadow-lg-hover: 10px 10px 0 var(--shadow-card)
transform-hover: translate(-2px, -2px)
```

## offset-shadow-active

```
shadow-sm-active: 1px 1px 0 var(--shadow-card)
shadow-md-active: 2px 2px 0 var(--shadow-card)
shadow-lg-active: 4px 4px 0 var(--shadow-card)
transform-active: translate(2px, 2px)
```

## color-stripe-bar

```
height: 6px
width: 100%
background: linear-gradient(90deg, var(--accent-primary) 0% 20%, var(--accent-secondary) 20% 40%, var(--accent-tertiary) 40% 60%, var(--accent-quaternary) 60% 80%, var(--accent-quinary) 80% 100%)
```

## rotation-transform

```
rotate-slight-ccw: rotate(-2deg)
rotate-slight-cw: rotate(2deg)
rotate-tilt-ccw: rotate(-5deg)
rotate-tilt-cw: rotate(5deg)
rotate-strong-ccw: rotate(-10deg)
rotate-strong-cw: rotate(10deg)
```

## skew-transform

```
skew-slight: skewX(-2deg)
skew-moderate: skewX(-5deg)
skew-strong: skewX(-8deg)
```

## scattered-placement

```
placement-top-right: top: 8%; right: 5%
placement-top-left: top: 12%; left: 3%
placement-mid-right: top: 45%; right: -2%
placement-mid-left: top: 50%; left: -3%
placement-bottom-right: bottom: 10%; right: 8%
placement-bottom-left: bottom: 15%; left: 5%
z-index: 0
pointer-events: none
```

