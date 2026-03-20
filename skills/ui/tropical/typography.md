# Tropical Paradise Typography

## 字体栈

| 角色 | 字体 | 回退 | 加载权重 |
|------|------|------|----------|
| display | Pacifico | Leckerli One, cursive | 400 |
| heading | Josefin Sans | sans-serif | 600, 700 |
| body | Nunito | Noto Sans SC, sans-serif | 400, 600, 700, 800 |

## 字号体系

| 层级 | 尺寸 | clamp | 字体 |
|------|------|-------|------|
| hero | 4.5rem | clamp(2.5rem, 6vw, 4.5rem) | Pacifico |
| h1 | 2.5rem | clamp(1.8rem, 4vw, 2.5rem) | Pacifico |
| h2 | 1.8rem | clamp(1.3rem, 3vw, 1.8rem) | Josefin Sans |
| h3 | 1.3rem | clamp(1.1rem, 2vw, 1.3rem) | Josefin Sans |
| h4 | 1.1rem | - | Josefin Sans |
| body | 0.95rem | - | Nunito |
| small | 0.85rem | - | Nunito |
| caption | 0.75rem | - | Nunito |
| tag | 0.7rem | - | Josefin Sans |

## 字重

| 用途 | 字重 |
|------|------|
| display 标题 | 400 (Pacifico 自带装饰感) |
| section 标题 | 700 |
| 按钮/标签 | 700 |
| 正文强调 | 600 |
| 正文 | 400 |
| 辅助文字 | 400 |

## 颜色映射

| 用途 | 变量 |
|------|------|
| display 标题 | var(--text-heading) |
| section 标题 | var(--accent-tertiary) |
| 正文 | var(--text-primary) |
| 辅助说明 | var(--text-secondary) |
| 占位/禁用 | var(--text-tertiary) |
| 链接 | var(--text-link) |
| 反色文字 | var(--text-inverse) |

## 行高

| 用途 | 行高 |
|------|------|
| display/hero | 1.2 |
| heading | 1.3 |
| body | 1.7 |
| compact (tag/btn) | 1.0 |

## 间距

| 属性 | 值 |
|------|------|
| letter-spacing (tag) | 0.12em |
| letter-spacing (section title) | 0.1em |
| letter-spacing (body) | normal |
| word-spacing | normal |

## 文字装饰

```css
.text-shadow-soft {
  text-shadow: 2px 3px 0 rgba(0, 0, 0, 0.06);
}

.text-gradient {
  background: linear-gradient(135deg, var(--accent-primary), var(--accent-secondary));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.text-uppercase {
  text-transform: uppercase;
  letter-spacing: 0.1em;
  font-family: var(--font-heading);
}
```

## 圆角体系

| 用途 | 圆角 |
|------|------|
| 按钮 (pill) | 50px |
| 卡片 | 16px |
| Modal | 20px |
| 输入框 | 12px |
| 标签 | 20px |
| 图片 | 12px |
| 小圆角 | 6px |
| 工具提示 | 8px |

## 响应式排版

```css
:root {
  --font-display: "Pacifico", cursive;
  --font-heading: "Josefin Sans", sans-serif;
  --font-body: "Nunito", "Noto Sans SC", sans-serif;
}

.hero-title {
  font-family: var(--font-display);
  font-size: clamp(2.5rem, 6vw, 4.5rem);
  font-weight: 400;
  color: var(--text-heading);
  text-align: center;
  text-shadow: 2px 3px 0 rgba(0, 0, 0, 0.06);
  line-height: 1.2;
}

.section-title {
  font-family: var(--font-heading);
  font-size: clamp(1.3rem, 3vw, 1.8rem);
  font-weight: 700;
  color: var(--accent-tertiary);
  text-transform: uppercase;
  letter-spacing: 0.1em;
  text-align: center;
  line-height: 1.3;
}

.body-text {
  font-family: var(--font-body);
  font-size: 0.95rem;
  font-weight: 400;
  color: var(--text-primary);
  line-height: 1.7;
}

.caption-text {
  font-family: var(--font-body);
  font-size: 0.75rem;
  font-weight: 400;
  color: var(--text-tertiary);
  line-height: 1.5;
}
```
