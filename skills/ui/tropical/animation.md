# Tropical Paradise Animation

## 波浪轻摇 Wave Float

```css
@keyframes waveFloat {
  0%, 100% { transform: translateY(0) rotate(0deg); }
  25% { transform: translateY(-8px) rotate(1deg); }
  75% { transform: translateY(4px) rotate(-1deg); }
}

.wave-float {
  animation: waveFloat 4s ease-in-out infinite;
}
```

| 参数 | 值 |
|------|------|
| duration | 4s |
| timing | ease-in-out |
| translateY | -8px / 4px |
| rotate | -1deg / 1deg |
| iteration | infinite |

## 棕榈摇摆 Palm Sway

```css
@keyframes palmSway {
  0%, 100% { transform: rotate(-2deg); }
  50% { transform: rotate(2deg); }
}

.palm-sway {
  transform-origin: bottom center;
  animation: palmSway 5s ease-in-out infinite;
}
```

| 参数 | 值 |
|------|------|
| duration | 5s |
| timing | ease-in-out |
| rotate | -2deg / 2deg |
| origin | bottom center |
| iteration | infinite |

## 日出渐现 Sunrise In

```css
@keyframes sunriseIn {
  from {
    opacity: 0;
    transform: translateY(30px);
    filter: brightness(0.8);
  }
  to {
    opacity: 1;
    transform: translateY(0);
    filter: brightness(1);
  }
}

.sunrise-in {
  animation: sunriseIn 0.8s ease-out;
}
```

| 参数 | 值 |
|------|------|
| duration | 0.8s |
| timing | ease-out |
| translateY | 30px -> 0 |
| brightness | 0.8 -> 1 |
| fill-mode | forwards (if needed) |

## 水波涟漪 Water Ripple

```css
@keyframes waterRipple {
  0% {
    box-shadow: 0 0 0 0 rgba(14, 165, 233, 0.3);
  }
  70% {
    box-shadow: 0 0 0 15px rgba(14, 165, 233, 0);
  }
  100% {
    box-shadow: 0 0 0 0 rgba(14, 165, 233, 0);
  }
}

.water-ripple {
  animation: waterRipple 2s ease-out infinite;
}
```

| 参数 | 值 |
|------|------|
| duration | 2s |
| timing | ease-out |
| max-spread | 15px |
| color | var(--accent-primary) at 0.3 |
| iteration | infinite |

## 鱼群游动 Fish Swim

```css
@keyframes fishSwim {
  0% {
    transform: translateX(-100%) scaleX(1);
    opacity: 0;
  }
  10% {
    opacity: 0.3;
  }
  45% {
    transform: translateX(50vw) scaleX(1);
    opacity: 0.3;
  }
  50% {
    transform: translateX(50vw) scaleX(-1);
    opacity: 0.3;
  }
  90% {
    opacity: 0.3;
  }
  100% {
    transform: translateX(-100%) scaleX(-1);
    opacity: 0;
  }
}

.fish-swim {
  position: fixed;
  bottom: 20px;
  animation: fishSwim 12s linear infinite;
  pointer-events: none;
  z-index: 0;
}
```

| 参数 | 值 |
|------|------|
| duration | 12s |
| timing | linear |
| opacity | 0.3 |
| bottom-offset | 20px |
| direction-flip | scaleX at 50% |

## 海鸥飞过 Seagull Fly

```css
@keyframes seagullFly {
  0% {
    transform: translate(-10vw, 0) scale(0.5);
    opacity: 0;
  }
  10% {
    opacity: 0.2;
  }
  50% {
    transform: translate(50vw, -30px) scale(0.7);
    opacity: 0.15;
  }
  90% {
    opacity: 0.1;
  }
  100% {
    transform: translate(110vw, -10px) scale(0.4);
    opacity: 0;
  }
}

.seagull-fly {
  position: fixed;
  top: 60px;
  animation: seagullFly 15s linear infinite;
  pointer-events: none;
  z-index: 0;
}
```

| 参数 | 值 |
|------|------|
| duration | 15s |
| timing | linear |
| opacity | 0.1-0.2 |
| top-offset | 60px |
| scale | 0.4-0.7 |
| y-drift | -30px |

## 漂浮气泡 Float Bubble

```css
@keyframes floatBubble {
  0% {
    transform: translateY(100%) scale(0.5);
    opacity: 0;
  }
  20% {
    opacity: 0.15;
  }
  80% {
    opacity: 0.1;
  }
  100% {
    transform: translateY(-20vh) scale(1);
    opacity: 0;
  }
}

.float-bubble {
  position: absolute;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--accent-tertiary);
  animation: floatBubble 6s ease-out infinite;
  pointer-events: none;
}
```

| 参数 | 值 |
|------|------|
| duration | 4-8s (randomized) |
| timing | ease-out |
| opacity | 0.1-0.15 |
| bubble-size | 4-12px |
| travel | 100% -> -20vh |

## 交互过渡 Interaction Transitions

```css
.hover-lift {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.hover-lift:hover {
  transform: translateY(-4px);
}

.hover-glow {
  transition: box-shadow 0.3s ease;
}

.hover-glow:hover {
  box-shadow: 0 0 20px rgba(14, 165, 233, 0.15);
}

.press-down:active {
  transform: scale(0.97);
  transition: transform 0.1s ease;
}

.fade-in {
  animation: sunriseIn 0.5s ease-out;
}

.slide-up {
  animation: sunriseIn 0.6s ease-out;
}
```

## 动画时间表

| 动画 | 用途 | 触发 |
|------|------|------|
| waveFloat | 装饰元素 | 自动/无限 |
| palmSway | 棕榈装饰 | 自动/无限 |
| sunriseIn | 页面元素入场 | 出现时/一次 |
| waterRipple | 按钮/焦点反馈 | 交互/无限 |
| fishSwim | 背景装饰 | 自动/无限 |
| seagullFly | 背景装饰 | 自动/无限 |
| floatBubble | 背景装饰 | 自动/无限 |
| hover-lift | 卡片/按钮 | hover |
| press-down | 按钮 | active |

## 减弱动画

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```
