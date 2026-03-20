---
paths:
  - "**/*.html"
  - "**/*.htm"
---

# HTML 编码规范

## 基础

- HTML5 doctype 必须声明
- lang 属性必须设置正确语言
- charset utf-8 必须在 head 最顶部声明
- 使用 2 空格缩进
- 属性值使用双引号
- 自闭合标签不加斜杠 如 `<br>` `<img>`

## 语义化

- 语义标签优先 header nav main section article aside footer
- h1-h6 层级严格递进 不跳级使用
- button 做交互 a 做导航 不混用
- 列表内容用 ul/ol/dl 不用 div 堆叠
- 表格数据用 table 布局禁止使用 table
- figure + figcaption 包裹图片和说明文字

## 可访问性

- img 必须有 alt 属性
- 表单控件必须关联 label
- aria 属性在语义标签不足时使用
- tabindex 管理焦点顺序
- role 属性补充语义信息

## 性能

- CSS 在 head 中 JS 在 body 底部或使用 defer
- 图片设置 width/height 防止布局偏移
- 懒加载非首屏图片 loading="lazy"
- 预加载关键资源 preload/prefetch

## 规范

- 属性顺序 id > class > name > data-* > src/href > 其他
- 布尔属性不写值 如 disabled readonly
- 避免内联样式和内联脚本
- 注释标记大区块起止位置
