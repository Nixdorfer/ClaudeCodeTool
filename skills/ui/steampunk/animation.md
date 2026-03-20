# Steampunk Animation

## 通用缓动函数

| 名称 | 值 | 用途 |
|------|-----|------|
| 机械线性 | linear | 齿轮旋转 持续运转 |
| 蒸汽缓出 | cubic-bezier(0.22, 0.61, 0.36, 1) | 蒸汽喷射 元素进入 |
| 弹簧回弹 | cubic-bezier(0.34, 1.56, 0.64, 1) | 指针摆动 压力表 |
| 机械顿挫 | cubic-bezier(0.65, 0, 0.35, 1) | 活塞运动 机械展开 |
| 烛火抖动 | cubic-bezier(0.4, 0, 0.6, 1) | 烛火闪烁 |
| 平滑过渡 | cubic-bezier(0.25, 0.1, 0.25, 1) | hover 状态变化 |

## 通用 transition 时长

| 场景 | 时长 |
|------|------|
| hover 颜色/边框 | 0.3s |
| hover 位移/阴影 | 0.3s |
| 展开/折叠 | 0.4s |
| Modal 进出 | 0.35s |
| 页面切换 | 0.5s |

## 齿轮旋转

主齿轮:
```css
@keyframes gear-spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

animation: gear-spin 15s linear infinite;
```

咬合齿轮 (反向):
```
animation: gear-spin 12s linear infinite reverse;
```

小齿轮 (快速):
```
animation: gear-spin 8s linear infinite;
```

装饰齿轮 (超慢):
```
animation: gear-spin 25s linear infinite;
```

齿轮组参数矩阵:

| 齿轮 | 时长 | 方向 | 尺寸 | 透明度 |
|------|------|------|------|--------|
| 主齿轮 | 15s | normal | 2rem | 0.6 |
| 咬合齿轮 | 12s | reverse | 1.6rem | 0.5 |
| 小齿轮 | 8s | normal | 1rem | 0.4 |
| 背景装饰 | 25s | reverse | 4rem | 0.15 |
| 角落装饰 | 20s | normal | 1.4rem | 0.35 |

## 蒸汽喷射

```css
@keyframes steam-burst {
  0% {
    opacity: 0;
    transform: translateY(0) scale(0.5);
    filter: blur(2px);
  }
  15% {
    opacity: 0.5;
    transform: translateY(-10px) scale(1);
    filter: blur(3px);
  }
  100% {
    opacity: 0;
    transform: translateY(-80px) scale(2.5);
    filter: blur(8px);
  }
}

animation: steam-burst 3s ease-out infinite;
```

蒸汽粒子参数:

| 属性 | 值 |
|------|-----|
| 粒子尺寸 | 15px - 25px |
| 上升距离 | -60px 至 -100px |
| 终态缩放 | 2 至 3 |
| 单次时长 | 2.5s - 4s |
| 起始模糊 | blur(2px) |
| 终态模糊 | blur(6px) - blur(10px) |
| 峰值透明度 | 0.3 - 0.5 |
| 粒子颜色 | rgba(232, 220, 200, 0.3) |
| 粒子形状 | radial-gradient(circle, rgba(232, 220, 200, 0.3), transparent) |

蒸汽延迟序列 (5粒子):
```
delay: 0s, 0.8s, 1.6s, 0.4s, 1.2s
```

## 指针摆动

压力表指针:
```css
@keyframes needle-swing {
  0% { transform: translateX(-50%) rotate(-60deg); }
  20% { transform: translateX(-50%) rotate(30deg); }
  40% { transform: translateX(-50%) rotate(-10deg); }
  60% { transform: translateX(-50%) rotate(15deg); }
  80% { transform: translateX(-50%) rotate(-5deg); }
  100% { transform: translateX(-50%) rotate(var(--target-angle, 0deg)); }
}

animation: needle-swing 2s cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
```

指针抖动 (空闲态):
```css
@keyframes needle-idle {
  0%, 100% { transform: translateX(-50%) rotate(var(--idle-angle, 0deg)); }
  25% { transform: translateX(-50%) rotate(calc(var(--idle-angle, 0deg) + 1.5deg)); }
  75% { transform: translateX(-50%) rotate(calc(var(--idle-angle, 0deg) - 1deg)); }
}

animation: needle-idle 3s cubic-bezier(0.4, 0, 0.6, 1) infinite;
```

指针参数:

| 属性 | 值 |
|------|-----|
| 摆动时长 | 2s |
| 摆动缓动 | cubic-bezier(0.34, 1.56, 0.64, 1) |
| 空闲抖动幅度 | +1.5deg / -1deg |
| 空闲抖动时长 | 3s |
| 指针宽度 | 2px |
| 指针长度 | 容器半径的 75% |
| 轴心尺寸 | 8px |

## 活塞运动

```css
@keyframes piston-pump {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-12px); }
}

animation: piston-pump 1.5s cubic-bezier(0.65, 0, 0.35, 1) infinite;
```

连杆运动:
```css
@keyframes connecting-rod {
  0%, 100% { transform: rotate(-5deg); }
  50% { transform: rotate(5deg); }
}

animation: connecting-rod 1.5s cubic-bezier(0.65, 0, 0.35, 1) infinite;
```

活塞参数:

| 属性 | 值 |
|------|-----|
| 行程距离 | 10px - 15px |
| 周期时长 | 1.2s - 2s |
| 缓动 | cubic-bezier(0.65, 0, 0.35, 1) |
| 连杆摆角 | +/- 5deg |

活塞组延迟序列 (交替运动):
```
piston-1: delay 0s
piston-2: delay 0.5s
piston-3: delay 1s
```

## 烛火闪烁

```css
@keyframes candle-flicker {
  0%, 100% {
    opacity: 1;
    transform: scale(1) translateY(0);
    filter: brightness(1);
  }
  10% {
    opacity: 0.85;
    transform: scale(0.97) translateY(-1px);
    filter: brightness(0.9);
  }
  30% {
    opacity: 0.95;
    transform: scale(1.02) translateY(0.5px);
    filter: brightness(1.05);
  }
  50% {
    opacity: 0.8;
    transform: scale(0.95) translateY(-1.5px);
    filter: brightness(0.85);
  }
  70% {
    opacity: 1;
    transform: scale(1.01) translateY(0);
    filter: brightness(1.1);
  }
  90% {
    opacity: 0.9;
    transform: scale(0.98) translateY(-0.5px);
    filter: brightness(0.95);
  }
}

animation: candle-flicker 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
```

烛火光晕:
```css
@keyframes candle-glow {
  0%, 100% { box-shadow: 0 0 10px rgba(200, 160, 50, 0.3), 0 0 25px rgba(200, 160, 50, 0.15); }
  50% { box-shadow: 0 0 15px rgba(200, 160, 50, 0.45), 0 0 35px rgba(200, 160, 50, 0.2); }
}

animation: candle-glow 2.5s cubic-bezier(0.4, 0, 0.6, 1) infinite;
```

烛火参数:

| 属性 | 值 |
|------|-----|
| 闪烁时长 | 1.5s - 2.5s |
| 缩放范围 | 0.95 - 1.02 |
| 位移范围 | -1.5px 至 0.5px |
| 亮度范围 | 0.85 - 1.1 |
| 光晕内圈 | 10px - 15px |
| 光晕外圈 | 25px - 35px |
| 光晕颜色 | rgba(200, 160, 50, 0.3) |

## 机械展开

折叠面板展开:
```css
@keyframes mechanical-unfold {
  0% {
    max-height: 0;
    opacity: 0;
    transform: scaleY(0.8);
    transform-origin: top;
  }
  40% {
    opacity: 0.6;
    transform: scaleY(1.02);
  }
  70% {
    transform: scaleY(0.99);
  }
  100% {
    max-height: var(--max-height, 500px);
    opacity: 1;
    transform: scaleY(1);
  }
}

animation: mechanical-unfold 0.5s cubic-bezier(0.65, 0, 0.35, 1) forwards;
```

门板展开 (左右):
```css
@keyframes door-open-left {
  0% {
    transform: perspective(800px) rotateY(90deg);
    opacity: 0;
  }
  60% {
    transform: perspective(800px) rotateY(-5deg);
  }
  100% {
    transform: perspective(800px) rotateY(0deg);
    opacity: 1;
  }
}

animation: door-open-left 0.6s cubic-bezier(0.65, 0, 0.35, 1) forwards;
transform-origin: left center;
```

机械展开参数:

| 属性 | 值 |
|------|-----|
| 展开时长 | 0.4s - 0.6s |
| 收起时长 | 0.3s - 0.4s |
| 缓动 | cubic-bezier(0.65, 0, 0.35, 1) |
| 过冲量 | 1.02 (scaleY) / -5deg (rotateY) |
| perspective | 800px (3D展开) |

## 元素进入动画

淡入上移:
```css
@keyframes fade-in-up {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

animation: fade-in-up 0.5s cubic-bezier(0.22, 0.61, 0.36, 1) forwards;
```

交错进入延迟:
```
--stagger-delay: 0.08s
child:nth-child(n) { animation-delay: calc(var(--stagger-delay) * n); }
```

## Hover 状态变化

卡片悬浮:
```css
transition: all 0.3s cubic-bezier(0.25, 0.1, 0.25, 1);

:hover {
  transform: translateY(-2px);
  border-color: rgba(200, 160, 50, 0.7);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4), 0 0 15px rgba(200, 160, 50, 0.1);
}
```

按钮悬浮:
```css
transition: all 0.3s cubic-bezier(0.25, 0.1, 0.25, 1);

:hover {
  transform: translateY(-1px);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.5), 0 0 15px rgba(200, 160, 50, 0.3);
}
```

## 减弱动画 (prefers-reduced-motion)

```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```
