# 现代极简风格 排版规范

## 字体族

```css
--font-sans: 'Inter', 'Plus Jakarta Sans', 'Noto Sans SC', 'PingFang SC', 'Microsoft YaHei', sans-serif;
--font-mono: 'JetBrains Mono', 'Fira Code', 'Cascadia Code', monospace;
```

## 字号

```css
--text-xs: 0.75rem;
--text-sm: 0.8125rem;
--text-base: 0.9375rem;
--text-lg: 1.125rem;
--text-xl: 1.25rem;
--text-2xl: 1.5rem;
--text-3xl: 2rem;
--text-4xl: 2.5rem;
--text-5xl: 3.5rem;
--text-hero: clamp(2.5rem, 6vw, 5rem);
```

## 字重

```css
--font-regular: 400;
--font-medium: 500;
--font-semibold: 600;
--font-bold: 700;
--font-extrabold: 800;
```

## 行高

```css
--leading-tight: 1.1;
--leading-snug: 1.3;
--leading-normal: 1.5;
--leading-relaxed: 1.7;
--leading-loose: 2;
```

## 字间距

```css
--tracking-tighter: -0.03em;
--tracking-tight: -0.02em;
--tracking-normal: 0;
--tracking-wide: 0.02em;
--tracking-wider: 0.05em;
--tracking-caps: 0.08em;
```

## 标题样式

```css
.heading-hero {
  font-family: var(--font-sans);
  font-size: var(--text-hero);
  font-weight: var(--font-extrabold);
  line-height: var(--leading-tight);
  letter-spacing: var(--tracking-tighter);
}

.heading-1 {
  font-family: var(--font-sans);
  font-size: var(--text-4xl);
  font-weight: var(--font-bold);
  line-height: var(--leading-tight);
  letter-spacing: var(--tracking-tight);
}

.heading-2 {
  font-family: var(--font-sans);
  font-size: var(--text-3xl);
  font-weight: var(--font-bold);
  line-height: var(--leading-snug);
  letter-spacing: var(--tracking-tight);
}

.heading-3 {
  font-family: var(--font-sans);
  font-size: var(--text-2xl);
  font-weight: var(--font-semibold);
  line-height: var(--leading-snug);
  letter-spacing: var(--tracking-normal);
}

.heading-4 {
  font-family: var(--font-sans);
  font-size: var(--text-xl);
  font-weight: var(--font-semibold);
  line-height: var(--leading-snug);
  letter-spacing: var(--tracking-normal);
}
```

## 正文样式

```css
.body-lg {
  font-size: var(--text-lg);
  font-weight: var(--font-regular);
  line-height: var(--leading-relaxed);
}

.body-base {
  font-size: var(--text-base);
  font-weight: var(--font-regular);
  line-height: var(--leading-relaxed);
}

.body-sm {
  font-size: var(--text-sm);
  font-weight: var(--font-regular);
  line-height: var(--leading-normal);
}
```

## 辅助样式

```css
.caption {
  font-size: var(--text-xs);
  font-weight: var(--font-medium);
  line-height: var(--leading-normal);
  letter-spacing: var(--tracking-wide);
}

.overline {
  font-size: var(--text-xs);
  font-weight: var(--font-semibold);
  line-height: var(--leading-normal);
  letter-spacing: var(--tracking-caps);
  text-transform: uppercase;
}

.label {
  font-size: var(--text-sm);
  font-weight: var(--font-medium);
  line-height: var(--leading-normal);
}

.code {
  font-family: var(--font-mono);
  font-size: 0.875em;
  padding: 2px 6px;
  border-radius: 4px;
  background: rgba(0, 0, 0, 0.04);
}
```

## 段落间距

```css
.prose p + p { margin-top: 1.25em; }
.prose h2 + p { margin-top: 0.75em; }
.prose h3 + p { margin-top: 0.5em; }
.prose p + h2 { margin-top: 2em; }
.prose p + h3 { margin-top: 1.5em; }
```

## 圆角

```css
--radius-sm: 4px;
--radius-md: 8px;
--radius-lg: 12px;
--radius-xl: 16px;
--radius-2xl: 24px;
--radius-full: 9999px;
```
