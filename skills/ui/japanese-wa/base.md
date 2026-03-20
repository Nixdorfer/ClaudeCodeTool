# 和风日式基础规范

## 核心美学

侘寂(わびさび)之美 在不完美中寻找完美 在朴素中感受深远
间(Ma)的运用 大量留白是无声的表达
枯山水 障子 和纸 墨绘水彩 浮世绘配色

## 页面

```
background: var(--bg-primary)
min-height: 100vh
line-height: 1.9
letter-spacing: 0.05em
overflow-x: hidden
```

和纸纹理叠加层(::before):
```
position: fixed
inset: 0
background-image: url("data:image/svg+xml,%3Csvg width='100' height='100' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence baseFrequency='0.9' numOctaves='5' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.03'/%3E%3C/svg%3E")
pointer-events: none
z-index: 0
```

## 字体

标题: "Zen Old Mincho", "Noto Serif JP", "Noto Serif SC", serif
正文: "Noto Sans JP", "Zen Maru Gothic", "Noto Sans SC", sans-serif
英数: "Cormorant Garamond", serif
等宽: "Source Han Mono", "Noto Sans Mono", monospace

Google Fonts 加载:
```
Zen+Old+Mincho:wght@400;700
Noto+Sans+JP:wght@300;400;500;700
Cormorant+Garamond:wght@400;600
```

## 图标

风格: 和风线描 细线(stroke-width: 1.2-1.5) 无填充
圆角: 0-2px 保持直线锐利感
尺寸: 16px / 20px / 24px / 32px
颜色: 继承文字色 强调态使用 var(--accent-primary)
推荐图标集: Tabler Icons(线描风) 或自绘 SVG
装饰符号: 「」 ● ○ ◆ ◇ ━ ▪ ☗ ✿

## 按钮

主按钮:
```
background: var(--glass-button-default-bg)
color: var(--glass-button-default-text)
border: none
padding: 12px 40px
font-family: var(--font-body)
font-size: 0.9rem
letter-spacing: 0.15em
border-radius: 2px
transition: all 0.3s ease
cursor: pointer
```

主按钮 hover:
```
background: var(--glass-button-hover-bg)
box-shadow: var(--shadow-medium)
```

主按钮 active:
```
background: var(--glass-button-active-bg)
transform: translateY(1px)
```

主按钮 disabled:
```
background: var(--glass-button-disabled-bg)
color: var(--glass-button-disabled-text)
cursor: not-allowed
opacity: 0.6
```

次要按钮:
```
background: transparent
color: var(--text-primary)
border: 1px solid var(--border-default)
padding: 12px 40px
font-size: 0.9rem
letter-spacing: 0.1em
border-radius: 2px
transition: all 0.3s ease
```

次要按钮 hover:
```
background: var(--glass-bg)
```

## Modal(障子窗框)

遮罩层:
```
position: fixed
inset: 0
background: rgba(51, 51, 51, 0.3)
backdrop-filter: blur(4px)
z-index: 1000
display: flex
align-items: center
justify-content: center
```

内容框:
```
background: var(--bg-primary)
padding: 48px 40px
max-width: 460px
width: 90%
border-top: 3px solid var(--accent-primary)
box-shadow: var(--shadow-heavy)
border-radius: 0
```

障子格窗装饰(可选 ::after):
```
content: ''
position: absolute
inset: 8px
border: 1px solid var(--border-subtle)
pointer-events: none
background: repeating-linear-gradient(
  90deg,
  transparent,
  transparent calc(33.33% - 0.5px),
  var(--border-subtle) calc(33.33% - 0.5px),
  var(--border-subtle) calc(33.33% + 0.5px),
  transparent calc(33.33% + 0.5px)
)
opacity: 0.3
```

关闭按钮:
```
position: absolute
top: 16px
right: 16px
color: var(--text-muted)
font-size: 1.2rem
background: none
border: none
cursor: pointer
transition: color 0.3s
```

关闭按钮 hover:
```
color: var(--accent-primary)
```

## 滚动条

```
width: 4px (纵向) / height: 4px (横向)
track-background: var(--scrollbar-track)
thumb-background: var(--scrollbar-thumb)
thumb-hover: var(--scrollbar-hover)
thumb-border-radius: 0
```

## 卡片

```
background: var(--bg-card)
padding: 32px
border-left: 3px solid var(--accent-primary)
box-shadow: var(--shadow-light)
border-radius: 0
transition: all 0.3s ease
```

hover:
```
box-shadow: var(--shadow-medium)
transform: translateY(-2px)
```

## 输入框

```
background: var(--input-bg)
border: none
border-bottom: 1px solid var(--input-border)
color: var(--input-text)
padding: 10px 4px
font-family: var(--font-body)
font-size: 0.95rem
width: 100%
outline: none
transition: border-color 0.3s
border-radius: 0
```

focus:
```
border-bottom-color: var(--input-focus-border)
border-bottom-width: 2px
```

label:
```
font-size: 0.8rem
color: var(--text-muted)
letter-spacing: 0.1em
margin-bottom: 4px
display: block
```

## 分隔线

枯山水砂纹:
```
margin: 60px auto
border: none
text-align: center
```

::before:
```
content: ''
display: block
width: 80%
max-width: 300px
height: 12px
margin: 0 auto
background: repeating-linear-gradient(
  0deg,
  transparent,
  transparent 3px,
  var(--border-subtle) 3px,
  var(--border-subtle) 4px
)
border-radius: 50%
```

## 导航栏

```
position: fixed
top: 0
width: 100%
padding: 16px 40px
background: var(--glass-nav-bg)
backdrop-filter: blur(10px)
border-bottom: 1px solid var(--border-subtle)
display: flex
justify-content: space-between
align-items: center
z-index: 100
```

## 设计约束

- 直角或极小圆角(0-2px) 避免大圆角
- 边框极少使用 区分区域靠留白和微弱阴影
- 配色极度克制 强调色仅用于点睛
- 字间距加大(0.1-0.2em) 体现印刷美感
- 留白充足 元素间距宽松(24-60px)
- 装饰极简 一笔一划蕴含禅意
