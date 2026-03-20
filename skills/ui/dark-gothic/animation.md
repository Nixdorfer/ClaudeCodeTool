# Dark Gothic Animation

## 烛火摇曳

### candleFlicker
- 用途: 标题光效 图标光源 装饰元素
- duration: 3s
- timing: ease-in-out
- iteration: infinite
- keyframes:
  - 0%: opacity 0.9 filter brightness(1)
  - 25%: opacity 0.85 filter brightness(0.95)
  - 50%: opacity 1.0 filter brightness(1.05)
  - 75%: opacity 0.88 filter brightness(0.98)
  - 100%: opacity 0.9 filter brightness(1)

### candleGlow
- 用途: 背景光斑 区域照明
- duration: 4s
- timing: ease-in-out
- iteration: infinite
- keyframes:
  - 0%: box-shadow 0 0 60px 20px accent-glow opacity 0.6
  - 50%: box-shadow 0 0 80px 30px accent-glow opacity 1.0
  - 100%: box-shadow 0 0 60px 20px accent-glow opacity 0.6

### candleShadow
- 用途: 投射阴影摇动
- duration: 5s
- timing: ease-in-out
- iteration: infinite
- keyframes:
  - 0%: text-shadow 2px 2px 8px shadow-md
  - 33%: text-shadow 3px 1px 10px shadow-md
  - 66%: text-shadow 1px 3px 8px shadow-md
  - 100%: text-shadow 2px 2px 8px shadow-md

## 雾气飘动

### fogDrift
- 用途: 底部雾气缓慢左右飘移
- duration: 12s
- timing: ease-in-out
- iteration: infinite
- keyframes:
  - 0%: transform translateX(0%) opacity 0.15
  - 50%: transform translateX(3%) opacity 0.2
  - 100%: transform translateX(0%) opacity 0.15

### fogFloat
- 用途: 全屏雾气层缓慢移动
- duration: 20s
- timing: linear
- iteration: infinite
- keyframes:
  - 0%: background-position 0% 50%
  - 50%: background-position 100% 50%
  - 100%: background-position 0% 50%

### fogPulse
- 用途: 雾气浓度起伏
- duration: 8s
- timing: ease-in-out
- iteration: infinite
- keyframes:
  - 0%: opacity 0.1
  - 50%: opacity 0.2
  - 100%: opacity 0.1

## 蔷薇绽放

### roseBloom
- 用途: 蔷薇装饰元素入场
- duration: 2s
- timing: ease-out
- iteration: 1
- keyframes:
  - 0%: transform scale(0) rotate(-45deg) opacity 0
  - 60%: transform scale(1.1) rotate(5deg) opacity 0.8
  - 100%: transform scale(1) rotate(0deg) opacity 1

### rosePetal
- 用途: 花瓣飘落粒子
- duration: 6s
- timing: ease-in
- iteration: 1
- keyframes:
  - 0%: transform translateY(0) rotate(0deg) opacity 0.6
  - 50%: transform translateY(40vh) rotate(180deg) translateX(20px) opacity 0.4
  - 100%: transform translateY(80vh) rotate(360deg) translateX(-10px) opacity 0

### roseWilt
- 用途: 蔷薇枯萎退场
- duration: 1.5s
- timing: ease-in
- iteration: 1
- keyframes:
  - 0%: transform scale(1) opacity 1 filter grayscale(0)
  - 100%: transform scale(0.8) opacity 0 filter grayscale(1)

## 铁链摆动

### chainSwing
- 用途: 悬挂装饰元素轻微摆动
- duration: 4s
- timing: ease-in-out
- iteration: infinite
- transform-origin: top center
- keyframes:
  - 0%: transform rotate(0deg)
  - 25%: transform rotate(1.5deg)
  - 75%: transform rotate(-1.5deg)
  - 100%: transform rotate(0deg)

### chainRattle
- 用途: 铁链抖动 用于 hover 交互
- duration: 0.4s
- timing: ease-in-out
- iteration: 3
- keyframes:
  - 0%: transform translateX(0)
  - 25%: transform translateX(-2px)
  - 75%: transform translateX(2px)
  - 100%: transform translateX(0)

### chainDrop
- 用途: 铁链装饰下垂入场
- duration: 1.2s
- timing: cubic-bezier(0.34, 1.56, 0.64, 1)
- iteration: 1
- keyframes:
  - 0%: transform translateY(-30px) opacity 0
  - 100%: transform translateY(0) opacity 1

## 血滴

### bloodDrip
- 用途: 极少量装饰性血滴粒子 不可过度使用
- duration: 4s
- timing: ease-in
- iteration: 1
- keyframes:
  - 0%: top -10px opacity 1 transform scaleY(1)
  - 20%: top -5px opacity 1 transform scaleY(1.3)
  - 100%: top 100vh opacity 0 transform scaleY(1)

### bloodPool
- 用途: 血滴落地扩散
- duration: 1s
- timing: ease-out
- iteration: 1
- keyframes:
  - 0%: transform scale(0) opacity 0.8
  - 100%: transform scale(1) opacity 0

### bloodPulse
- 用途: 血红元素脉动 用于警告状态
- duration: 2s
- timing: ease-in-out
- iteration: infinite
- keyframes:
  - 0%: box-shadow 0 0 0 0 rgba(var(--accent-primary-rgb), 0.4)
  - 70%: box-shadow 0 0 0 8px rgba(var(--accent-primary-rgb), 0)
  - 100%: box-shadow 0 0 0 0 rgba(var(--accent-primary-rgb), 0)

## 暗影脉动

### shadowPulse
- 用途: 卡片 按钮的幽暗呼吸效果
- duration: 6s
- timing: ease-in-out
- iteration: infinite
- keyframes:
  - 0%: box-shadow 0 0 20px shadow-sm
  - 50%: box-shadow 0 0 40px shadow-md
  - 100%: box-shadow 0 0 20px shadow-sm

### shadowExpand
- 用途: hover 时阴影扩展
- duration: 0.4s
- timing: ease-out
- iteration: 1
- fill-mode: forwards
- keyframes:
  - 0%: box-shadow 0 0 10px shadow-sm
  - 100%: box-shadow 0 0 30px shadow-md 0 0 60px shadow-sm

### darkVeil
- 用途: 遮罩层渐入
- duration: 0.5s
- timing: ease-out
- iteration: 1
- keyframes:
  - 0%: background-color rgba(0,0,0,0) backdrop-filter blur(0px)
  - 100%: background-color rgba(0,0,0,0.92) backdrop-filter blur(4px)

## 入场动画

### fadeRise
- 用途: 元素从下方浮现 通用入场
- duration: 1.5s
- timing: ease-out
- iteration: 1
- keyframes:
  - 0%: opacity 0 transform translateY(20px) filter blur(4px)
  - 100%: opacity 1 transform translateY(0) filter blur(0)

### fadeFromDark
- 用途: 从黑暗中浮现
- duration: 2s
- timing: ease-out
- iteration: 1
- keyframes:
  - 0%: opacity 0 filter brightness(0)
  - 50%: opacity 0.5 filter brightness(0.5)
  - 100%: opacity 1 filter brightness(1)

### gothicReveal
- 用途: 从中心向两侧展开 如打开教堂大门
- duration: 1.8s
- timing: ease-out
- iteration: 1
- keyframes:
  - 0%: clip-path inset(0 50% 0 50%)
  - 100%: clip-path inset(0 0 0 0)

### staggeredRise
- 用途: 列表项依次入场
- duration: 0.8s per item
- timing: ease-out
- stagger-delay: 0.1s
- iteration: 1
- keyframes:
  - 0%: opacity 0 transform translateY(15px)
  - 100%: opacity 1 transform translateY(0)

## Transition 参数

| 用途 | duration | timing |
|------|----------|--------|
| 按钮 hover | 0.3s | ease |
| 链接 hover | 0.3s | ease |
| 卡片 hover | 0.3s | ease |
| 边框变化 | 0.3s | ease |
| 背景变化 | 0.4s | ease |
| 颜色变化 | 0.3s | ease |
| 阴影变化 | 0.4s | ease-out |
| transform | 0.3s | ease-out |
| modal 入场 | 0.5s | ease-out |
| modal 退场 | 0.3s | ease-in |
| 页面切换 | 0.6s | ease-in-out |

## 使用原则

- 所有动画必须极其缓慢微妙 模拟烛火摇曳而非烟花绽放
- 血滴效果极少量使用 每屏最多 1-2 个
- 雾气效果 opacity 不超过 0.2
- 优先使用 transform 和 opacity 实现动画 保证 GPU 加速
- 提供 prefers-reduced-motion 媒体查询 关闭所有非必要动画
- infinite 动画必须足够微妙 不可分散用户注意力
- 入场动画使用 IntersectionObserver 触发 避免页面加载时全部播放
