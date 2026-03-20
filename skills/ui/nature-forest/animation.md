# Nature Forest Animation

## 全局动画配置

| 参数 | 值 |
|------|------|
| 默认缓动 | cubic-bezier(0.4, 0, 0.2, 1) |
| 弹性缓动 | cubic-bezier(0.34, 1.56, 0.64, 1) |
| 自然缓动 | cubic-bezier(0.25, 0.46, 0.45, 0.94) |
| 微风缓动 | cubic-bezier(0.37, 0, 0.63, 1) |
| 减速停用偏好 | prefers-reduced-motion: reduce 时禁用所有装饰动画 |

## 树叶飘落

```
@keyframes leafFall
  0%: translateY(0) rotate(0deg) translateX(0) opacity(0.5)
  25%: translateY(25vh) rotate(90deg) translateX(30px)
  50%: translateY(50vh) rotate(180deg) translateX(-20px)
  75%: translateY(75vh) rotate(270deg) translateX(25px)
  100%: translateY(100vh) rotate(360deg) translateX(-10px) opacity(0)

duration: 6s - 12s
timing-function: linear
fill-mode: forwards
生成间隔: 2000ms
最大同屏粒子数: 6
```

## 光斑移动

```
@keyframes sunspot
  0%, 100%: opacity(0.3) scale(1)
  50%: opacity(0.5) scale(1.1)

duration: 4s - 8s
timing-function: ease-in-out
iteration-count: infinite
direction: alternate
```

```
@keyframes sunspotDrift
  0%: translate(0, 0)
  33%: translate(15px, -10px)
  66%: translate(-10px, 8px)
  100%: translate(0, 0)

duration: 15s - 25s
timing-function: ease-in-out
iteration-count: infinite
```

## 微风摇曳

```
@keyframes breeze
  0%, 100%: rotate(0deg) translateX(0)
  25%: rotate(1.5deg) translateX(2px)
  50%: rotate(-1deg) translateX(-1px)
  75%: rotate(0.5deg) translateX(1px)

duration: 4s - 7s
timing-function: ease-in-out
iteration-count: infinite
transform-origin: bottom center
适用: 植物装饰元素 叶子图标
```

## 水波涟漪

```
@keyframes ripple
  0%: width(0) height(0) opacity(0.6) border-width(2px)
  100%: width(80px) height(80px) opacity(0) border-width(0.5px)

duration: 2s
timing-function: ease-out
fill-mode: forwards
触发方式: 点击位置生成
```

```
@keyframes rippleMulti
  0%: scale(0) opacity(0.5)
  50%: scale(0.5) opacity(0.3)
  100%: scale(1) opacity(0)

duration: 1.5s
delay: 第二环 0.3s 第三环 0.6s
```

## 萤火虫

```
@keyframes firefly
  0%, 100%: opacity(0) scale(0.5)
  10%: opacity(0.8) scale(1)
  50%: opacity(0.4) scale(0.8)
  90%: opacity(0.7) scale(1)

duration: 5s - 10s
timing-function: ease-in-out
iteration-count: infinite
```

```
@keyframes fireflyPath
  0%: translate(0, 0)
  20%: translate(30px, -20px)
  40%: translate(-15px, -35px)
  60%: translate(20px, -15px)
  80%: translate(-25px, 10px)
  100%: translate(0, 0)

duration: 12s - 20s
timing-function: ease-in-out
iteration-count: infinite

粒子样式:
  width: 4px
  height: 4px
  border-radius: 50%
  background: rgba(220, 200, 100, 0.8)
  box-shadow: 0 0 8px rgba(220,200,100,0.4), 0 0 20px rgba(220,200,100,0.2)
  最大同屏数: 8
  z-index: 1
  适用场景: 深林幽谷配色
```

## 花瓣散落

```
@keyframes petalFall
  0%: translateY(0) rotate(0deg) translateX(0) opacity(0.6) scale(1)
  30%: translateY(30vh) rotate(120deg) translateX(40px) scale(0.9)
  60%: translateY(60vh) rotate(240deg) translateX(-30px) scale(0.8)
  100%: translateY(100vh) rotate(360deg) translateX(15px) opacity(0) scale(0.6)

duration: 8s - 15s
timing-function: linear
fill-mode: forwards
生成间隔: 3000ms
最大同屏粒子数: 5
适用场景: 春日花园配色

花瓣样式:
  width: 10px
  height: 14px
  border-radius: 50% 0 50% 50%
  background: rgba(210, 155, 165, 0.5)
```

## 日出渐亮

```
@keyframes sunrise
  0%: filter brightness(0.7) saturate(0.8)
  100%: filter brightness(1) saturate(1)

duration: 1.5s
timing-function: ease-out
fill-mode: forwards
触发: 页面加载时
适用: body 或主容器
```

```
@keyframes sunriseGlow
  0%: opacity(0) translateY(20px)
  100%: opacity(1) translateY(0)

duration: 0.8s
timing-function: ease-out
delay: 子元素依次 stagger 0.1s
适用: 页面内各内容块入场
```

## 交互动画

### 按钮悬停
```
hover: translateY(-1px) box-shadow 扩散
active: translateY(0) box-shadow 收缩
duration: 0.3s
timing-function: ease
```

### 叶形按钮变形
```
hover: border-radius 从 30px 8px 30px 8px 变为 8px 30px 8px 30px
duration: 0.3s
timing-function: ease
```

### 卡片悬停
```
hover: translateY(-3px) box-shadow 扩散 border-color 变化
duration: 0.3s
timing-function: ease
```

### Modal 入场
```
overlay: opacity 0 -> 1
  duration: 0.2s
content: scale(0.95) opacity(0) -> scale(1) opacity(1)
  duration: 0.3s
  timing-function: cubic-bezier(0.34, 1.56, 0.64, 1)
```

### Modal 退场
```
content: scale(1) opacity(1) -> scale(0.95) opacity(0)
  duration: 0.2s
overlay: opacity 1 -> 0
  duration: 0.2s
  delay: 0.1s
```

### 页面元素入场 (滚动触发)
```
@keyframes fadeInUp
  0%: opacity(0) translateY(20px)
  100%: opacity(1) translateY(0)

duration: 0.6s
timing-function: cubic-bezier(0.25, 0.46, 0.45, 0.94)
threshold: 0.1 (IntersectionObserver)
stagger: 子元素间隔 0.08s
```

### 手写文字出现
```
@keyframes handwrite
  0%: clip-path inset(0 100% 0 0) opacity(0)
  100%: clip-path inset(0 0 0 0) opacity(1)

duration: 0.8s
timing-function: ease-out
transform: rotate 同步从 -3deg 到目标角度
```

### 叶子摇晃 (hover 图标)
```
@keyframes leafShake
  0%, 100%: rotate(0deg)
  20%: rotate(8deg)
  40%: rotate(-6deg)
  60%: rotate(4deg)
  80%: rotate(-2deg)

duration: 0.6s
timing-function: ease-in-out
iteration-count: 1
```

## 性能约束

| 约束 | 值 |
|------|------|
| 同屏装饰粒子上限 | 20 |
| 装饰动画仅使用 | transform opacity filter |
| 避免触发 layout | 不使用 width height top left 动画 |
| 移动端策略 | 粒子数减半 或完全禁用装饰粒子 |
| will-change | 仅对持续动画元素设置 动画结束后移除 |
| GPU 加速 | transform: translateZ(0) 用于粒子容器 |