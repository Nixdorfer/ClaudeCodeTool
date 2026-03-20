# 现代极简风格 特效规范

## 微妙阴影系统

四级阴影 从几乎不可见到明显但克制

```css
--shadow-xs: 0 1px 2px rgba(0, 0, 0, 0.04);
--shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.06), 0 1px 2px rgba(0, 0, 0, 0.04);
--shadow-md: 0 4px 12px rgba(0, 0, 0, 0.08);
--shadow-lg: 0 8px 30px rgba(0, 0, 0, 0.1);
--shadow-xl: 0 20px 60px rgba(0, 0, 0, 0.15);
```

## 细线边框

```css
--border-light: 1px solid rgba(0, 0, 0, 0.06);
--border-default: 1px solid rgba(0, 0, 0, 0.1);
--border-strong: 1.5px solid rgba(0, 0, 0, 0.15);
--border-focus: 1.5px solid var(--color-accent);
```

## 悬浮抬升

```css
.hover-lift {
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.hover-lift:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.08);
}

.hover-lift:active {
  transform: translateY(0);
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.06);
}
```

## 焦点光环

```css
.focus-ring:focus-visible {
  outline: none;
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.15);
  border-color: rgba(37, 99, 235, 1);
}
```

## 加载骨架屏

```css
.skeleton {
  background: linear-gradient(
    90deg,
    rgba(0, 0, 0, 0.04) 25%,
    rgba(0, 0, 0, 0.08) 50%,
    rgba(0, 0, 0, 0.04) 75%
  );
  background-size: 200% 100%;
  animation: skeleton-shimmer 1.5s ease-in-out infinite;
  border-radius: 6px;
}

@keyframes skeleton-shimmer {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}

.skeleton-text {
  height: 14px;
  margin-bottom: 10px;
  width: 80%;
}

.skeleton-text:last-child {
  width: 60%;
}

.skeleton-avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
}

.skeleton-card {
  height: 200px;
  border-radius: 12px;
}
```

## 分割线

```css
.divider {
  height: 1px;
  background: rgba(0, 0, 0, 0.06);
  border: none;
  margin: 0;
}

.divider-strong {
  background: rgba(0, 0, 0, 0.1);
}

.divider-vertical {
  width: 1px;
  height: 100%;
  background: rgba(0, 0, 0, 0.06);
}

.divider-spaced {
  margin: 32px 0;
}

.divider-section {
  margin: 60px 0;
}
```

## 网格系统

```css
.grid {
  display: grid;
  gap: 24px;
}

.grid-2 { grid-template-columns: repeat(2, 1fr); }
.grid-3 { grid-template-columns: repeat(3, 1fr); }
.grid-4 { grid-template-columns: repeat(4, 1fr); }

.grid-auto {
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
}

@media (max-width: 768px) {
  .grid-2, .grid-3, .grid-4 {
    grid-template-columns: 1fr;
  }
}

@media (min-width: 769px) and (max-width: 1024px) {
  .grid-3, .grid-4 {
    grid-template-columns: repeat(2, 1fr);
  }
}
```

## 毛玻璃效果

```css
.glass {
  backdrop-filter: blur(12px) saturate(180%);
  -webkit-backdrop-filter: blur(12px) saturate(180%);
}

.glass-light {
  background: rgba(255, 255, 255, 0.8);
}

.glass-dark {
  background: rgba(0, 0, 0, 0.4);
}
```

## 卡片效果

```css
.card {
  background: var(--color-card-bg);
  border: 1px solid rgba(0, 0, 0, 0.06);
  border-radius: 12px;
  padding: 24px;
  transition: all 0.2s ease;
}

.card-interactive:hover {
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.08);
  transform: translateY(-2px);
  border-color: transparent;
}

.card-flat {
  border: none;
  background: rgba(0, 0, 0, 0.02);
}
```

## 文字截断

```css
.truncate {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.line-clamp-3 {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
```

## 间距系统

```css
--space-1: 4px;
--space-2: 8px;
--space-3: 12px;
--space-4: 16px;
--space-5: 20px;
--space-6: 24px;
--space-8: 32px;
--space-10: 40px;
--space-12: 48px;
--space-16: 64px;
--space-20: 80px;
--space-24: 96px;
```
