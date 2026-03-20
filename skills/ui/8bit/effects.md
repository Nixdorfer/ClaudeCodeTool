# 8-Bit Pixel Effects

## Pixel Border Staircase

通过多层 box-shadow 构建阶梯式边框 模拟像素锯齿

```css
.pixel-border-1px {
  box-shadow:
    -1px -1px 0 0 var(--border-strong),
    1px -1px 0 0 var(--border-strong),
    -1px 1px 0 0 var(--border-strong),
    1px 1px 0 0 var(--border-strong);
  border: 1px solid var(--border-strong);
}

.pixel-border-2px {
  box-shadow:
    -2px -2px 0 0 var(--border-strong),
    2px -2px 0 0 var(--border-strong),
    -2px 2px 0 0 var(--border-strong),
    2px 2px 0 0 var(--border-strong);
  border: 2px solid var(--border-strong);
}

.pixel-border-4px {
  box-shadow:
    -4px -4px 0 0 var(--border-strong),
    4px -4px 0 0 var(--border-strong),
    -4px 4px 0 0 var(--border-strong),
    4px 4px 0 0 var(--border-strong);
  border: 4px solid var(--border-strong);
}
```

## Pixel Drop Shadow

只使用整数偏移 blur-radius 始终为 0

```css
.pixel-drop-sm {
  box-shadow: 4px 4px 0 0 var(--shadow-sm);
}

.pixel-drop-md {
  box-shadow: 8px 8px 0 0 var(--shadow-md);
}

.pixel-drop-lg {
  box-shadow:
    4px 4px 0 0 var(--shadow-sm),
    8px 8px 0 0 var(--shadow-md),
    12px 12px 0 0 var(--shadow-lg);
}
```

## Combined Border + Shadow

```css
.pixel-panel {
  border: 4px solid var(--border-strong);
  box-shadow:
    -4px -4px 0 0 var(--border-strong),
    4px -4px 0 0 var(--border-strong),
    -4px 4px 0 0 var(--border-strong),
    4px 4px 0 0 var(--border-strong),
    8px 8px 0 0 var(--shadow-md);
}
```

## Scanline Overlay

```css
.scanlines {
  position: relative;
  overflow: hidden;
}

.scanlines::after {
  content: "";
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(
    0deg,
    transparent 0px,
    transparent 2px,
    rgba(0, 0, 0, 0.15) 2px,
    rgba(0, 0, 0, 0.15) 4px
  );
  pointer-events: none;
  z-index: 10;
}
```

## CRT Screen Curvature

```css
.crt-curve {
  position: relative;
  overflow: hidden;
}

.crt-curve::before {
  content: "";
  position: absolute;
  inset: 0;
  background: radial-gradient(
    ellipse at center,
    transparent 60%,
    rgba(0, 0, 0, 0.25) 100%
  );
  pointer-events: none;
  z-index: 11;
}
```

## CRT Full Effect

```css
.crt-screen {
  position: relative;
  overflow: hidden;
  background: var(--bg-primary);
}

.crt-screen::before {
  content: "";
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(
    0deg,
    transparent 0px,
    transparent 2px,
    rgba(0, 0, 0, 0.12) 2px,
    rgba(0, 0, 0, 0.12) 4px
  );
  pointer-events: none;
  z-index: 10;
}

.crt-screen::after {
  content: "";
  position: absolute;
  inset: 0;
  background: radial-gradient(
    ellipse at center,
    transparent 55%,
    rgba(0, 0, 0, 0.3) 100%
  );
  pointer-events: none;
  z-index: 11;
}
```

## Pixel Rounded Corners (Staircase Simulation)

```css
.pixel-rounded-sm {
  clip-path: polygon(
    4px 0%, calc(100% - 4px) 0%,
    100% 4px, 100% calc(100% - 4px),
    calc(100% - 4px) 100%, 4px 100%,
    0% calc(100% - 4px), 0% 4px
  );
}

.pixel-rounded-md {
  clip-path: polygon(
    8px 0%, calc(100% - 8px) 0%,
    calc(100% - 4px) 4px, 100% 8px,
    100% calc(100% - 8px), calc(100% - 4px) calc(100% - 4px),
    calc(100% - 8px) 100%, 8px 100%,
    4px calc(100% - 4px), 0% calc(100% - 8px),
    0% 8px, 4px 4px
  );
}
```

## Health Bar UI

```css
.hp-container {
  display: flex;
  align-items: center;
  gap: 8px;
}

.hp-label {
  font-size: 8px;
  min-width: 24px;
  color: var(--text-primary);
}

.hp-track {
  flex: 1;
  height: 16px;
  background: var(--input-bg);
  border: 2px solid var(--border-strong);
  box-shadow:
    -2px -2px 0 0 var(--border-strong),
    2px -2px 0 0 var(--border-strong),
    -2px 2px 0 0 var(--border-strong),
    2px 2px 0 0 var(--border-strong);
}

.hp-fill {
  height: 100%;
  background: var(--status-success);
  transition: width 0.5s steps(10);
}

.hp-fill[data-level="mid"] {
  background: var(--status-warning);
}

.hp-fill[data-level="low"] {
  background: var(--status-danger);
}

.hp-value {
  font-size: 8px;
  min-width: 48px;
  text-align: right;
  color: var(--text-primary);
}
```

## Experience Bar UI

```css
.exp-track {
  width: 100%;
  height: 8px;
  background: var(--input-bg);
  border: 2px solid var(--accent-secondary);
}

.exp-fill {
  height: 100%;
  background: var(--exp-bar-fill);
  transition: width 1.2s steps(20);
}
```

## Pixel Grid Overlay

```css
.pixel-grid::after {
  content: "";
  position: absolute;
  inset: 0;
  background-image:
    linear-gradient(rgba(255, 255, 255, 0.02) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
  background-size: 4px 4px;
  pointer-events: none;
}
```

## Screen Flicker

```css
@keyframes screenFlicker {
  0%, 95%, 100% { opacity: 1; }
  96% { opacity: 0.85; }
  97% { opacity: 0.95; }
  98% { opacity: 0.88; }
}

.screen-flicker {
  animation: screenFlicker 4s steps(1) infinite;
}
```

## Pixel Inset Border

```css
.pixel-inset {
  border: 4px solid var(--border-default);
  box-shadow:
    inset 4px 4px 0 0 var(--shadow-sm),
    inset -4px -4px 0 0 rgba(255, 255, 255, 0.05);
}
```

## Constraints

- 阴影永远使用 --shadow-* 系列变量
- 边框永远使用 --border-* 系列变量
- 所有特效叠加层 opacity 不超过 0.3 避免遮挡内容
- 扫描线间距固定 4px 或 2px 保持像素对齐
