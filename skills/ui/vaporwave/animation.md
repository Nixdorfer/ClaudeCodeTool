# Vaporwave Animation

## 网格滚动

```css
@keyframes gridScroll {
  from { background-position: 0 0; }
  to { background-position: 0 40px; }
}
```

应用目标: .grid-floor
duration: 2s
timing-function: linear
iteration-count: infinite
background-position 的终值必须等于 background-size 的纵向值
移动端可增大 duration 至 3s 以降低性能开销

## 日落脉动

```css
@keyframes sunPulse {
  0%, 100% {
    opacity: 0.5;
    transform: translateX(-50%) scale(1);
  }
  50% {
    opacity: 0.6;
    transform: translateX(-50%) scale(1.03);
  }
}
```

应用目标: .sunset-sun
duration: 6s
timing-function: ease-in-out
iteration-count: infinite
幅度克制 scale 不超过 1.05 opacity 波动不超过 0.15

## CRT 闪烁

```css
@keyframes crtFlicker {
  0%, 100% { opacity: 1; }
  92% { opacity: 1; }
  93% { opacity: 0.8; }
  94% { opacity: 1; }
  96% { opacity: 0.9; }
  97% { opacity: 1; }
}
```

应用目标: .crt-overlay::after 或整个页面容器
duration: 4s
timing-function: steps(1)
iteration-count: infinite
闪烁频率低且短暂 避免引起不适
如用户系统开启 prefers-reduced-motion 则禁用

## 文字色差漂移

```css
@keyframes chromaShift {
  0%, 100% {
    text-shadow: 0 0 10px var(--accent-primary);
  }
  33% {
    text-shadow:
      -2px 0 var(--accent-secondary),
      2px 0 var(--accent-primary);
  }
  66% {
    text-shadow:
      2px 0 var(--accent-point-green),
      -2px 0 var(--accent-tertiary);
  }
}
```

应用目标: 标题文字 装饰文字
duration: 4s
timing-function: ease-in-out
iteration-count: infinite
偏移量 1-3px 过大会导致文字模糊
仅用于少量文字 不可全局应用

## 几何图形旋转

```css
@keyframes geoSpin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

@keyframes geoFloat {
  0%, 100% { transform: translateY(0) rotate(0deg); }
  50% { transform: translateY(-15px) rotate(180deg); }
}
```

应用目标: 装饰性几何图形 (三角形 菱形 圆环)
geoSpin duration: 20s linear infinite
geoFloat duration: 8s ease-in-out infinite
几何图形应为 position: fixed + pointer-events: none + 低 opacity

## 霓虹呼吸

```css
@keyframes neonBreathe {
  0%, 100% {
    box-shadow: 0 0 15px var(--shadow-primary);
  }
  50% {
    box-shadow:
      0 0 25px var(--shadow-primary),
      0 0 50px var(--shadow-secondary);
  }
}
```

应用目标: 卡片 按钮 边框
duration: 3s
timing-function: ease-in-out
iteration-count: infinite
适用于需要吸引注意力的单个元素 不宜大面积使用

## 日文文字纵向滚动

```css
@keyframes jpScroll {
  from { transform: translateY(100vh); }
  to { transform: translateY(-100%); }
}
```

应用目标: .jp-deco 纵向装饰文字
duration: 30s
timing-function: linear
iteration-count: infinite
文字从底部上升至顶部消失 如 Matrix 雨效果的蒸汽波版本

## 入场动画

```css
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes glitchIn {
  0% {
    opacity: 0;
    transform: translate(-5px, 5px);
    clip-path: inset(40% 0 60% 0);
  }
  20% {
    opacity: 1;
    transform: translate(3px, -2px);
    clip-path: inset(20% 0 30% 0);
  }
  40% {
    transform: translate(-2px, 3px);
    clip-path: inset(60% 0 10% 0);
  }
  60% {
    transform: translate(2px, -1px);
    clip-path: inset(10% 0 50% 0);
  }
  80% {
    transform: translate(-1px, 1px);
    clip-path: inset(0);
  }
  100% {
    transform: translate(0);
    clip-path: inset(0);
  }
}
```

fadeInUp: 通用内容入场 duration 0.6s ease-out
glitchIn: 故障风入场 duration 0.5s steps(1) 用于标题或关键元素

## 交互微动画

按钮悬停:
```css
transition: all 0.3s ease;
transform: translateY(-2px);
```

卡片悬停:
```css
transition: all 0.3s ease;
transform: translateY(-3px);
```

链接悬停:
```css
transition: color 0.3s, text-shadow 0.3s;
```

## 无障碍

```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

所有循环动画必须在 prefers-reduced-motion: reduce 下禁用
CRT 闪烁和色差漂移在该模式下必须完全移除
入场动画可保留但缩短至极短时间

## 性能

- 仅使用 transform 和 opacity 做动画 避免 layout/paint 属性
- 对动画元素添加 will-change: transform 或 will-change: opacity
- 移动端减少同时运行的动画数量 (隐藏装饰性动画)
- 几何图形旋转和日文滚动在移动端建议禁用
