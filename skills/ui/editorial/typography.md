# 排版规范

## 字体栈

用途	字体
英文大标题	Playfair Display, serif
英文副标题	Libre Baskerville, Cormorant Garamond, serif
英文正文	Source Serif 4, Merriweather, serif
英文标签/UI	Inter, DM Sans, sans-serif
中文回退	Noto Serif SC, SimSun, serif
等宽/数据	JetBrains Mono, Courier New, monospace

## 字号层级

层级	大小	字重	颜色变量	letter-spacing
Hero标题	clamp(2.5rem, 7vw, 5rem)	900	--color-text-bright	-0.02em
页面标题 H1	clamp(1.5rem, 3vw, 2.2rem)	700	--color-text-bright	-0.01em
区块标题 H2	1.25rem (20px)	700	--color-text-bright	0
卡片标题 H3	1.1rem (17.6px)	700	--color-text-bright	0
正文	1rem (16px)	400	--color-text	0
标签/分类	0.7rem (11.2px)	600	--color-accent	0.15em
署名/日期	0.8rem (12.8px)	400	--color-text-dim	0.08em
小字/脚注	0.75rem (12px)	400	--color-text-dim	0

## 字重使用

字重	数值	使用场景
Black	900	Hero 标题 首字下沉
Bold	700	页面标题 区块标题 卡片标题
Semibold	600	标签/分类 按钮文字
Regular	400	正文 署名 脚注

## 文字处理

标题使用衬线字体 不使用 text-transform
标签/分类使用无衬线字体 配合 text-transform: uppercase
Hero 标题居中对齐 text-align: center
正文使用 text-align: justify 配合 hyphens: auto 实现两端对齐
所有文字使用 -webkit-font-smoothing: antialiased
标题 letter-spacing 为负值 (-0.02em 至 -0.01em) 收紧字距
标签 letter-spacing 为正值 (0.08em 至 0.15em) 拉开字距

## 行高规范

层级	line-height
Hero标题	1.05
页面标题	1.15
区块标题	1.2
卡片标题	1.3
正文	1.8
标签/分类	1.2
脚注	1.6

## 段首缩进

属性	值
正文段落	text-indent: 2em (除首段外)
首段	text-indent: 0 配合首字下沉
引用段落	text-indent: 0
列表内文字	text-indent: 0

## 多栏排版

属性	值
双栏	column-count: 2; column-gap: 40px
三栏	column-count: 3; column-gap: 30px
四栏	column-count: 4; column-gap: 24px
分栏线	column-rule: 1px solid var(--color-border)

## 间距规范

层级	大小	用途
xs	4px	紧凑元素内间距
sm	8px	标签间距 图标与文字间距
md	16px	卡片内边距 列表项间距
lg	24px	卡片padding 区块间距
xl	32px	页面区块间距
2xl	48px	大区块/section间距
3xl	64px	页面顶部/底部留白

## 圆角规范

组件	border-radius	说明
按钮	0-2px	几乎无圆角 保持方正印刷感
输入框	0	完全方正
卡片	0	无圆角 使用线条分隔
模态框	0	完全方正
标签/徽章	2px	极小圆角
头像/缩略图	0	方形裁切
tooltip	2px	极小圆角

报纸排版风格中所有元素使用极小或零圆角 保持方正的印刷品质感

## 文字颜色层次

层次	变量	用途
最深	--color-text-bright	标题 首字下沉 粗线
标准	--color-text	正文 默认文字
暗淡	--color-text-dim	署名 日期 脚注 占位符
禁用	--color-text-disabled	不可交互文字
强调	--color-accent	分类标签 链接 脚注标记
