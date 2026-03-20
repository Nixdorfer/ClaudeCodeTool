# 动画体系

报纸排版风格几乎不使用动画 保持印刷品的静态质感 仅有极少量克制的过渡效果

## 滚动淡入 (Fade In)

动画名	fadeIn
时长	0.5s
循环	once
时序函数	ease

### 关键帧

0%	opacity: 0; transform: translateY(10px)
100%	opacity: 1; transform: translateY(0)

用于文章区块在滚动进入视口时的渐显效果
位移量极小 (10px) 保持沉稳感 不使用弹性或夸张位移

## 翻页效果 (Page Turn)

动画名	pageTurn
时长	0.6s
循环	once
时序函数	ease-in-out

### 关键帧

0%	opacity: 0; transform: rotateY(-5deg); transform-origin: left center
100%	opacity: 1; transform: rotateY(0deg); transform-origin: left center

用于页面/视图切换 模拟纸张翻动
旋转角度极小 (5deg) 仅产生微弱的翻动暗示

## 下划线展开 (Underline Expand)

动画名	underlineExpand
时长	0.3s
循环	once
时序函数	ease

### 实现方式

使用 ::after 伪元素作为下划线
position: absolute; bottom: -2px; left: 0
width 从 0 到 100% 过渡
height: 1px
background: var(--color-accent)

用于导航链接和文字链接的悬停效果
从左到右展开 不使用居中展开

## 图片渐显 (Image Reveal)

动画名	imageReveal
时长	0.8s
循环	once
时序函数	ease-out

### 关键帧

0%	opacity: 0; filter: grayscale(100%) contrast(1.2)
60%	opacity: 1; filter: grayscale(50%) contrast(1.1)
100%	opacity: 1; filter: grayscale(0%) contrast(1)

用于图片加载完成后的渐显 先以灰度高对比出现再恢复彩色
模拟报纸黑白照片到杂志彩色的过渡

## 状态过渡 (State Transitions)

交互类型	属性	时长	时序函数
按钮悬停	background, color	0.2s	ease
链接悬停	color	0.2s	ease
卡片标题悬停	color	0.2s	ease
输入框聚焦	border-color	0.2s	ease
关闭按钮悬停	color	0.2s	ease
下划线展开	width	0.3s	ease

所有过渡时长不超过 0.3s 保持干脆利落

## 进入动画

动画名	时长	效果
fadeIn	0.5s ease	opacity 0 -> 1, translateY(10px) -> 0
modalIn	0.3s ease	opacity 0 -> 1, translateY(15px) -> 0
dropdownIn	0.15s ease-out	opacity 0 -> 1, translateY(4px) -> 0

模态框和下拉菜单的进入动画幅度极小 不使用缩放效果

## 退出动画

动画名	时长	效果
fadeOut	0.3s ease	opacity 1 -> 0
modalOut	0.2s ease	opacity 1 -> 0, translateY(10px)
dropdownOut	0.1s ease-in	opacity 1 -> 0, translateY(2px)

退出动画时长短于进入动画 保持响应感

## 动画性能原则

只使用 transform 和 opacity 做动画 避免触发重排
所有动画添加 prefers-reduced-motion 媒体查询 减弱运动时直接显示无动画
禁止使用弹跳/回弹/震动等夸张效果
禁止使用循环动画 (loading spinner 除外)
禁止使用 3D 变换 (翻页效果中的 rotateY 是唯一例外且角度极小)
整体动画哲学: 印刷品不会动 动画只是从无到有的过渡辅助
