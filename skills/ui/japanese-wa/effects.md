# 和风日式特效系统

## 和纸纹理

全局叠加层(::before):
```
position: fixed
inset: 0
background-image: url("data:image/svg+xml,%3Csvg width='100' height='100' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence baseFrequency='0.9' numOctaves='5' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.03'/%3E%3C/svg%3E")
pointer-events: none
z-index: 0
```

局部和纸(card/panel):
```
background-image: url("data:image/svg+xml,%3Csvg width='60' height='60' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='w'%3E%3CfeTurbulence baseFrequency='1.2' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23w)' opacity='0.04'/%3E%3C/svg%3E")
background-blend-mode: overlay
```

## 墨渍晕染

径向渐变墨点:
```
background: radial-gradient(
  ellipse at var(--ink-x, 50%) var(--ink-y, 50%),
  var(--accent-subtle) 0%,
  transparent 70%
)
pointer-events: none
opacity: 0.6
```

SVG 滤镜墨迹:
```
filter: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='ink'%3E%3CfeTurbulence baseFrequency='0.04' numOctaves='4' seed='2'/%3E%3CfeDisplacementMap in='SourceGraphic' scale='6'/%3E%3C/filter%3E%3C/svg%3E#ink")
```

墨渍扩散动画:
```
@keyframes ink-bleed {
  0% { filter: blur(0px); opacity: 0; transform: scale(0.8) }
  50% { filter: blur(2px); opacity: 0.7 }
  100% { filter: blur(0px); opacity: 1; transform: scale(1) }
}
animation: ink-bleed 1.2s cubic-bezier(0.22, 1, 0.36, 1) forwards
```

## 障子格窗

十字格窗:
```
background:
  repeating-linear-gradient(
    90deg,
    transparent,
    transparent calc(33.33% - 0.5px),
    var(--border-subtle) calc(33.33% - 0.5px),
    var(--border-subtle) calc(33.33% + 0.5px),
    transparent calc(33.33% + 0.5px)
  ),
  repeating-linear-gradient(
    0deg,
    transparent,
    transparent calc(33.33% - 0.5px),
    var(--border-subtle) calc(33.33% - 0.5px),
    var(--border-subtle) calc(33.33% + 0.5px),
    transparent calc(33.33% + 0.5px)
  )
opacity: 0.3
pointer-events: none
```

横向障子:
```
background: repeating-linear-gradient(
  0deg,
  transparent,
  transparent calc(25% - 0.5px),
  var(--border-subtle) calc(25% - 0.5px),
  var(--border-subtle) calc(25% + 0.5px),
  transparent calc(25% + 0.5px)
)
opacity: 0.25
```

木框边:
```
border: 2px solid var(--border-strong)
box-shadow: inset 0 0 0 4px var(--bg-primary), inset 0 0 0 5px var(--border-default)
```

## 枯山水纹波

同心圆波纹:
```
background: repeating-radial-gradient(
  circle at center,
  transparent,
  transparent 18px,
  var(--border-subtle) 18px,
  var(--border-subtle) 19px
)
```

平行砂纹:
```
background: repeating-linear-gradient(
  0deg,
  transparent,
  transparent 5px,
  var(--border-subtle) 5px,
  var(--border-subtle) 6px
)
```

流水纹 SVG:
```
background-image: url("data:image/svg+xml,%3Csvg width='200' height='40' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M0 20 Q25 10 50 20 T100 20 T150 20 T200 20' fill='none' stroke='%23b4aa9b' stroke-width='0.5' opacity='0.3'/%3E%3C/svg%3E")
background-repeat: repeat
background-size: 200px 40px
```

## 樱花飘落粒子

```
@keyframes sakura-fall {
  0% { transform: translateY(-10vh) translateX(0) rotate(0deg); opacity: 0 }
  10% { opacity: 1 }
  90% { opacity: 1 }
  100% { transform: translateY(105vh) translateX(80px) rotate(360deg); opacity: 0 }
}

.sakura-petal {
  position: fixed
  width: 10px
  height: 10px
  background: var(--accent-primary)
  clip-path: polygon(50% 0%, 80% 30%, 100% 60%, 80% 100%, 50% 80%, 20% 100%, 0% 60%, 20% 30%)
  animation: sakura-fall var(--duration, 8s) linear infinite
  animation-delay: var(--delay, 0s)
  opacity: 0
  pointer-events: none
  z-index: 0
}
```

## 竹影摇曳

```
@keyframes bamboo-shadow {
  0%, 100% { transform: skewX(-2deg) scaleY(1) }
  25% { transform: skewX(1deg) scaleY(1.02) }
  75% { transform: skewX(-1deg) scaleY(0.98) }
}

.bamboo-shadow {
  position: absolute
  width: 2px
  height: 100%
  background: linear-gradient(to bottom, transparent, var(--border-subtle), transparent)
  animation: bamboo-shadow 6s ease-in-out infinite
  opacity: 0.15
}
```

## 水墨渐变背景

```
background: linear-gradient(
  180deg,
  var(--bg-primary) 0%,
  var(--bg-secondary) 40%,
  var(--bg-tertiary) 70%,
  var(--bg-secondary) 100%
)
```

水墨湿润效果:
```
background: radial-gradient(
  ellipse at 30% 20%,
  var(--accent-subtle) 0%,
  transparent 50%
),
radial-gradient(
  ellipse at 70% 80%,
  var(--accent-subtle) 0%,
  transparent 40%
),
var(--bg-primary)
```

## 金箔点缀

```
background-image: radial-gradient(
  1px 1px at var(--x1, 20%) var(--y1, 30%),
  rgba(192, 168, 96, 0.6) 50%,
  transparent 50%
),
radial-gradient(
  1.5px 1.5px at var(--x2, 65%) var(--y2, 15%),
  rgba(192, 168, 96, 0.4) 50%,
  transparent 50%
),
radial-gradient(
  1px 1px at var(--x3, 80%) var(--y3, 70%),
  rgba(192, 168, 96, 0.5) 50%,
  transparent 50%
)
```

## 涟漪点击反馈

```
@keyframes ripple {
  0% { transform: scale(0); opacity: 0.5 }
  100% { transform: scale(4); opacity: 0 }
}

.ripple {
  position: absolute
  width: 20px
  height: 20px
  border-radius: 50%
  background: var(--accent-primary)
  animation: ripple 0.6s cubic-bezier(0, 0.55, 0.45, 1) forwards
  pointer-events: none
}
```

## 雾气过渡

```
@keyframes fog-in {
  0% { opacity: 0; filter: blur(8px) }
  100% { opacity: 1; filter: blur(0) }
}

@keyframes fog-out {
  0% { opacity: 1; filter: blur(0) }
  100% { opacity: 0; filter: blur(8px) }
}
animation: fog-in 0.8s cubic-bezier(0.22, 1, 0.36, 1) forwards
```

