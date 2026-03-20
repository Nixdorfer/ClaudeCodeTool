# Dark Gothic Typography

## 字体栈

### 标题字体 (Gothic Display)
- font-family: "UnifrakturMaguntia", "IM Fell English SC", cursive
- 用途: hero-title h1 品牌名 大装饰标题
- 仅用于展示性大标题 禁止用于正文

### 副标题字体 (Inscription)
- font-family: "Cinzel", "Cinzel Decorative", serif
- 用途: section-title h2 h3 按钮文字 导航链接 标签
- text-transform: uppercase
- letter-spacing: 0.1em - 0.2em

### 正文字体 (Body Serif)
- font-family: "EB Garamond", "Cormorant Garamond", "Noto Serif SC", "SimSun", serif
- 用途: 段落 列表 表单标签 描述文字 正文内容

### 等宽字体 (Code)
- font-family: "Fira Code", "JetBrains Mono", "Cascadia Code", monospace
- 用途: 代码块 技术标签 数据展示

## 字号层级

### 桌面端
| 层级 | 字号 | 用途 |
|------|------|------|
| display-xl | clamp(3rem, 7vw, 6rem) | 首屏主标题 |
| display-lg | clamp(2.5rem, 6vw, 5rem) | hero 标题 |
| display-md | clamp(2rem, 4vw, 3.5rem) | 页面标题 |
| h1 | clamp(1.6rem, 3vw, 2.4rem) | 章节主标题 |
| h2 | clamp(1.2rem, 2.5vw, 1.8rem) | 章节副标题 |
| h3 | clamp(1rem, 2vw, 1.4rem) | 小节标题 |
| h4 | clamp(0.9rem, 1.5vw, 1.1rem) | 卡片标题 |
| body-lg | 1.125rem | 引言/重点段落 |
| body | 1rem | 正文 |
| body-sm | 0.875rem | 辅助文字 |
| caption | 0.75rem | 标注/时间戳 |
| overline | 0.7rem | 上标标签 |

## 字重

| 用途 | 字重 |
|------|------|
| 花体标题 (UnifrakturMaguntia) | 400 (该字体仅单一字重) |
| 碑文标题 (Cinzel) | 600 - 700 |
| 碑文按钮 (Cinzel) | 500 |
| 正文强调 | 600 |
| 正文普通 | 400 |
| 正文轻量 | 300 |

## 颜色分配

| 元素 | 变量 |
|------|------|
| 花体标题 | var(--text-heading) |
| 碑文标题 | var(--accent-primary) 或 var(--text-heading) |
| 正文 | var(--text-primary) |
| 辅助文字 | var(--text-secondary) |
| 禁用/占位 | var(--text-tertiary) |
| 链接 | var(--accent-primary) |
| 链接 hover | var(--accent-hover) |
| 强调关键词 | var(--text-accent) |

## 间距

### 行高
| 用途 | line-height |
|------|-------------|
| 花体标题 | 1.2 |
| 碑文标题 | 1.3 |
| h1-h4 | 1.4 |
| 正文 | 1.8 |
| 紧凑文字 (标签/按钮) | 1.2 |

### 字间距
| 用途 | letter-spacing |
|------|----------------|
| 花体标题 | 0.03em |
| 碑文标题 | 0.15em - 0.2em |
| 导航链接 | 0.1em |
| 按钮 | 0.15em |
| 正文 | 0 (默认) |
| 上标标签 | 0.2em |

### 段落间距
- 段落 margin-bottom: 1.5em
- 标题上方 margin-top: 2.5em
- 标题下方 margin-bottom: 1em
- 列表项间距: 0.5em

## 圆角

全局圆角策略: 0px

哥特风格拒绝圆润感 所有元素使用直角 需要特殊造型时使用 clip-path 而非 border-radius

| 元素 | border-radius | 替代方案 |
|------|---------------|----------|
| 按钮 | 0px | clip-path 尖拱/菱形 |
| 卡片 | 0px | 直角 |
| 输入框 | 0px | 直角 |
| Modal | 0px | clip-path 尖拱顶部 |
| 头像 | 0px | clip-path 八边形 |
| 徽章/标签 | 0px | clip-path 菱形或直角 |
| 滚动条 thumb | 0px | 直角 |
| 工具提示 | 0px | 直角 |

## 文字装饰

### 标题 text-shadow
- 花体标题: 0 2px 10px rgba(var(--accent-primary-rgb), 0.3)
- 碑文标题: 0 1px 6px rgba(var(--accent-primary-rgb), 0.2)
- 烛火效果: 0 0 10px rgba(var(--accent-primary-rgb), 0.3), 0 0 30px rgba(var(--accent-primary-rgb), 0.15)

### 装饰横线标题
- 伪元素 ::before ::after
- content: "✦" margin: 0 15px font-size: 0.6em vertical-align: middle
- color: var(--accent-primary)

### 首字下沉
- .drop-cap::first-letter
- font-family: "UnifrakturMaguntia", cursive
- font-size: 3.5em
- float: left
- line-height: 0.8
- margin: 0 8px 0 0
- color: var(--accent-primary)

## Google Fonts 导入

https://fonts.googleapis.com/css2?family=UnifrakturMaguntia&family=Cinzel:wght@400;500;600;700&family=Cinzel+Decorative:wght@400;700&family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,400&family=IM+Fell+English+SC&family=Noto+Serif+SC:wght@300;400;600&display=swap
