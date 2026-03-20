# Memphis Design Typography

## font-stack

```
--font-heading: Fredoka One, Noto Sans SC, Microsoft YaHei, sans-serif
--font-body: DM Sans, Poppins, Noto Sans SC, Microsoft YaHei, sans-serif
--font-display: Bungee, Rubik Mono One, Noto Sans SC, sans-serif
--font-mono: Space Mono, Courier New, monospace
```

## heading

### h1-hero

```
font-family: var(--font-heading)
font-size: clamp(2.5rem, 7vw, 5rem)
font-weight: 400
color: var(--text-heading)
line-height: 1.1
letter-spacing: -0.02em
text-align: center
border-radius: 0
```

### h1-hero-outline

```
font-family: var(--font-heading)
font-size: clamp(2.5rem, 7vw, 5rem)
font-weight: 400
-webkit-text-stroke: 3px var(--text-heading)
color: transparent
line-height: 1.1
letter-spacing: -0.02em
```

### h2-section

```
font-family: var(--font-heading)
font-size: clamp(1.3rem, 3vw, 2rem)
font-weight: 400
color: var(--accent-secondary)
display: inline-block
padding: 4px 16px
background: var(--accent-tertiary)
transform: rotate(-2deg)
line-height: 1.3
border-radius: 0
```

### h3-subsection

```
font-family: var(--font-heading)
font-size: clamp(1.1rem, 2.2vw, 1.5rem)
font-weight: 400
color: var(--text-heading)
line-height: 1.3
border-radius: 0
```

### h4-label

```
font-family: var(--font-body)
font-size: clamp(0.95rem, 1.8vw, 1.15rem)
font-weight: 700
color: var(--text-primary)
text-transform: uppercase
letter-spacing: 0.08em
line-height: 1.4
border-radius: 0
```

## display

### display-large

```
font-family: var(--font-display)
font-size: clamp(3rem, 10vw, 7rem)
font-weight: 400
color: var(--accent-primary)
line-height: 1.0
letter-spacing: 0.02em
text-transform: uppercase
```

### display-rotated

```
font-family: var(--font-display)
font-size: clamp(1.5rem, 4vw, 3rem)
font-weight: 400
color: var(--accent-secondary)
transform: rotate(-5deg)
display: inline-block
```

### display-sticker

```
font-family: var(--font-heading)
font-size: clamp(1rem, 2vw, 1.5rem)
font-weight: 400
color: var(--text-heading)
background: var(--accent-tertiary)
border: 3px solid var(--border-primary)
padding: 8px 20px
box-shadow: 4px 4px 0 var(--border-primary)
transform: rotate(3deg)
display: inline-block
border-radius: 0
```

## body

### body-default

```
font-family: var(--font-body)
font-size: 1rem
font-weight: 400
color: var(--text-primary)
line-height: 1.7
letter-spacing: 0
```

### body-bold

```
font-family: var(--font-body)
font-size: 1rem
font-weight: 700
color: var(--text-primary)
line-height: 1.7
```

### body-small

```
font-family: var(--font-body)
font-size: 0.875rem
font-weight: 400
color: var(--text-secondary)
line-height: 1.6
```

### body-caption

```
font-family: var(--font-body)
font-size: 0.75rem
font-weight: 500
color: var(--text-muted)
line-height: 1.5
text-transform: uppercase
letter-spacing: 0.06em
```

## link

```
color: var(--text-link)
font-weight: 700
text-decoration: none
border-bottom: 2px solid var(--accent-primary)
transition: background 0.15s
padding: 0 2px
```

```
link:hover
  background: var(--accent-primary)
  color: var(--text-inverse)
```

## font-weight-scale

```
light: 300
regular: 400
medium: 500
semibold: 600
bold: 700
extrabold: 800
black: 900
```

## spacing

```
letter-spacing-tight: -0.02em
letter-spacing-normal: 0
letter-spacing-wide: 0.04em
letter-spacing-wider: 0.08em
word-spacing-normal: 0
word-spacing-wide: 0.05em
```

## border-radius

```
radius-none: 0
radius-sm: 0
radius-md: 0
radius-lg: 0
radius-pill: 50px
radius-circle: 50%
```

## underline-wave

```
display: block
margin: 12px auto 0
width: 60%
height: 8px
background: url("data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 width=%2740%27 height=%278%27%3E%3Cpath d=%27M0 4 Q10 0 20 4 Q30 8 40 4%27 fill=%27none%27 stroke=%27%23ff3366%27 stroke-width=%273%27/%3E%3C/svg%3E")
background-repeat: repeat-x
```

