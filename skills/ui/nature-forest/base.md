# Nature Forest Base

## 核心特征

自然森系风格 以纸张木纹质感为基底 树叶元素贯穿装饰 手绘风线条图标 柔和有机形状 自然光影层次
灵感来源于北欧自然美学 植物图鉴 手作杂货铺 目标是清晨森林般的治愈体验

## 页面

- 背景使用大地暖色 叠加纸张纹理SVG噪点层 opacity 0.03-0.05
- 纸张纹理使用 feTurbulence baseFrequency 0.6-0.9 numOctaves 4 stitchTiles stitch
- 页面留白充足 section 间距 60-80px 内容区最大宽度 960px
- 奇偶 section 交替使用米白和浅苔绿背景 过渡自然
- 全局 border-radius 统一 6-12px 不过于圆润也不方正
- 页面底部可添加地面纹理装饰带 使用渐变模拟草地/泥土

## 字体

- 标题字体 Playfair Display 或 Lora 优雅衬线体
- 正文字体 Source Sans 3 或 Nunito 圆润无衬线
- 手写装饰字体 Caveat 或 Kalam 用于标签和注释
- 中文回退 Noto Serif SC 和 Noto Sans SC
- 手写字体可施加微小旋转 rotate(-1deg ~ -3deg) 增添手作感
- 全局 line-height 1.7-1.8 letter-spacing 0.02em

## 图标

- 手绘线条风格 stroke-width 1.5-2px stroke-linecap round stroke-linejoin round
- 不使用实心填充图标 保持线条感
- 图标颜色跟随文字色或强调色 不独立配色
- 可用植物emoji作为装饰图标 🌿🍃🍂🌱🌸🍀🌾
- SVG图标优先 线条末端带微小弧度模拟手绘抖动
- 图标尺寸 16px/20px/24px 三档

## 按钮

- 主按钮 实心填充强调色 圆角 6px padding 12px 32px font-weight 600
- 次按钮 透明底 1.5px 描边 同色文字 hover 时填充 8% 透明度底色
- 叶形按钮 border-radius 30px 8px 30px 8px hover 时对角翻转为 8px 30px 8px 30px
- 按钮 hover 上浮 translateY(-1px) 配合阴影加深
- 按钮 active 下沉 translateY(0) 阴影收缩
- 按钮 disabled opacity 0.5 cursor not-allowed
- transition all 0.3s ease

## Modal

- 遮罩层 背景色 rgba(74,63,53,0.4) backdrop-filter blur(6px)
- 内容框 纸张底色 border-radius 12px padding 40px max-width 480px
- 边框 1px solid rgba(139,111,71,0.15) 模拟木框质感
- 阴影 0 20px 50px rgba(74,63,53,0.15)
- 顶部装饰 🍃 emoji 或叶子SVG 绝对定位 top -16px 居中
- 关闭按钮 30px 圆形 浅苔绿底 右上角 hover 时加深底色
- 入场动画 从 scale(0.95) opacity(0) 到 scale(1) opacity(1) 300ms ease-out

## 滚动条

- 宽度 6px
- track 背景跟随页面底色
- thumb 使用苔绿色 border-radius 3px
- thumb hover 时颜色加深
- 可选藤蔓纹理 使用 repeating-linear-gradient 模拟节点

## 卡片

- 白色底 1px 边框 rgba(139,111,71,0.12)
- border-radius 10px padding 28px
- 阴影 0 2px 8px rgba(74,63,53,0.06)
- hover 上浮 3px 阴影扩散 边框色过渡到强调绿
- 卡片图标区使用 2rem 大小

## 导航栏

- fixed 顶部 背景色带 0.9 透明度 backdrop-filter blur(12px)
- 底部 1px 边框 rgba(139,111,71,0.1)
- 品牌名使用衬线标题字体 font-weight 700
- 导航链接 font-size 0.9rem font-weight 500 hover 变为强调色
- padding 14px 36px

## 表单输入

- 白色底 1.5px 边框 rgba(139,111,71,0.2) border-radius 8px
- padding 12px 16px font-size 0.95rem
- focus 时边框变为强调绿 外层 0 0 0 3px rgba(强调色,0.1) 光环
- placeholder 使用浅棕色 opacity 0.5
- outline none 使用自定义 focus 样式

## 分隔线

- flex 布局 两侧渐隐线条 中间叶子装饰
- 线条 linear-gradient(90deg, transparent, 大地棕, transparent) height 1px max-width 150px
- 间距 margin 50px 0
