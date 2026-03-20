# 排版特效体系

## 首字下沉 (Drop Cap)

文章开头段落的首字母放大下沉 是报纸排版的标志性元素

### 首字下沉规范

属性	值
选择器	::first-letter
font-family	Playfair Display, serif
font-size	4.5em
float	left
line-height	0.8
padding-right	10px
padding-top	4px
color	--color-text-bright
font-weight	900

### 变体

小型下沉	font-size: 3em 用于卡片/摘要
装饰下沉	添加背景色块 padding: 8px 12px background: --color-text-bright color: --color-bg
框线下沉	添加 2px solid 边框包裹 padding: 6px 10px

## 多栏布局 (Multi-column)

报纸的灵魂布局 将正文分为多栏并排

### 栏数规范

组件	column-count	column-gap	column-rule
双栏正文	2	40px	1px solid var(--color-border)
三栏布局	3	30px	1px solid var(--color-border)
四栏索引	4	24px	1px solid var(--color-border-dim)

### 响应式回退

断点	行为
max-width 768px	所有多栏回退为 column-count: 1
max-width 1024px	三栏和四栏回退为 column-count: 2

### 栏内控制

属性	值	用途
break-inside	avoid	防止卡片/图片被栏截断
break-after	column	强制换栏
column-span	all	标题横跨所有栏

## 报头横线 (Masthead Rules)

### 横线等级

类型	CSS	用途
细线	height: 1px; background: var(--color-border)	小节分隔
粗线	height: 3px; background: var(--color-text-bright)	大区域分隔/报头底线
双线	border-top: 3px double var(--color-text-bright)	最重要的分隔 报头/版块
装饰短线	width: 60px; height: 1px; margin: 0 auto; background: var(--color-border)	段落间居中装饰
渐隐线	background: linear-gradient(90deg, transparent, var(--color-border), transparent)	柔和分隔

### 报头装饰组合

报头上方	双线
报名下方	细线
日期下方	粗线
版块标题上方	粗线
版块标题下方	细线

## 引用块 (Pullquote)

### 标准引用

属性	值
font-family	Playfair Display, serif
font-size	1.6rem
font-style	italic
color	var(--color-text-bright)
text-align	center
padding	30px 40px
margin	40px 0
border-top	2px solid var(--color-text-bright)
border-bottom	2px solid var(--color-text-bright)
line-height	1.4

### 引用来源

属性	值
font-family	Inter, sans-serif
font-size	0.75rem
font-style	normal
color	var(--color-text-dim)
text-transform	uppercase
letter-spacing	0.1em
margin-top	12px

### 引用变体

侧栏引用	float: right; width: 45%; margin-left: 30px; border-left: 3px solid var(--color-accent); border-top: none; border-bottom: none; text-align: left; padding: 0 0 0 20px
大字引用	font-size: 2.2rem; font-weight: 700; font-style: normal; 无边框 仅靠字号突出

## 脚注 (Footnotes)

### 脚注标记

属性	值
font-size	0.7em
vertical-align	super
color	var(--color-accent)
font-weight	600
cursor	pointer

### 脚注内容

属性	值
font-size	0.8rem
color	var(--color-text-dim)
border-top	1px solid var(--color-border)
padding-top	16px
margin-top	40px
line-height	1.6

## 页码 (Page Number)

属性	值
font-family	Inter, sans-serif
font-size	0.75rem
color	var(--color-text-dim)
text-align	center
padding	20px 0
letter-spacing	0.1em

## 分栏线 (Column Rule)

属性	值
column-rule-style	solid
column-rule-width	1px
column-rule-color	var(--color-border)

### 变体

虚线分栏	column-rule-style: dashed
点线分栏	column-rule-style: dotted

## 纸张纹理 (Paper Texture)

### CSS 纹理实现

背景叠加层使用 ::before 伪元素

属性	值
position	fixed
top	0
left	0
width	100%
height	100%
pointer-events	none
z-index	0
opacity	0.03
background	url() 或 CSS 噪点

### CSS 噪点替代方案

使用 SVG filter turbulence 生成纸张纹理
baseFrequency	0.65
numOctaves	4
type	fractalNoise

### 纸张老化效果

属性	值
边缘暗角	box-shadow: inset 0 0 100px rgba(0,0,0,0.05)
页面轻微暖色	background-blend-mode: multiply 叠加极淡米色

## 印刷对齐网格 (Baseline Grid)

### 基线网格参数

属性	值
基线单位	8px
正文行高	1.8 (即 font-size * 1.8 对齐到 8px 倍数)
标题行高	1.05-1.2 (对齐到基线)
段落间距	基线单位的倍数 通常 16px 或 24px

### 可视化调试网格

background-image	repeating-linear-gradient(to bottom, transparent, transparent 7px, rgba(0,0,0,0.03) 7px, rgba(0,0,0,0.03) 8px)
background-size	100% 8px

## 标签/分类 (Category Labels)

属性	值
font-family	Inter, sans-serif
font-size	0.7rem
font-weight	600
text-transform	uppercase
letter-spacing	0.15em
color	var(--color-accent)

## 署名线 (Byline)

属性	值
font-family	Inter, sans-serif
font-size	0.8rem
color	var(--color-text-dim)
text-transform	uppercase
letter-spacing	0.08em
