# 动画体系

## 霓虹闪烁 (Neon Flicker)

动画名	neonFlicker
时长	4s
循环	infinite
时序函数	steps(1)

### 关键帧

0%	text-shadow: 0 0 10px var(--accent), 0 0 20px var(--accent), 0 0 40px var(--accent)
19%	同上
20%	text-shadow: none
21%	text-shadow: 0 0 10px var(--accent), 0 0 20px var(--accent), 0 0 40px var(--accent)
23%	同上
24%	text-shadow: none
25%	text-shadow: 0 0 10px var(--accent), 0 0 20px var(--accent), 0 0 40px var(--accent)
54%	同上
55%	text-shadow: none
56%	text-shadow: 0 0 10px var(--accent), 0 0 20px var(--accent), 0 0 40px var(--accent)
100%	同上

### 变体

轻微闪烁	opacity 在 0.9 和 1.0 之间切换 时长 3s 用于次要元素
快速闪烁	时长 0.5s 用于故障/错误状态下的短暂闪烁
呼吸闪烁	opacity 在 0.6 和 1.0 之间 ease-in-out 时长 2s 用于待机/空闲指示

## 故障抖动 (Glitch Shake)

动画名	glitchShake
时长	3s
循环	infinite
时序函数	linear

### 关键帧

0%	transform: translate(0, 0)
2%	transform: translate(-2px, 1px)
4%	transform: translate(2px, -1px)
6%	transform: translate(-1px, -2px)
8%	transform: translate(1px, 2px)
10%	transform: translate(0, 0)
100%	transform: translate(0, 0)

10% 到 100% 保持静止 实现间歇性故障效果

### 色彩偏移故障

动画名	glitchColorShift
时长	2.5s
循环	infinite

::before 关键帧
0%	clip-path: inset(0 0 85% 0); transform: translate(-3px, 0)
15%	clip-path: inset(15% 0 65% 0); transform: translate(3px, 0)
30%	clip-path: inset(50% 0 20% 0); transform: translate(-2px, 0)
45%	clip-path: inset(70% 0 5% 0); transform: translate(2px, 0)
60%	clip-path: inset(10% 0 70% 0); transform: translate(-1px, 0)
75%	clip-path: inset(40% 0 30% 0); transform: translate(1px, 0)
100%	clip-path: inset(0 0 85% 0); transform: translate(-3px, 0)

::after 使用相同结构但反向偏移和不同裁剪区域

## 扫描线移动 (Scanline Sweep)

动画名	scanlineSweep
时长	8s
循环	infinite
时序函数	linear

### 关键帧

0%	background-position: 0 -100%
100%	background-position: 0 100%

使用一条水平半透明亮线从上到下循环扫过容器
background: linear-gradient(to bottom, transparent 49%, rgba(var(--accent-rgb), 0.08) 50%, transparent 51%)
background-size: 100% 200%

### CRT 扫描线

动画名	crtScanline
时长	10s
循环	infinite
叠加一条更亮的单线从上缓慢移到下 高度 2px
background: linear-gradient(transparent, transparent 49.5%, rgba(var(--accent-rgb), 0.15) 50%, transparent 50.5%, transparent)

## 打字机效果 (Typewriter)

动画名	typewriter
时长	根据字符数动态计算 每字符 50-80ms
循环	once
时序函数	steps(字符数)

### 实现方式

width 从 0 到 100%
overflow: hidden
white-space: nowrap
border-right: 2px solid var(--color-accent) 作为光标

### 光标闪烁

动画名	cursorBlink
时长	0.8s
循环	infinite
时序函数	steps(1)

0%	border-right-color: var(--color-accent)
50%	border-right-color: transparent
100%	border-right-color: var(--color-accent)

## 数据流 (Data Rain)

动画名	dataRain
时长	每列随机 2s 到 5s
循环	infinite
时序函数	linear

### 关键帧

0%	transform: translateY(-100%); opacity: 1
70%	opacity: 1
100%	transform: translateY(100vh); opacity: 0

字符使用主强调色 尾部渐变为透明
字符集 01 或 0123456789ABCDEF 或片假名
每列随机 animation-delay 范围 0s 到 5s
字体 Share Tech Mono 字号 14px

## 水平光扫 (Light Sweep)

动画名	lightSweep
时长	3s
循环	infinite
时序函数	ease-in-out

### 关键帧

0%	transform: translateX(-100%)
100%	transform: translateX(200%)

应用于容器顶部 2px 装饰线
使用 overflow: hidden 限制在容器内
background: linear-gradient(90deg, transparent 0%, var(--color-accent) 50%, transparent 100%)
width: 50%

## 脉冲光晕 (Pulse Glow)

动画名	pulseGlow
时长	2s
循环	infinite
时序函数	ease-in-out

### 关键帧

0%	box-shadow: 0 0 5px rgba(var(--accent-rgb), 0.2)
50%	box-shadow: 0 0 20px rgba(var(--accent-rgb), 0.4), 0 0 40px rgba(var(--accent-rgb), 0.15)
100%	box-shadow: 0 0 5px rgba(var(--accent-rgb), 0.2)

用于焦点元素 在线状态指示 加载状态

## 状态过渡 (State Transitions)

交互类型	属性	时长	时序函数
按钮悬停	all	0.3s	ease
链接悬停	color, text-shadow	0.3s	ease
卡片悬停	border-color, box-shadow, transform	0.3s	ease
输入框聚焦	border-color, box-shadow, background	0.3s	ease
导航下划线	width	0.3s	ease
关闭按钮	text-shadow	0.3s	ease

## 进入动画

动画名	时长	效果
fadeIn	0.3s ease-out	opacity 0 -> 1
slideInUp	0.3s ease-out	opacity 0 -> 1, translateY(20px) -> 0
slideInLeft	0.3s ease-out	opacity 0 -> 1, translateX(-20px) -> 0
scaleIn	0.25s ease-out	opacity 0 -> 1, scale(0.95) -> 1
modalIn	0.3s ease-out	opacity 0 -> 1, scale(0.9) -> 1, translateY(20px) -> 0
dropdownIn	0.15s ease-out	opacity 0 -> 1, translateY(4px) -> 0, scale(0.96) -> 1
glitchIn	0.4s steps(8)	随机 clip-path inset + translate 抖动后归位

## 背景动画

### 网格呼吸

动画名	gridBreath
时长	20s
循环	infinite
时序函数	ease-in-out

背景网格线透明度在 0.02 和 0.05 之间缓慢变化

### 渐变漂移

动画名	bgDrift
时长	30s
循环	infinite
时序函数	ease-in-out

背景从深蓝黑 (主色) 到深紫黑 (辅色) 缓慢渐变漂移

## 动画性能原则

只使用 transform 和 opacity 做动画 避免触发重排
所有装饰性动画添加 prefers-reduced-motion 媒体查询回退
GPU 加速使用 will-change: transform 或 translateZ(0)
故障效果频率不能过高 主体内容 10% 时间抖动 90% 时间静止
