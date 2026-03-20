# Memphis Design Base

## page

```
background-color: var(--bg-primary)
color: var(--text-primary)
font-family: var(--font-body)
line-height: 1.7
overflow-x: hidden
```

```
body::before
  content: ''
  position: fixed
  top: 10%
  right: -30px
  width: 120px
  height: 120px
  background: var(--accent-tertiary)
  border-radius: 50%
  opacity: 0.15
  z-index: 0
  pointer-events: none
```

```
body::after
  content: ''
  position: fixed
  bottom: 15%
  left: -40px
  width: 150px
  height: 150px
  background: var(--accent-primary)
  opacity: 0.1
  z-index: 0
  pointer-events: none
  transform: rotate(45deg)
```

## font

```
--font-heading: 'Fredoka One', 'Noto Sans SC', sans-serif
--font-body: 'DM Sans', 'Poppins', 'Noto Sans SC', sans-serif
--font-display: 'Bungee', 'Rubik Mono One', sans-serif
```

google-fonts: Fredoka One, DM Sans, Poppins, Bungee, Rubik Mono One, Noto Sans SC

## icon

```
stroke: none
fill: var(--accent-primary)
stroke-width: 0
shape-rendering: geometricPrecision
icon-style: geometric-filled
icon-weight: bold
icon-border: 2px solid var(--border-primary)
icon-shadow: 3px 3px 0 var(--border-primary)
icon-size-sm: 20px
icon-size-md: 28px
icon-size-lg: 40px
```

## button

```
border: 3px solid var(--border-primary)
border-radius: 0
padding: 14px 32px
font-family: var(--font-body)
font-size: 1rem
font-weight: 700
cursor: pointer
box-shadow: 5px 5px 0 var(--border-primary)
transition: transform 0.15s ease
```

```
button:hover
  transform: translate(-2px, -2px)
  box-shadow: 7px 7px 0 var(--border-primary)
```

```
button:active
  transform: translate(2px, 2px)
  box-shadow: 2px 2px 0 var(--border-primary)
```

```
button-secondary
  background: var(--bg-primary)
  color: var(--accent-secondary)
  border-color: var(--accent-secondary)
  box-shadow: 5px 5px 0 var(--accent-secondary)
```

```
button-circle
  width: 80px
  height: 80px
  border-radius: 50%
  background: var(--accent-tertiary)
  color: var(--border-primary)
  border: 3px solid var(--border-primary)
  box-shadow: 4px 4px 0 var(--border-primary)
  font-size: 0.8rem
  font-weight: 700
```

```
button-circle:hover
  transform: rotate(10deg) scale(1.05)
```

## modal

```
overlay
  background: var(--shadow-overlay)
  z-index: 1000
  display: flex
  align-items: center
  justify-content: center
```

```
content
  background: var(--bg-primary)
  border: 4px solid var(--border-primary)
  padding: 40px
  max-width: 480px
  width: 90%
  box-shadow: 8px 8px 0 var(--accent-primary)
  transform: rotate(-1deg)
```

```
close-button
  position: absolute
  top: -18px
  right: -18px
  width: 40px
  height: 40px
  border-radius: 50%
  background: var(--accent-secondary)
  border: 3px solid var(--border-primary)
  color: var(--text-inverse)
  font-size: 1.1rem
  font-weight: 700
  box-shadow: 3px 3px 0 var(--border-primary)
```

```
close-button:hover
  background: var(--accent-primary)
```

## scrollbar

```
::-webkit-scrollbar
  width: 12px

::-webkit-scrollbar-track
  background: var(--scrollbar-track)
  border-left: 3px solid var(--border-primary)

::-webkit-scrollbar-thumb
  background: var(--scrollbar-thumb)
  border: 2px solid var(--scrollbar-border)
```

## card

```
background: var(--glass-bg)
border: 3px solid var(--border-primary)
padding: 28px
box-shadow: 6px 6px 0 var(--border-primary)
transition: transform 0.2s ease
```

```
card:nth-child(odd)
  transform: rotate(-1deg)

card:nth-child(even)
  transform: rotate(1deg)
```

```
card:hover
  transform: rotate(0deg) translateY(-4px)
  box-shadow: 8px 8px 0 var(--border-primary)
```

```
card-top-bar
  position: absolute
  top: 0
  left: 0
  width: 100%
  height: 6px
  color-cycle: accent-primary, accent-secondary, accent-tertiary, accent-quaternary
```

## input

```
background: var(--input-bg)
border: 3px solid var(--input-border)
color: var(--input-text)
padding: 12px 16px
font-family: var(--font-body)
font-size: 0.95rem
box-shadow: 4px 4px 0 var(--border-primary)
border-radius: 0
outline: none
transition: box-shadow 0.15s
```

```
input:focus
  box-shadow: 4px 4px 0 var(--accent-secondary)
  border-color: var(--input-border-focus)
```

## navbar

```
position: fixed
top: 0
width: 100%
padding: 12px 32px
background: var(--accent-tertiary)
border-bottom: 4px solid var(--border-primary)
z-index: 100
```

```
nav-brand
  font-family: var(--font-heading)
  color: var(--border-primary)
  font-size: 1.3rem
```

```
nav-link
  color: var(--border-primary)
  font-family: var(--font-body)
  font-weight: 700
  font-size: 0.9rem
  padding: 4px 10px
  transition: all 0.15s
```

```
nav-link:hover
  background: var(--accent-primary)
  color: var(--text-inverse)
```

## divider

```
height: 8px
margin: 50px 0
border: none
pattern: zigzag
stroke: var(--border-primary)
stroke-width: 2
segment-width: 10px
```
