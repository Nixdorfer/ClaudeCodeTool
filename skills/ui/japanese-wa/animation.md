# 和风日式动画系统

## 缓动函数

```
--ease-wabi: cubic-bezier(0.22, 1, 0.36, 1)
--ease-sabi: cubic-bezier(0.65, 0, 0.35, 1)
--ease-ma: cubic-bezier(0.4, 0, 0, 1)
--ease-zen: cubic-bezier(0.16, 1, 0.3, 1)
--ease-breath: cubic-bezier(0.45, 0, 0.55, 1)
```

## 樱花飘落

```
@keyframes sakura-fall {
  0% {
    transform: translateY(-10vh) translateX(0) rotate(0deg) scale(0.8)
    opacity: 0
  }
  10% { opacity: 0.8 }
  50% { transform: translateY(50vh) translateX(40px) rotate(180deg) scale(1) }
  90% { opacity: 0.6 }
  100% {
    transform: translateY(105vh) translateX(80px) rotate(360deg) scale(0.6)
    opacity: 0
  }
}

@keyframes sakura-sway {
  0%, 100% { transform: translateX(0) rotate(0deg) }
  25% { transform: translateX(15px) rotate(5deg) }
  75% { transform: translateX(-10px) rotate(-3deg) }
}
```

参数:
- duration: 6-12s
- delay: random 0-8s
- iteration: infinite

## 水墨晕染

```
@keyframes ink-bleed {
  0% {
    filter: blur(0px)
    opacity: 0
    transform: scale(0.8)
  }
  40% {
    filter: blur(3px)
    opacity: 0.6
  }
  100% {
    filter: blur(0px)
    opacity: 1
    transform: scale(1)
  }
}

@keyframes ink-spread {
  0% { clip-path: circle(0% at var(--origin-x, 50%) var(--origin-y, 50%)) }
  100% { clip-path: circle(100% at var(--origin-x, 50%) var(--origin-y, 50%)) }
}
```

## 涟漪扩散

```
@keyframes ripple-expand {
  0% {
    transform: scale(0)
    opacity: 0.5
    border-width: 2px
  }
  100% {
    transform: scale(4)
    opacity: 0
    border-width: 0.5px
  }
}

@keyframes zen-ripple {
  0% { box-shadow: 0 0 0 0 var(--accent-subtle) }
  50% { box-shadow: 0 0 0 12px transparent }
  100% { box-shadow: 0 0 0 0 transparent }
}
```

## 风铃摇曳

```
@keyframes furin-sway {
  0%, 100% { transform: rotate(0deg) }
  15% { transform: rotate(8deg) }
  30% { transform: rotate(-6deg) }
  45% { transform: rotate(4deg) }
  60% { transform: rotate(-3deg) }
  75% { transform: rotate(2deg) }
  90% { transform: rotate(-1deg) }
}

@keyframes furin-idle {
  0%, 100% { transform: rotate(0deg) }
  50% { transform: rotate(1.5deg) }
}
```

参数:
- sway: 1.5s var(--ease-wabi) (triggered)
- idle: 4s var(--ease-breath) infinite

## 纸门滑动

```
@keyframes fusuma-slide-in {
  0% { transform: translateX(100%); opacity: 0 }
  100% { transform: translateX(0); opacity: 1 }
}

@keyframes fusuma-slide-out {
  0% { transform: translateX(0); opacity: 1 }
  100% { transform: translateX(-100%); opacity: 0 }
}

@keyframes shoji-open {
  0% { clip-path: inset(0 50% 0 50%) }
  100% { clip-path: inset(0 0 0 0) }
}
```

参数:
- fusuma: 0.6s var(--ease-ma)
- shoji: 0.8s var(--ease-zen)

## 灯笼摇曳

```
@keyframes chouchin-sway {
  0%, 100% { transform: rotate(-2deg) translateY(0) }
  25% { transform: rotate(1.5deg) translateY(-2px) }
  50% { transform: rotate(-1deg) translateY(0) }
  75% { transform: rotate(2deg) translateY(-1px) }
}

@keyframes chouchin-glow {
  0%, 100% { opacity: 0.8; filter: brightness(1) }
  50% { opacity: 1; filter: brightness(1.1) }
}
```

参数:
- sway: 5s var(--ease-breath) infinite
- glow: 3s ease-in-out infinite

## 淡入淡出系列

```
@keyframes fade-in {
  0% { opacity: 0; transform: translateY(12px) }
  100% { opacity: 1; transform: translateY(0) }
}

@keyframes fade-out {
  0% { opacity: 1; transform: translateY(0) }
  100% { opacity: 0; transform: translateY(-8px) }
}

@keyframes fade-in-up {
  0% { opacity: 0; transform: translateY(24px) }
  100% { opacity: 1; transform: translateY(0) }
}

@keyframes fade-scale {
  0% { opacity: 0; transform: scale(0.95) }
  100% { opacity: 1; transform: scale(1) }
}
```

序列淡入(stagger):
```
animation: fade-in 0.5s var(--ease-wabi) backwards
animation-delay: calc(var(--i, 0) * 80ms)
```

## 毛笔描线

```
@keyframes brush-stroke {
  0% { stroke-dashoffset: var(--path-length, 1000) }
  100% { stroke-dashoffset: 0 }
}
stroke-dasharray: var(--path-length, 1000)
stroke-dashoffset: var(--path-length, 1000)
animation: brush-stroke 1.5s var(--ease-sabi) forwards
```

## 云雾流动

```
@keyframes mist-drift {
  0% { transform: translateX(-20%) scaleX(1.2); opacity: 0 }
  30% { opacity: 0.15 }
  70% { opacity: 0.15 }
  100% { transform: translateX(120%) scaleX(1); opacity: 0 }
}
```

参数: 15-25s linear infinite

## 交互反馈

```
--hover-lift: translateY(-2px)
--hover-duration: 0.3s
--active-press: translateY(1px)
--focus-ring: 0 0 0 2px var(--bg-primary), 0 0 0 4px var(--accent-primary)
```

hover:
```
transform: var(--hover-lift)
box-shadow: var(--shadow-medium)
transition: all var(--hover-duration) var(--ease-wabi)
```

active:
```
transform: var(--active-press)
transition: transform 0.1s ease
```

focus-visible:
```
outline: none
box-shadow: var(--focus-ring)
transition: box-shadow 0.2s var(--ease-wabi)
```

## 页面过渡

```
@keyframes page-enter {
  0% { opacity: 0; filter: blur(6px); transform: scale(0.98) }
  100% { opacity: 1; filter: blur(0); transform: scale(1) }
}

@keyframes page-exit {
  0% { opacity: 1; filter: blur(0); transform: scale(1) }
  100% { opacity: 0; filter: blur(4px); transform: scale(1.02) }
}
```

参数: 0.5s var(--ease-ma)

## 时长参考

| 场景 | 时长 | 缓动 |
|------|------|------|
| hover反馈 | 0.3s | ease |
| 点击反馈 | 0.1s | ease |
| 淡入 | 0.5s | --ease-wabi |
| 淡出 | 0.3s | --ease-sabi |
| 滑动过渡 | 0.6s | --ease-ma |
| 弹窗 | 0.4s | --ease-zen |
| 装饰动画 | 3-12s | --ease-breath |
| 页面过渡 | 0.5s | --ease-ma |

## 无障碍

```
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important
    animation-iteration-count: 1 !important
    transition-duration: 0.01ms !important
  }
}
```

