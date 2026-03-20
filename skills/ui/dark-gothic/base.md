# Dark Gothic Base

## 核心特征

暗黑哥特风格 深黑紫背景如深渊般沉寂 尖拱窗花装饰贯穿全局 哥特衬线体营造中世纪手抄本氛围 烛火光效赋予页面神秘摇曳感 铁链与蔷薇元素交织暗黑浪漫

## 页面基础

- 背景: 深黑紫纯色底 叠加径向渐变暗角 营造教堂穹顶下的幽暗感
- 背景纹理: 可选裂纹石材纹理或羊皮纸纹理 opacity 0.03-0.05
- 暗角遮罩: 固定定位伪元素 径向渐变从中心透明到边缘半透明黑
- 最小高度 100vh 禁止水平滚动
- 内容区最大宽度 1200px 居中 左右 padding 24px

## 字体

- 标题字体: `UnifrakturMaguntia, "IM Fell English SC", cursive` 哥特花体
- 副标题字体: `Cinzel, "Cinzel Decorative", serif` 罗马碑文风
- 正文字体: `"EB Garamond", "Cormorant Garamond", "Noto Serif SC", "SimSun", serif`
- 代码字体: `"Fira Code", "JetBrains Mono", monospace`
- Google Fonts 导入: UnifrakturMaguntia Cinzel EB Garamond Cormorant Garamond Noto Serif SC

## 图标

- 风格: 哥特线条图标 细线条 尖角转折 带有荆棘/蔷薇装饰感
- 推荐图标库: 自定义 SVG 或 Font Awesome 的哥特相关图标
- 装饰符号集: ✦ ♰ ❧ ✠ ☽ ⚜ ☩ ✝ 用于分隔线和角饰
- 图标颜色跟随强调色 hover 时跟随主强调色
- 图标 stroke-width: 1-1.5px 保持纤细感

## 按钮

### 尖拱形主按钮
- 形状: clip-path 实现尖拱顶部造型 `polygon(50% 0%, 100% 15%, 100% 100%, 0% 100%, 0% 15%)`
- 背景: 线性渐变从上到下 强调色到深色
- 边框: 1px solid 强调色亮化
- padding: 18px 40px 14px 40px (顶部加大适应尖拱)
- 字体: Cinzel 0.85rem 大写 letter-spacing 0.15em
- hover: box-shadow 外发光 + 内发光 背景渐变亮化
- active: 略微缩小 transform scale(0.98)
- 伪元素角饰: ✦ 符号绝对定位在左右两侧

### 菱形次要按钮
- 形状: transform rotate(0deg) 但边框用菱形装饰线
- 背景: transparent
- 边框: 1px solid 装饰色
- hover: 边框色和文字色亮化
- 四角用伪元素添加小菱形装饰点

### 幽灵按钮
- 背景: transparent
- 边框: 1px solid 文字次要色
- hover: 背景微透明 边框色变强调色

### 图标按钮
- 圆形或八边形 clip-path
- 尺寸: 36px / 44px / 52px 三档
- 背景: 半透明深色
- hover: 强调色发光

## Modal 弹窗

- 遮罩: 固定全屏 rgba(0,0,0,0.92)
- 容器: 深色渐变背景 双层边框模拟教堂窗花
- 外边框: 1px solid 装饰色 带哥特尖拱 clip-path 顶部
- 内边框: 伪元素 inset 10px 1px solid 装饰色低透明度
- 顶部装饰: ♰ 符号居中 背景色衬底
- 四角装饰: 用伪元素或额外元素添加蔷薇/荆棘角饰
- padding: 44px
- max-width: 500px width: 90%
- box-shadow: 0 0 60px 强调色极低透明度
- 关闭按钮: 绝对定位右上 Cinzel 字体 强调色 hover 亮化

## 滚动条

- 宽度: 6px
- track: 背景主色
- thumb: 强调色 可选带铁链纹理 background-image repeating-linear-gradient
- thumb hover: 强调色亮化
- 圆角: 0px 保持哥特硬朗线条

## 分隔线

- 使用 flex 布局 两侧线条 中间装饰符号
- 线条: linear-gradient 从透明到装饰色再到透明 高度 1px max-width 180px
- 中间符号: ✦ ♰ ❧ ✠ 任选 强调色 font-size 1.2rem
- margin: 50px 0

## 卡片

- 背景: 半透明深色 rgba
- 边框: 1px solid 装饰色低透明度
- hover: 边框色变强调色 box-shadow 外发光
- 右上角蔷薇装饰: ❧ 伪元素 强调色低透明度
- padding: 32px
- transition: all 0.3s ease

## 导航栏

- 固定顶部 深色半透明背景 底部装饰色细线
- 品牌名: UnifrakturMaguntia 字体
- 导航链接: Cinzel 字体 0.8rem 大写 letter-spacing 0.1em
- hover: 强调色
- 可选: 底部添加哥特花纹 border-image

## 表单输入框

- 背景: 半透明深色
- 边框: 1px solid 装饰色低透明度
- focus: 边框色变强调色 box-shadow 发光
- font-family: EB Garamond
- padding: 12px 16px
- placeholder 色: 文字次要色更低透明度

## 设计准则

- 色调极度克制 大面积深黑 强调色仅用于关键点缀
- 哥特花体仅用于大标题 正文必须高可读性衬线体
- 动画极其缓慢微妙 像烛火而非烟花
- 避免任何可爱或活泼元素 一切沉稳庄严略带阴郁
- 图片加暗色滤镜和暗角处理
- 圆角全局为 0px 保持哥特尖锐硬朗感 仅特殊组件用尖拱 clip-path
