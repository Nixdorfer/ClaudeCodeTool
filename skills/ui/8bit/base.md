# 8-Bit Pixel Style Base

## Core Identity

8-Bit像素风 所有视觉元素由方块构成 无圆角 无渐变 无平滑过渡 模拟FC红白机/GameBoy/SNES时代的低分辨率美学

## Mandatory Rules

- border-radius 全局禁止 所有元素保持直角
- 所有尺寸必须是 4px 的整数倍 模拟像素对齐网格
- image-rendering: pixelated 应用于所有图像和画布元素
- 过渡动画只使用 steps() 时序函数 禁止 ease/linear 等平滑缓动
- 颜色总数不超过 16 色 模拟有限调色板
- box-shadow 只使用整数偏移 禁止模糊半径 (blur-radius 始终为 0)
- 所有交互反馈必须是离散的(步进式) 不允许连续变化

## Layout

- 网格系统基于 4px 基准单元
- 间距序列: 4px / 8px / 12px / 16px / 24px / 32px / 48px
- 容器最大宽度: 960px (240 个像素单元)
- 内边距统一: 组件内部 16px 或 24px
- 外边距统一: 组件之间 24px 或 32px

## Pixel Border System

像素边框通过 box-shadow 阶梯实现 这是整个风格的视觉基石

```css
.pixel-border-sm {
  border: 2px solid;
  box-shadow:
    -2px -2px 0 0 currentColor,
    2px -2px 0 0 currentColor,
    -2px 2px 0 0 currentColor,
    2px 2px 0 0 currentColor;
}

.pixel-border {
  border: 4px solid;
  box-shadow:
    -4px -4px 0 0 currentColor,
    4px -4px 0 0 currentColor,
    -4px 4px 0 0 currentColor,
    4px 4px 0 0 currentColor;
}

.pixel-border-lg {
  border: 4px solid;
  box-shadow:
    -4px -4px 0 0 currentColor,
    4px -4px 0 0 currentColor,
    -4px 4px 0 0 currentColor,
    4px 4px 0 0 currentColor,
    -8px 0 0 0 currentColor,
    8px 0 0 0 currentColor,
    0 -8px 0 0 currentColor,
    0 8px 0 0 currentColor;
}
```

## Pixel Shadow

```css
.pixel-shadow {
  box-shadow: 4px 4px 0 0 rgba(0, 0, 0, 0.5);
}

.pixel-shadow-lg {
  box-shadow: 8px 8px 0 0 rgba(0, 0, 0, 0.5);
}
```

## Background Grid Texture

```css
.pixel-grid-bg {
  background-image:
    linear-gradient(rgba(255, 255, 255, 0.02) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
  background-size: 4px 4px;
}
```

## Game UI Elements

### Health Bar

```css
.hp-bar-container {
  background: rgba(0, 0, 0, 0.6);
  border: 4px solid;
  height: 24px;
  width: 100%;
  position: relative;
  box-shadow:
    -4px -4px 0 0 currentColor,
    4px -4px 0 0 currentColor,
    -4px 4px 0 0 currentColor,
    4px 4px 0 0 currentColor;
}

.hp-bar-fill {
  height: 100%;
  transition: width 0.6s steps(12);
}
```

### Experience Bar

```css
.exp-bar-container {
  background: rgba(0, 0, 0, 0.6);
  border: 2px solid;
  height: 12px;
  width: 100%;
}

.exp-bar-fill {
  height: 100%;
  transition: width 1s steps(20);
}
```

### Status Badge

```css
.status-badge {
  display: inline-block;
  padding: 4px 12px;
  font-size: 8px;
  text-transform: uppercase;
  letter-spacing: 2px;
  border: 2px solid;
}
```

## RPG Dialog Box

```css
.dialog-box {
  border: 4px solid;
  padding: 24px;
  position: relative;
  box-shadow:
    -4px -4px 0 0 currentColor,
    4px -4px 0 0 currentColor,
    -4px 4px 0 0 currentColor,
    4px 4px 0 0 currentColor,
    8px 8px 0 0 rgba(0, 0, 0, 0.4);
}

.dialog-box::after {
  content: '\25BC';
  position: absolute;
  bottom: 8px;
  right: 12px;
  font-size: 12px;
}
```

## Button Base

```css
.pixel-btn {
  border: 4px solid;
  padding: 12px 24px;
  cursor: pointer;
  position: relative;
  transition: none;
  image-rendering: pixelated;
  line-height: 1.5;
  box-shadow:
    -4px -4px 0 0 currentColor,
    4px -4px 0 0 currentColor,
    -4px 4px 0 0 currentColor,
    4px 4px 0 0 currentColor,
    8px 8px 0 0 rgba(0, 0, 0, 0.4);
}

.pixel-btn:active {
  box-shadow:
    -4px -4px 0 0 currentColor,
    4px -4px 0 0 currentColor,
    -4px 4px 0 0 currentColor,
    4px 4px 0 0 currentColor;
  transform: translate(4px, 4px);
}

.pixel-btn:hover::before {
  content: '\25B6';
  margin-right: 8px;
}
```

## Input Base

```css
.pixel-input {
  border: 4px solid;
  padding: 10px 12px;
  width: 100%;
  outline: none;
  transition: none;
}

.pixel-input:focus {
  box-shadow:
    -4px -4px 0 0 currentColor,
    4px -4px 0 0 currentColor,
    -4px 4px 0 0 currentColor,
    4px 4px 0 0 currentColor;
}
```

## Divider

```css
.pixel-divider {
  height: 4px;
  background: repeating-linear-gradient(
    90deg,
    currentColor 0px, currentColor 8px,
    transparent 8px, transparent 16px
  );
  margin: 32px 0;
  border: none;
}
```

## Scrollbar

```css
::-webkit-scrollbar {
  width: 12px;
}

::-webkit-scrollbar-track {
  border-left: 4px solid;
}

::-webkit-scrollbar-thumb {
  background: currentColor;
}
```

## Icon System

| Symbol | Usage |
|--------|-------|
| ♥ | 生命/收藏 |
| ★ | 评分/星级 |
| ▶ | 选择光标/播放 |
| ■ | 停止/填充 |
| ● | 圆点/项目符号 |
| ◆ | 菱形/特殊标记 |
| ▼ | 下拉/继续 |
| ✦ | 魔法/特效 |
