# 现代极简风格 基础规范

## 核心特征

少即是多 大量留白 细线条 无装饰 几何网格 功能至上
灵感来源: 苹果官网 无印良品 北欧设计
每一个像素都有其存在的理由 多余的装饰一概去除

## 页面

```css
html {
  box-sizing: border-box;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-rendering: optimizeLegibility;
  scroll-behavior: smooth;
}

*, *::before, *::after {
  box-sizing: inherit;
  margin: 0;
  padding: 0;
}

body {
  min-height: 100vh;
  overflow-x: hidden;
  line-height: 1.7;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 24px;
}

.section {
  padding: 80px 0;
}

@media (min-width: 768px) {
  .section {
    padding: 120px 0;
  }
}
```

## 字体

无衬线字体族 干净利落 高可读性

```css
font-family: 'Inter', 'Plus Jakarta Sans', 'Noto Sans SC', 'PingFang SC', 'Microsoft YaHei', sans-serif;
```

标题与正文使用同一字体族 通过字重和字号区分层级

## 图标

细线单色风格 线宽 1.5px 统一尺寸网格
推荐图标库: Lucide Feather Icons Phosphor (light weight)
图标颜色跟随文字颜色 不使用多彩图标
尺寸规范: 16px / 20px / 24px 三档

```css
.icon {
  width: 20px;
  height: 20px;
  stroke-width: 1.5;
  fill: none;
  stroke: currentColor;
  flex-shrink: 0;
}

.icon-sm { width: 16px; height: 16px; }
.icon-lg { width: 24px; height: 24px; }
```

## 按钮

简洁矩形或胶囊形 无多余装饰 无渐变 无阴影(悬浮时除外)

```css
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 10px 24px;
  font-family: inherit;
  font-size: 0.875rem;
  font-weight: 500;
  line-height: 1.5;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s ease;
  white-space: nowrap;
  user-select: none;
  outline: none;
}

.btn:focus-visible {
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.3);
}

.btn-pill {
  border-radius: 9999px;
}

.btn-sm {
  padding: 6px 16px;
  font-size: 0.8125rem;
}

.btn-lg {
  padding: 14px 32px;
  font-size: 0.9375rem;
}
```

## Modal

极简白框 大圆角 毛玻璃遮罩 内容居中

```css
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.4);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  z-index: 1000;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
}

.modal {
  background: #ffffff;
  border-radius: 16px;
  padding: 32px;
  max-width: 480px;
  width: 100%;
  max-height: 85vh;
  overflow-y: auto;
  position: relative;
}

.modal-close {
  position: absolute;
  top: 12px;
  right: 12px;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  border: none;
  background: rgba(0, 0, 0, 0.05);
  color: rgba(0, 0, 0, 0.4);
  font-size: 1rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s;
}

.modal-close:hover {
  background: rgba(0, 0, 0, 0.1);
  color: rgba(0, 0, 0, 0.7);
}
```

## 滚动条

极细 透明轨道 圆角滑块

```css
::-webkit-scrollbar {
  width: 6px;
  height: 6px;
}

::-webkit-scrollbar-track {
  background: transparent;
}

::-webkit-scrollbar-thumb {
  background: rgba(0, 0, 0, 0.15);
  border-radius: 3px;
}

::-webkit-scrollbar-thumb:hover {
  background: rgba(0, 0, 0, 0.25);
}

* {
  scrollbar-width: thin;
  scrollbar-color: rgba(0, 0, 0, 0.15) transparent;
}
```

## 设计原则

1. 留白是最重要的设计元素 不要填满每一寸空间
2. 颜色使用极度克制 主要靠黑白灰层次 强调色仅点缀
3. 字号对比要大 大标题非常大 正文保持舒适阅读大小
4. 字重对比要强 标题 700-800 正文 400
5. 所有圆角统一使用 8px 或 12px 保持一致性
6. 动画要微妙 持续时间 0.15-0.3s 避免华丽效果
7. 一切视觉噪音都要消除
