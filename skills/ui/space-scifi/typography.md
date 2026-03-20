# 排版规范

## 字体栈

用途	字体	回退
标题	Exo 2	Chakra Petch, Noto Sans SC, sans-serif
正文	Inter	Source Sans 3, Noto Sans SC, sans-serif
数据/HUD	JetBrains Mono	Space Mono, Noto Sans SC, monospace

## 字号层级

层级	大小	字重	颜色	用途
hero	clamp(2.5rem, 6vw, 4.5rem)	800	--color-text-bright	首屏主标题
h1	clamp(1.5rem, 3vw, 2rem)	700	--color-text-bright	页面标题
h2	clamp(1.2rem, 2.5vw, 1.6rem)	700	--color-text-bright	区域标题
h3	1.1rem	600	--color-text-bright	卡片标题/面板标题
body-lg	1rem	400	--color-text	大段正文
body	0.9rem	400	--color-text	默认正文
body-sm	0.85rem	400	--color-text	辅助正文
caption	0.8rem	400	--color-text-dim	说明/备注
label	0.75rem	500	--color-text-dim	表单标签
hud-label	0.7rem	400	--color-holo	HUD角标/数据标签
hud-data	0.65rem	400	--color-holo	HUD微型数据
tiny	0.6rem	400	--color-text-dim	最小文字

## 标题样式

所有标题使用 Exo 2 字体
text-shadow: 0 0 40px rgba(74,168,216,0.15)
line-height: 1.2

## 区域标题 (section-title)

字体: Exo 2
text-transform: uppercase
letter-spacing: 0.15em
可选底部装饰线: 40px宽 2px高 引擎橙色 居中

## HUD标签样式

字体: JetBrains Mono
text-transform: uppercase
letter-spacing: 0.2em
opacity: 0.7
颜色: --color-holo
常用内容: SYSTEM / COMM LINK / DATA PANEL / NAV / STATUS / TELEMETRY

## 数据值样式

字体: JetBrains Mono
颜色: --color-text-bright
font-variant-numeric: tabular-nums
用于: 坐标/数值/计数器/百分比/时间戳

## 行高

标题: 1.2
正文: 1.7
HUD数据: 1.4
按钮: 1

## 字间距

标题: -0.02em
正文: 0
按钮文字: 0.08em
HUD标签: 0.15-0.2em
区域标题: 0.15em

## 圆角规范

组件	圆角
按钮	6px (配合切角使用时可为0)
输入框	8px
卡片	10px
模态框	12px
气泡	12px
HUD角标	3px
芯片/徽章	full (9999px)
头像	50%
tooltip	6px
下拉菜单	8px

## 间距规范

xs	4px
sm	8px
md	12px
lg	16px
xl	24px
2xl	32px
3xl	48px
4xl	64px

卡片内边距: 28px
模态框内边距: 40px
面板间距: 20px
导航栏内边距: 14px 36px
按钮内边距: 14px 36px
输入框内边距: 12px 16px
HUD数据行间距: 8px 0
