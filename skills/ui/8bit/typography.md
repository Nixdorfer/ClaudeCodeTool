# 8-Bit Typography

## Font Stack

| Priority | Font | Source | Usage |
|----------|------|--------|-------|
| 1 | Press Start 2P | Google Fonts | 标题 / 按钮 / 标签 |
| 2 | VT323 | Google Fonts | 正文 / 对话框 / 长文本 |
| 3 | Noto Sans SC | Google Fonts | 中文回退 |
| 4 | monospace | System | 最终回退 |

```css
--font-display: "Press Start 2P", monospace;
--font-body: "VT323", "Noto Sans SC", monospace;
```

## Font Import

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&family=VT323&family=Noto+Sans+SC:wght@400;700&display=swap" rel="stylesheet">
```

## Size Scale (8px Multiples)

| Token | Size | Line Height | Usage |
|-------|------|-------------|-------|
| --text-2xs | 8px | 16px | 微型标签 / 状态文字 |
| --text-xs | 10px | 20px | 小标签 / 辅助说明 (Press Start 2P) |
| --text-sm | 16px | 28px | 正文小号 (VT323) |
| --text-base | 20px | 32px | 正文默认 (VT323) |
| --text-md | 24px | 36px | 正文大号 (VT323) |
| --text-lg | 14px | 28px | 小标题 (Press Start 2P) |
| --text-xl | 18px | 36px | 标题 (Press Start 2P) |
| --text-2xl | 24px | 44px | 大标题 (Press Start 2P) |
| --text-3xl | 32px | 56px | 主标题 (Press Start 2P) |

Press Start 2P 字体渲染尺寸偏小 实际视觉大小约为同号普通字体的 60-70%
VT323 字体渲染尺寸偏大 实际视觉大小约为同号普通字体的 110-120%
两种字体混用时需要独立的尺寸配置

## Text Rendering

```css
* {
  -webkit-font-smoothing: none;
  -moz-osx-font-smoothing: unset;
  text-rendering: optimizeSpeed;
}

img, canvas {
  image-rendering: pixelated;
  image-rendering: crisp-edges;
}
```

## Text Shadow (Pixel Style)

```css
.text-shadow-sm {
  text-shadow: 2px 2px 0 var(--shadow-sm);
}

.text-shadow-md {
  text-shadow: 4px 4px 0 var(--shadow-md);
}

.text-shadow-outline {
  text-shadow:
    -2px -2px 0 var(--shadow-sm),
    2px -2px 0 var(--shadow-sm),
    -2px 2px 0 var(--shadow-sm),
    2px 2px 0 var(--shadow-sm);
}
```

## Heading Styles

```css
h1 {
  font-family: var(--font-display);
  font-size: var(--text-3xl);
  line-height: 56px;
  color: var(--text-primary);
  text-shadow: 4px 4px 0 var(--shadow-md);
  letter-spacing: 2px;
}

h2 {
  font-family: var(--font-display);
  font-size: var(--text-2xl);
  line-height: 44px;
  color: var(--accent-primary);
  text-shadow: 2px 2px 0 var(--shadow-sm);
  letter-spacing: 2px;
}

h3 {
  font-family: var(--font-display);
  font-size: var(--text-xl);
  line-height: 36px;
  color: var(--accent-secondary);
  text-shadow: 2px 2px 0 var(--shadow-sm);
  letter-spacing: 1px;
}

h4 {
  font-family: var(--font-display);
  font-size: var(--text-lg);
  line-height: 28px;
  color: var(--text-primary);
}
```

## Body Text

```css
body {
  font-family: var(--font-body);
  font-size: var(--text-base);
  line-height: 32px;
  color: var(--text-secondary);
}

p {
  margin-bottom: 16px;
}

strong {
  color: var(--text-primary);
}
```

## Pixel Underline

```css
.pixel-underline::after {
  content: "";
  display: block;
  margin-top: 8px;
  height: 4px;
  background: repeating-linear-gradient(
    90deg,
    currentColor 0px, currentColor 8px,
    transparent 8px, transparent 12px
  );
}
```

## Label / Badge Text

```css
.pixel-label {
  font-family: var(--font-display);
  font-size: var(--text-2xs);
  letter-spacing: 2px;
  text-transform: uppercase;
  line-height: 16px;
}
```

## Monospace Number Display

```css
.pixel-number {
  font-family: var(--font-display);
  font-size: var(--text-xl);
  font-variant-numeric: tabular-nums;
  letter-spacing: 4px;
  color: var(--accent-primary);
  text-shadow: 2px 2px 0 var(--shadow-sm);
}
```

## Constraints

- 所有字号必须产生整数像素渲染 避免亚像素
- line-height 必须是 4px 的倍数
- letter-spacing 只使用整数值
- Press Start 2P 最小可读字号为 8px
- VT323 最小可读字号为 14px
- 中文内容使用 Noto Sans SC 时建议 font-weight: 700 模拟像素方块感
- 禁止使用 font-smooth / antialiased 保持像素锐利边缘
