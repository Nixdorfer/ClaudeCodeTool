# Steampunk Typography

## 字体栈

| 用途 | 字体栈 |
|------|--------|
| 展示标题 | "Cinzel Decorative", "Playfair Display", "Noto Serif SC", serif |
| 章节标题 | "Playfair Display", "Noto Serif SC", "SimSun", serif |
| 正文 | "Crimson Text", "EB Garamond", "Noto Serif SC", "SimSun", serif |
| 等宽/仪表 | "Special Elite", "Courier New", monospace |
| 数字标注 | "Special Elite", monospace |

## 字号层级

| 级别 | 字号 | 响应式 |
|------|------|--------|
| display | 3rem / 48px | clamp(2rem, 5vw, 4rem) |
| h1 | 2.25rem / 36px | clamp(1.75rem, 4vw, 2.5rem) |
| h2 | 1.75rem / 28px | clamp(1.375rem, 3vw, 2rem) |
| h3 | 1.375rem / 22px | clamp(1.125rem, 2.5vw, 1.5rem) |
| h4 | 1.125rem / 18px | clamp(1rem, 2vw, 1.25rem) |
| body-lg | 1.125rem / 18px | - |
| body | 1rem / 16px | - |
| body-sm | 0.875rem / 14px | - |
| caption | 0.75rem / 12px | - |
| overline | 0.7rem / 11.2px | - |

## 字重

| 用途 | 字重 |
|------|------|
| 展示标题 | 900 (Black) |
| 主标题 | 700 (Bold) |
| 章节标题 | 600 (SemiBold) |
| 正文强调 | 600 (SemiBold) |
| 正文 | 400 (Regular) |
| 辅助文字 | 400 (Regular) |
| 按钮文字 | 700 (Bold) |
| 标签文字 | 600 (SemiBold) |

## 字间距

| 用途 | letter-spacing |
|------|---------------|
| 展示标题 | 0.08em |
| 主标题 | 0.05em |
| 章节标题 | 0.04em |
| 正文 | 0.02em |
| 按钮 / 大写文字 | 0.12em |
| overline | 0.15em |
| 等宽文字 | 0em |

## 行高

| 用途 | line-height |
|------|-------------|
| 标题 | 1.2 |
| 副标题 | 1.3 |
| 正文 | 1.65 |
| 紧凑文字 | 1.4 |
| 单行 (按钮/标签) | 1 |

## 文字颜色

| 用途 | 颜色 |
|------|------|
| 展示标题 | rgba(219, 184, 80, 1) |
| 主标题 | rgba(219, 184, 80, 1) |
| 章节标题 | rgba(200, 160, 50, 1) |
| 正文 | rgba(212, 197, 160, 1) |
| 次要文字 | rgba(212, 197, 160, 0.7) |
| 禁用文字 | rgba(212, 197, 160, 0.35) |
| 链接 | rgba(184, 115, 51, 1) |
| 链接悬浮 | rgba(200, 160, 50, 1) |
| 反色文字 (亮底按钮) | rgba(26, 18, 9, 1) |
| 代码文字 | rgba(200, 160, 50, 0.9) |
| 占位符 | rgba(212, 197, 160, 0.4) |

## 标题文字阴影

展示标题:
```
text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.6), 0 0 15px rgba(200, 160, 50, 0.2);
```

章节标题:
```
text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.5);
```

## 段落间距

段落间距: 1.25em
列表项间距: 0.5em
标题下方间距: 0.75em
章节间距: 2.5em

## 文字装饰

大写样式 (按钮/overline):
```
text-transform: uppercase;
letter-spacing: 0.12em;
font-weight: 700;
```

引用样式:
```css
blockquote {
  font-family: "Crimson Text", serif;
  font-style: italic;
  font-size: 1.125rem;
  color: rgba(212, 197, 160, 0.85);
  border-left: 3px solid rgba(200, 160, 50, 0.5);
  padding-left: 20px;
  margin: 24px 0;
}
```

代码样式:
```css
code {
  font-family: "Special Elite", "Courier New", monospace;
  font-size: 0.9em;
  color: rgba(200, 160, 50, 0.9);
  background: rgba(42, 31, 14, 0.6);
  padding: 2px 8px;
  border-radius: 3px;
  border: 1px solid rgba(184, 115, 51, 0.25);
}
```

标签/徽章样式:
```css
.tag {
  font-family: "Cinzel Decorative", serif;
  font-size: 0.7rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  padding: 4px 12px;
  border: 1px solid rgba(200, 160, 50, 0.4);
  border-radius: 2px;
  color: rgba(200, 160, 50, 0.9);
}
```

## 圆角参考

标签/徽章: 2px
代码内联: 3px
按钮/输入框: 4px
卡片/Modal: 6px
