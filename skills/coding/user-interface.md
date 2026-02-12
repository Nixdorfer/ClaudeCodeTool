# 用户界面书写规范

## 基本要求

### 页面要求
- 页面禁止使用渐变色
- 极简现代风格 类似苹果的液态玻璃质感
- 英文字体Cascade Code
- 中文字体微软雅黑
- 图标不要使用emoji 使用空心线框单色SVG图标 必要时才使用文字

### 按钮和滑块
- 按钮使用胶囊形状
- 所有checkbox等是否选项都改用滑块替代
- 二选一且必选的选项使用左右滑块替代

### 下拉栏和modal
- 尽可能不显示滚动条 如果放不下则滚动条需要自行实现美化
- 所有modal都有不随滚动条滚动的
  - 顶部header放置标题
  - 底部footer放置按钮
  - 被滚动的文字放在content内
- 下拉栏要做美化 要有卷动的动画

## 详细风格描述

核心视觉风格: 深色液态玻璃科技风
色彩方案纯深色主题
主背景	--color-bg	#050505
表面色	--color-surface	#111111
模态框	--color-modal	#222222
主文字	--color-text	#b7b7b7
暗文字	--color-text-dim	#777777
亮文字	--color-text-bright	#e0e0e0
强调色	--color-accent	#166d3b (深绿)
强调悬停	--color-accent-hover	#1a8548
边框	--color-border	#333333
危险	--color-danger	#dc2626
成功	--color-success	#16a34a
玻璃态 (Liquid Glass) 体系
这是设计的核心特征 所有容器都使用半透明+模糊+光线折射效果:

组件	背景	模糊度	边框
侧边栏	rgba(17,17,17,0.6)	blur(24px) saturate(140%)	rgba(255,255,255,0.06)
顶栏	rgba(17,17,17,0.5)	blur(16px) saturate(130%)	同上
卡片	rgba(255,255,255,0.04)	blur(8px)	rgba(255,255,255,0.08)
输入框	rgba(255,255,255,0.05)	blur(12px) saturate(130%)	rgba(255,255,255,0.1)
按钮	rgba(22,109,59,0.3)	blur(8px)	rgba(22,109,59,0.3)
AI气泡	rgba(255,255,255,0.05)	blur(12px)	rgba(255,255,255,0.08)
用户气泡	rgba(22,109,59,0.35)	blur(12px)	rgba(22,109,59,0.3)
排版规范
层级	大小	字重	颜色
标签/说明	text-xs (12px)	normal	text-text-dim
正文/标签	text-sm (14px)	normal/medium	text-text
标题	text-sm~text-base	font-medium	text-text-bright
间距使用 Tailwind 标准: p-2 p-3 p-4 gap-2 gap-3 space-y-3

圆角规范
组件	圆角
按钮/输入框	rounded-lg (8px)
卡片	rounded-xl (12px)
模态框/气泡	rounded-2xl (16px)
芯片/徽章	rounded-full
动画体系
动画	效果	时长
fade-in	opacity 0→1 + translateY 6px→0	0.25s ease-out
modal-in	opacity + scale(0.95→1) + translateY	0.25s ease-out
dropdown-in	opacity + translateY(4px) + scale(0.96)	0.15s ease-out
bg-drift	背景渐变漂移+缩放+旋转	40s infinite
confirm-pulse	绿色光晕脉冲	2s infinite
状态过渡	transition-colors / transition-all	0.2s ease
动态背景
body::before 使用径向绿色渐变 配合 bg-drift 40秒缓慢漂移动画 系统状态变化时通过 data-status 属性改变色调:

busy → 色相偏移+饱和度增强
error → 红色化+亮度增强
滚动条
细窄6px宽 透明轨道 rgba(255,255,255,0.1) 圆角滑块

关键设计原则总结
极暗背景 (#050505) 配合液态玻璃组件
绿色 作为唯一强调色贯穿交互元素
低对比度 灰色文字层次 (dim → normal → bright)
统一模糊 所有容器使用 backdrop-filter blur
微妙边框 使用 rgba(255,255,255, 0.06~0.1) 白色极淡边框
流畅动画 所有交互 0.15-0.25s 过渡 背景持续漂移
无第三方依赖 全部样式基于 Tailwind 原子类 + 自定义 CSS 类

# 参考配色方案

## 亮色 白底蓝白配色

- 背景色 #f5f7fa
- modal色 #ffffff
- 按钮色 #4a69bd
- 文字色 #1a1a2e

## 亮色 蓝底蓝白配色

- 背景色 #1a1a2e
- modal色 #f5f7fa
- 按钮色 #4a69bd
- 文字色 #1a1a2e

## 暗色 黑绿配色

- 背景色 #050505
- modal色 #222222
- 按钮色 #166d3b
- 文字色 #b7b7b7

## 暗色 灰彩配色

- 背景色 #282c34
- modal色 #5a6374
- 按钮色 #98c379 #e06c75 #56b6c2 #e5c07b
- 文字色 #dcdfe4

## 暗色 灰橘配色

- 背景色 #262626
- modal色 #30302e
- 按钮色 #c6613f
- 文字色 #9c9a92