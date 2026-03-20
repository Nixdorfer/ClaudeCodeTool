---
paths:
  - "**/*.css"
  - "**/*.scss"
  - "**/*.sass"
  - "**/*.less"
---

# CSS 编码规范

## 命名

- BEM 命名 block__element--modifier
- 类名 kebab-case
- 避免 ID 选择器做样式
- 变量用 -- 前缀 如 --color-primary

## 格式

- 2 空格缩进
- 每个属性独占一行
- 声明以分号结尾
- 选择器和花括号之间一个空格
- 多选择器每个独占一行

## 属性顺序

- 第一组 布局 display position float flex grid
- 第二组 盒模型 width height margin padding border
- 第三组 排版 font text line-height color
- 第四组 视觉 background shadow opacity
- 第五组 动画 transition animation transform
- 第六组 其他 cursor pointer-events z-index

## 现代特性

- CSS 变量优先于预处理器变量
- 逻辑属性 margin-inline padding-block 优于物理方向
- gap 优于 margin 做间距
- clamp() 做响应式尺寸
- :is() :where() :has() 简化选择器

## 布局

- Flexbox 一维布局 Grid 二维布局
- 避免固定宽高 用 min/max 约束
- 移动优先 媒体查询 min-width
- container queries 组件级响应式

## 规范

- 避免 !important 除非覆盖第三方样式
- 嵌套不超过 3 层
- 避免通配符选择器
- 动画用 transform/opacity 触发 GPU 加速
- 颜色用 hsl() 或 oklch() 格式
- 统一使用 rem 做尺寸单位 px 仅用于边框
