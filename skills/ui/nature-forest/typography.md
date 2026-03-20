# Nature Forest Typography

## 字体族

| 用途 | 首选 | 备选 | 中文回退 |
|------|------|------|----------|
| 标题 | Playfair Display | Lora | Noto Serif SC |
| 正文 | Source Sans 3 | Nunito | Noto Sans SC |
| 手写装饰 | Caveat | Kalam | - |

## Google Fonts 引入

```
fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Source+Sans+3:wght@300;400;500;600&family=Caveat:wght@400;600&family=Noto+Serif+SC:wght@400;600;700&family=Noto+Sans+SC:wght@300;400;500&display=swap
```

## 标题层级

| 层级 | 字号 | 字重 | 行高 | 间距 | 字体族 |
|------|------|------|------|------|--------|
| h1 | clamp(2rem, 5vw, 3.5rem) | 700 | 1.2 | -0.01em | Playfair Display, Noto Serif SC, serif |
| h2 | clamp(1.5rem, 3.5vw, 2.4rem) | 700 | 1.3 | 0em | Playfair Display, Noto Serif SC, serif |
| h3 | clamp(1.3rem, 3vw, 1.8rem) | 600 | 1.35 | 0.01em | Playfair Display, Noto Serif SC, serif |
| h4 | clamp(1.1rem, 2.5vw, 1.4rem) | 600 | 1.4 | 0.01em | Playfair Display, Noto Serif SC, serif |
| h5 | 1rem | 600 | 1.45 | 0.02em | Source Sans 3, Noto Sans SC, sans-serif |
| h6 | 0.875rem | 600 | 1.5 | 0.03em | Source Sans 3, Noto Sans SC, sans-serif |

## 正文层级

| 变体 | 字号 | 字重 | 行高 | 间距 | 字体族 |
|------|------|------|------|------|--------|
| body-lg | 1.1rem | 400 | 1.8 | 0.02em | Source Sans 3, Noto Sans SC, sans-serif |
| body | 0.95rem | 400 | 1.75 | 0.02em | Source Sans 3, Noto Sans SC, sans-serif |
| body-sm | 0.85rem | 400 | 1.7 | 0.02em | Source Sans 3, Noto Sans SC, sans-serif |
| caption | 0.78rem | 400 | 1.5 | 0.03em | Source Sans 3, Noto Sans SC, sans-serif |
| overline | 0.7rem | 600 | 1.4 | 0.08em | Source Sans 3, Noto Sans SC, sans-serif |

## 手写装饰文字

| 变体 | 字号 | 字重 | 行高 | 旋转 | 字体族 |
|------|------|------|------|------|--------|
| handwritten-lg | 1.5rem | 600 | 1.4 | rotate(-2deg) | Caveat, cursive |
| handwritten | 1.3rem | 400 | 1.4 | rotate(-1.5deg) | Caveat, cursive |
| handwritten-sm | 1.1rem | 400 | 1.3 | rotate(-1deg) | Caveat, cursive |

## 特殊文字样式

### 引用块
- font-family: Playfair Display, Noto Serif SC, serif
- font-size: 1.1rem
- font-style: italic
- font-weight: 400
- line-height: 1.8
- padding-left: 20px
- border-left: 3px solid 强调色 opacity 0.3

### 代码/等宽
- font-family: JetBrains Mono, Fira Code, Cascadia Code, monospace
- font-size: 0.85rem
- font-weight: 400
- line-height: 1.6
- letter-spacing: 0em
- background: rgba(139, 111, 71, 0.06)
- border-radius: 4px
- padding: 2px 6px

### 标签文字
- font-family: Source Sans 3, Noto Sans SC, sans-serif
- font-size: 0.75rem
- font-weight: 600
- letter-spacing: 0.05em
- text-transform: uppercase

## 按钮文字

| 尺寸 | 字号 | 字重 | 间距 | 字体族 |
|------|------|------|------|--------|
| btn-lg | 1rem | 600 | 0.02em | Source Sans 3, Noto Sans SC, sans-serif |
| btn | 0.95rem | 600 | 0.02em | Source Sans 3, Noto Sans SC, sans-serif |
| btn-sm | 0.82rem | 600 | 0.03em | Source Sans 3, Noto Sans SC, sans-serif |

## 输入框文字

- font-family: Source Sans 3, Noto Sans SC, sans-serif
- font-size: 0.95rem
- font-weight: 400
- line-height: 1.5
- letter-spacing: 0.01em

## 圆角规范

| 元素 | border-radius |
|------|---------------|
| 按钮 | 6px |
| 叶形按钮 | 30px 8px 30px 8px |
| 输入框 | 8px |
| 卡片 | 10px |
| Modal | 12px |
| 标签/徽章 | 12px |
| 头像/圆形 | 50% |
| 工具提示 | 6px |
| 代码块 | 8px |