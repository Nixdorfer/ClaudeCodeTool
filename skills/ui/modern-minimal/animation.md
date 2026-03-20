# 现代极简风格 动画体系

## 缓动函数

```css
--ease-default: cubic-bezier(0.4, 0, 0.2, 1);
--ease-in: cubic-bezier(0.4, 0, 1, 1);
--ease-out: cubic-bezier(0, 0, 0.2, 1);
--ease-in-out: cubic-bezier(0.4, 0, 0.2, 1);
--ease-bounce: cubic-bezier(0.34, 1.56, 0.64, 1);
--ease-spring: cubic-bezier(0.22, 1, 0.36, 1);
```

## 时长

```css
--duration-fast: 0.15s;
--duration-normal: 0.2s;
--duration-slow: 0.3s;
--duration-slower: 0.5s;
--duration-entrance: 0.4s;
```

## 平滑过渡

```css
.transition-all {
  transition: all var(--duration-normal) var(--ease-default);
}

.transition-colors {
  transition: color var(--duration-fast) var(--ease-default),
              background-color var(--duration-fast) var(--ease-default),
              border-color var(--duration-fast) var(--ease-default);
}

.transition-transform {
  transition: transform var(--duration-normal) var(--ease-default);
}

.transition-opacity {
  transition: opacity var(--duration-normal) var(--ease-default);
}

.transition-shadow {
  transition: box-shadow var(--duration-normal) var(--ease-default);
}
```

## 渐显

```css
.fade-in {
  animation: fadeIn var(--duration-entrance) var(--ease-out) both;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

.fade-in-delayed {
  animation: fadeIn var(--duration-entrance) var(--ease-out) 0.1s both;
}
```

## 轻微位移

```css
.fade-up {
  animation: fadeUp var(--duration-entrance) var(--ease-out) both;
}

@keyframes fadeUp {
  from {
    opacity: 0;
    transform: translateY(16px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.fade-down {
  animation: fadeDown var(--duration-entrance) var(--ease-out) both;
}

@keyframes fadeDown {
  from {
    opacity: 0;
    transform: translateY(-16px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.fade-left {
  animation: fadeLeft var(--duration-entrance) var(--ease-out) both;
}

@keyframes fadeLeft {
  from {
    opacity: 0;
    transform: translateX(16px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

.fade-right {
  animation: fadeRight var(--duration-entrance) var(--ease-out) both;
}

@keyframes fadeRight {
  from {
    opacity: 0;
    transform: translateX(-16px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}
```

## 缩放进入

```css
.scale-in {
  animation: scaleIn var(--duration-slow) var(--ease-spring) both;
}

@keyframes scaleIn {
  from {
    opacity: 0;
    transform: scale(0.95);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}
```

## 加载旋转

```css
.spin {
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

.spinner {
  width: 20px;
  height: 20px;
  border: 2px solid rgba(0, 0, 0, 0.1);
  border-top-color: currentColor;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}
```

## 骨架闪烁

```css
.shimmer {
  animation: shimmer 1.5s ease-in-out infinite;
  background: linear-gradient(
    90deg,
    rgba(0, 0, 0, 0.04) 25%,
    rgba(0, 0, 0, 0.08) 50%,
    rgba(0, 0, 0, 0.04) 75%
  );
  background-size: 200% 100%;
}

@keyframes shimmer {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}
```

## 展开收起

```css
.collapse-enter {
  animation: collapseIn var(--duration-slow) var(--ease-default) both;
  overflow: hidden;
}

@keyframes collapseIn {
  from {
    max-height: 0;
    opacity: 0;
  }
  to {
    max-height: 500px;
    opacity: 1;
  }
}

.collapse-exit {
  animation: collapseOut var(--duration-normal) var(--ease-default) both;
  overflow: hidden;
}

@keyframes collapseOut {
  from {
    max-height: 500px;
    opacity: 1;
  }
  to {
    max-height: 0;
    opacity: 0;
  }
}
```

## 脉冲

```css
.pulse {
  animation: pulse 2s var(--ease-in-out) infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}
```

## 交错延迟

```css
.stagger-1 { animation-delay: 0.05s; }
.stagger-2 { animation-delay: 0.1s; }
.stagger-3 { animation-delay: 0.15s; }
.stagger-4 { animation-delay: 0.2s; }
.stagger-5 { animation-delay: 0.25s; }
.stagger-6 { animation-delay: 0.3s; }
```

## 滚动触发

```javascript
const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible");
      }
    });
  },
  { threshold: 0.1 }
);

document.querySelectorAll("[data-animate]").forEach((el) => {
  observer.observe(el);
});
```

```css
[data-animate] {
  opacity: 0;
  transform: translateY(16px);
  transition: opacity var(--duration-entrance) var(--ease-out),
              transform var(--duration-entrance) var(--ease-out);
}

[data-animate].visible {
  opacity: 1;
  transform: translateY(0);
}
```

## 减少动画偏好

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```
