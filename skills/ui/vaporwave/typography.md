# Vaporwave Typography

## 字体栈

| 用途 | 字体 | 回退 |
|------|------|------|
| 标题 | Monoton | Bungee Shade, cursive |
| 正文 | Space Mono | IBM Plex Mono, Noto Sans SC, monospace |
| 日文装饰 | Noto Sans JP | sans-serif |
| 中文 | Noto Sans SC | system-ui, sans-serif |

## 字号系统

| 层级 | 尺寸 | 用途 |
|------|------|------|
| display | clamp(2.5rem, 6vw, 5rem) | 主视觉标题 hero |
| h1 | clamp(1.8rem, 4vw, 3rem) | 页面标题 |
| h2 | clamp(1.2rem, 2.5vw, 1.75rem) | 区块标题 |
| h3 | clamp(1rem, 2vw, 1.25rem) | 卡片标题 |
| body | 0.9rem | 正文 |
| small | 0.8rem | 辅助文字 导航链接 |
| caption | 0.75rem | 标题栏文字 标签 |
| deco | 0.7-1.2rem | 日文装饰文字 |

## 行高

| 场景 | line-height |
|------|-------------|
| 标题 | 1.2 |
| 正文 | 1.7 |
| 紧凑文字 (标签/按钮) | 1.0 |

## 字重

| 场景 | font-weight |
|------|-------------|
| Monoton 标题 | 400 (仅支持 400) |
| 正文 | 400 |
| 强调正文 | 700 |

## 字间距

| 场景 | letter-spacing |
|------|----------------|
| 全角蒸汽波文字 | 0.5em |
| 区块标题 | 0.3em |
| 按钮文字 | 0.15em |
| 导航链接 | 0.1em |
| 标题 | 0.08em |
| 日文装饰 | 0.2-0.3em |
| 正文 | normal |

## 文字变换

标题/按钮/导航: text-transform: uppercase
全角蒸汽波效果: 手动使用全角字母 如 Ａ Ｅ Ｓ Ｔ Ｈ Ｅ Ｔ Ｉ Ｃ

## 文字颜色层级

| 层级 | 用法 | CSS 变量 |
|------|------|----------|
| 标题色 | 主标题 hero | var(--text-heading) |
| 主文字 | 正文 | var(--text-primary) |
| 副文字 | 说明 占位符 | var(--text-secondary) |
| 强调文字 | 链接 高亮 | var(--accent-primary) |
| 区块标题 | 小节标题 | var(--accent-secondary) |
| 装饰文字 | 日文片假名 | var(--accent-tertiary) + opacity: 0.2-0.3 |

## 文字阴影

标题霓虹发光:
```
text-shadow:
  0 0 10px var(--accent-primary),
  0 0 30px var(--accent-primary),
  0 0 60px color-mix(in srgb, var(--accent-primary) 40%, transparent);
```

区块标题微光:
```
text-shadow: 0 0 10px color-mix(in srgb, var(--accent-secondary) 40%, transparent);
```

导航悬停:
```
text-shadow: 0 0 8px color-mix(in srgb, var(--accent-secondary) 50%, transparent);
```

## 标题样式参考

```css
.hero-title {
  font-family: 'Monoton', cursive;
  font-size: clamp(2.5rem, 6vw, 5rem);
  font-weight: 400;
  color: var(--text-heading);
  text-align: center;
  letter-spacing: 0.08em;
}

.section-title {
  font-family: 'Space Mono', monospace;
  font-size: clamp(1rem, 2.5vw, 1.5rem);
  color: var(--accent-secondary);
  text-transform: uppercase;
  letter-spacing: 0.3em;
}
```

## 响应式调整

移动端 (< 640px):
- display 标题使用 clamp 下限
- 全角字母间距缩小至 0.2em
- 日文装饰文字隐藏或缩小

## 禁忌

- 正文不使用 Monoton 字体 (可读性差)
- 正文不加 text-shadow (影响阅读)
- letter-spacing 不用于长段落正文
- 避免同时使用全角字母和 text-transform: uppercase
