# 赛博朋克特效体系

## 切角 (Clip-path)

所有容器和交互元素使用切角替代圆角 切角是赛博朋克风格的核心视觉元素

### 切角规范

组件	clip-path	切角尺寸
小按钮	polygon(6px 0, 100% 0, calc(100% - 6px) 100%, 0 100%)	6px
大按钮	polygon(10px 0, 100% 0, calc(100% - 10px) 100%, 0 100%)	10px
卡片	polygon(0 0, calc(100% - 15px) 0, 100% 15px, 100% 100%, 15px 100%, 0 calc(100% - 15px))	15px
模态框	polygon(0 0, calc(100% - 20px) 0, 100% 20px, 100% 100%, 20px 100%, 0 calc(100% - 20px))	20px
输入框	polygon(4px 0, 100% 0, calc(100% - 4px) 100%, 0 100%)	4px
徽章/标签	polygon(4px 0, 100% 0, calc(100% - 4px) 100%, 0 100%)	4px
tooltip	polygon(0 0, calc(100% - 8px) 0, 100% 8px, 100% 100%, 8px 100%, 0 calc(100% - 8px))	8px

### 四角切角公式 (六边形)
polygon(0 0, calc(100% - SIZE) 0, 100% SIZE, 100% 100%, SIZE 100%, 0 calc(100% - SIZE))

### 平行四边形切角公式 (按钮)
polygon(SIZE 0, 100% 0, calc(100% - SIZE) 100%, 0 100%)

## 霓虹发光 (Neon Glow)

### text-shadow 发光参数

层级	text-shadow 值	用途
微发光	0 0 8px var(--color-accent)	导航链接悬停
标准发光	0 0 10px var(--color-accent), 0 0 20px var(--color-accent)	标题文字
强发光	0 0 10px var(--color-accent), 0 0 20px var(--color-accent), 0 0 40px var(--color-accent)	主标题/Hero
极强发光	0 0 10px var(--color-accent), 0 0 20px var(--color-accent), 0 0 40px var(--color-accent), 0 0 80px rgba(var(--accent-rgb), 0.33)	特殊强调

### box-shadow 发光参数

层级	box-shadow 值	用途
微发光	0 0 8px rgba(var(--accent-rgb), 0.2)	卡片默认
标准发光	0 0 15px rgba(var(--accent-rgb), 0.3)	卡片悬停
强发光	0 0 15px rgba(var(--accent-rgb), 0.5), inset 0 0 15px rgba(var(--accent-rgb), 0.1)	按钮悬停
极强发光	0 0 30px rgba(var(--accent-rgb), 0.5), 0 0 60px rgba(var(--accent-rgb), 0.2)	模态框/焦点元素

### 边框发光

1px solid var(--color-accent) 配合 box-shadow 实现发光边框效果
聚焦态边框使用 0 0 10px rgba(var(--accent-rgb), 0.3) 增强

## 故障艺术 (Glitch)

### 基础故障位移

属性	值
伪元素	::before 和 ::after 使用 content: attr(data-text)
定位	position: absolute top: 0 left: 0 width: 100% height: 100%
::before clip-path	inset(0 0 60% 0) 裁剪上部 40%
::after clip-path	inset(60% 0 0 0) 裁剪下部 40%
::before 颜色	副强调色 (霓虹粉)
::after 颜色	主强调色 (霓虹青)

### 故障色彩偏移

通过 ::before 和 ::after 各自偏移不同方向 造成 RGB 色差效果
::before transform: translate(-2px, 0) 左偏移
::after transform: translate(2px, 0) 右偏移

### 随机裁剪故障

使用 clip-path: inset() 在动画关键帧中随机变化裁剪区域
clip-path: inset(20% 0 60% 0) -> inset(50% 0 10% 0) -> inset(5% 0 80% 0)

## 扫描线 (Scanlines)

### 叠加扫描线

选择器	使用 ::after 伪元素叠加在页面或容器上
position	fixed (全页面) 或 absolute (容器内)
background	repeating-linear-gradient(0deg, transparent, transparent 2px, rgba(0,0,0,0.08) 2px, rgba(0,0,0,0.08) 4px)
pointer-events	none
z-index	9999 (全页面) 或适当层级 (容器内)
opacity	0.5 到 1.0 根据需要调整

### 扫描线密度变体

稀疏	transparent 4px / rgba 4px 到 8px	CRT 效果
标准	transparent 2px / rgba 2px 到 4px	默认
密集	transparent 1px / rgba 1px 到 2px	高清屏效果

## 网格背景 (Circuit Grid)

background-color	var(--color-bg)
background-image	linear-gradient(rgba(var(--accent-rgb), 0.03) 1px, transparent 1px), linear-gradient(90deg, rgba(var(--accent-rgb), 0.03) 1px, transparent 1px)
background-size	50px 50px

### 网格变体

细密网格	background-size: 25px 25px	密集电路板
大网格	background-size: 80px 80px	空间感
点阵	radial-gradient(circle, rgba(var(--accent-rgb), 0.06) 1px, transparent 1px) background-size: 20px 20px	矩阵点

## 数据流 (Data Stream)

### 垂直数据雨

使用多个伪元素或 span 模拟从上到下的字符流
字符集 0123456789ABCDEF 或日文片假名
字体 Share Tech Mono 等宽
颜色从主强调色到透明的渐变
每列随机延迟和速度

### 水平数据条

使用 linear-gradient 从左到右扫过的光条效果
width: 100% height: 1-2px
background: linear-gradient(90deg, transparent, var(--color-accent), transparent)
配合 translateX 动画从左扫到右

## 全息投影 (Hologram)

### 全息色彩偏移

使用 mix-blend-mode: screen 叠加 RGB 通道偏移
红通道偏移 (-2px, 0)
蓝通道偏移 (2px, 0)
绿通道保持原位

### 全息闪烁

opacity 在 0.85 到 1.0 之间随机跳动
配合细微的 brightness 和 contrast 变化

## 顶部发光线 (Top Glow Line)

卡片和容器顶部添加装饰发光线

position	absolute top: 0 left: 0
width	100%
height	2px
background	linear-gradient(90deg, transparent, var(--color-accent), transparent)

### 变体

双色渐变线	linear-gradient(90deg, transparent, var(--color-accent), var(--color-accent-secondary), transparent)
脉冲线	配合 opacity 动画产生呼吸效果
扫描线	配合 translateX 动画从左到右循环移动
