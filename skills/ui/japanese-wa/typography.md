# 和风日式排版规范

## 字体堆栈

```
--font-heading: "Zen Old Mincho", "Noto Serif JP", "Noto Serif SC", serif
--font-body: "Noto Sans JP", "Zen Maru Gothic", "Noto Sans SC", sans-serif
--font-accent: "Cormorant Garamond", serif
--font-mono: "Source Han Mono", "Noto Sans Mono", monospace
```

Google Fonts:
```
Zen+Old+Mincho:wght@400;700
Noto+Sans+JP:wght@300;400;500;700
Cormorant+Garamond:wght@400;600
```

## 字号系统

```
--text-xs: clamp(0.65rem, 0.6rem + 0.25vw, 0.72rem)
--text-sm: clamp(0.78rem, 0.74rem + 0.2vw, 0.84rem)
--text-base: clamp(0.88rem, 0.84rem + 0.2vw, 0.95rem)
--text-md: clamp(1rem, 0.95rem + 0.25vw, 1.1rem)
--text-lg: clamp(1.15rem, 1.08rem + 0.35vw, 1.3rem)
--text-xl: clamp(1.35rem, 1.25rem + 0.5vw, 1.6rem)
--text-2xl: clamp(1.65rem, 1.5rem + 0.75vw, 2rem)
--text-3xl: clamp(2rem, 1.8rem + 1vw, 2.5rem)
--text-4xl: clamp(2.5rem, 2.2rem + 1.5vw, 3.2rem)
--text-5xl: clamp(3rem, 2.6rem + 2vw, 4rem)
```

## 字重

```
--weight-light: 300
--weight-regular: 400
--weight-medium: 500
--weight-bold: 700
```

用途:
- 标题: 700(强) / 400(淡)
- 正文: 400
- 辅助/muted: 300
- 强调: 500

## 文字颜色

```
--text-primary: 主要文字 高对比度
--text-secondary: 次要文字 中等对比度
--text-muted: 辅助文字 低对比度
--text-inverse: 反色文字 用于深色背景
--text-link: 链接色 强调色系
--text-link-hover: 链接悬停色 深一度
```

## 行高

```
--leading-tight: 1.4
--leading-normal: 1.9
--leading-relaxed: 2.2
--leading-loose: 2.6
```

用途:
- 标题: 1.4
- 正文: 1.9
- 长段落: 2.2
- 注释/说明: 2.6

## 字间距

```
--tracking-tight: 0.02em
--tracking-normal: 0.05em
--tracking-wide: 0.1em
--tracking-wider: 0.15em
--tracking-widest: 0.2em
```

用途:
- 英文正文: 0.02em
- 日中文正文: 0.05em
- 按钮/标签: 0.1-0.15em
- 大标题: 0.15-0.2em

## 段落间距

```
--space-paragraph: 1.5em
--space-section: 3em
--space-heading-top: 2.5em
--space-heading-bottom: 1em
```

## 纵向排版

```
writing-mode: vertical-rl
text-orientation: mixed
line-height: 2.2
letter-spacing: 0.1em
overflow-x: auto
overflow-y: hidden
padding: 40px
```

注意:
- 仅用于装饰性标题或短文
- 英文自动旋转(text-orientation: mixed)
- 需预留充足宽度

## 标题装饰

左侧窰线:
```
border-left: 3px solid var(--accent-primary)
padding-left: 16px
```

下方墨线:
```
padding-bottom: 12px
border-bottom: 1px solid var(--border-default)
```

装饰符前缀(::before):
```
content: '◆'
margin-right: 8px
color: var(--accent-primary)
font-size: 0.6em
vertical-align: middle
```

## 引用块

```
border-left: 2px solid var(--accent-secondary)
padding: 16px 24px
margin: 24px 0
background: var(--accent-subtle)
font-family: var(--font-heading)
font-style: normal
line-height: 2.2
letter-spacing: 0.1em
```

## 圆角规范

| 元素 | border-radius |
|------|---------------|
| 按钮 | 2px |
| 卡片 | 0 |
| Modal | 0 |
| 输入框 | 0 |
| 标签/badge | 2px |
| tooltip | 2px |
| 滚动条 | 0 |
| 头像 | 0 |

## 对齐规则

- 正文: 左对齐
- 标题: 左对齐或居中
- 数字/编号: 右对齐或等宽
- 装饰性短句: 居中

## 特殊装饰符号

- 引号: 「」 『』
- 圆点: ● ○
- 菱形: ◆ ◇
- 线条: ━ ▪
- 花: ✿ ❀
- 棋: ☗
