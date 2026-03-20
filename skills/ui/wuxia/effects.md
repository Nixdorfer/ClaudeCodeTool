# 武侠水墨风 特效规范

## 水墨晕染

入场时元素从模糊到清晰 模拟墨滴在宣纸上晕开

- filter: blur(20px) -> blur(0)
- opacity: 0 -> 1
- transform: scale(0.85) -> scale(1)
- duration: 1.0s-1.4s
- easing: cubic-bezier(0.25, 0.46, 0.45, 0.94)

## 宣纸纹理

用多层 radial-gradient 模拟宣纸纤维质感

- 底层: 纯色背景
- 纤维层1: radial-gradient(ellipse at 20% 80%, rgba(200,190,170,0.2) 0%, transparent 50%)
- 纤维层2: radial-gradient(ellipse at 80% 20%, rgba(180,170,150,0.15) 0%, transparent 50%)
- 纤维层3: radial-gradient(ellipse at 50% 50%, rgba(210,200,180,0.1) 0%, transparent 40%)
- 可叠加 noise texture 作为 background-image (base64 SVG)

## 毛笔笔锋边框

用不规则 border-width 模拟毛笔运笔的粗细变化

- 上边框: 1px
- 右边框: 2px
- 下边框: 2px
- 左边框: 1px
- 或使用 border-image 配合 SVG 毛笔笔触图案
- 替代方案: 用 box-shadow 叠加实现 如 box-shadow: -1px 0 0 borderColor, 0 2px 0 borderColor

## 远山水墨背景

用 radial-gradient 堆叠模拟水墨远山

- 层1 (近山): radial-gradient(ellipse at 30% 100%, rgba(100,100,90,0.15) 0%, transparent 60%)
- 层2 (中山): radial-gradient(ellipse at 70% 100%, rgba(80,80,70,0.12) 0%, transparent 55%)
- 层3 (远山): radial-gradient(ellipse at 50% 100%, rgba(60,60,55,0.08) 0%, transparent 70%)
- 容器高度: 180px-250px
- position: absolute bottom:0 pointer-events: none

## 云雾缭绕

用 radial-gradient 椭圆模拟云层 配合位移动画

- 单云尺寸: width 180px-280px height 50px-80px
- 形状: radial-gradient(ellipse, rgba(cloudColor, 0.25), transparent)
- border-radius: 50%
- 动画: translateX(0) -> translateX(25px-40px) 往返
- opacity: 0.15 - 0.35 间变化
- duration: 12s-20s
- easing: ease-in-out
- 布置 2-4 朵在不同位置 错开动画延迟

## 剑气光效

用于按钮点击/重要操作反馈 线性光芒划过

- 伪元素实现: width 2px height 120% 斜 45 度
- background: linear-gradient(transparent, rgba(accentColor, 0.6), transparent)
- 从左划到右: translateX(-100%) -> translateX(200%)
- duration: 0.5s-0.8s
- easing: ease-out
- 使用 overflow: hidden 裁剪

## 印章效果

用 border + transform 模拟方形或圆形印章

方形印章:
- border: 2px solid accentColor
- padding: 4px 8px
- transform: rotate(-5deg to -12deg)
- font-family: 书法字体
- line-height: 1.2

圆形印章:
- border: 2px solid accentColor
- border-radius: 50%
- width/height 相等 50px-70px
- display: inline-flex align-items center justify-content center
- transform: rotate(-8deg)

印章盖下动画:
- transform: scale(1.5) rotate(-15deg) -> scale(1) rotate(-8deg)
- opacity: 0.3 -> 1
- duration: 0.4s
- easing: cubic-bezier(0.34, 1.56, 0.64, 1)

## 水墨滴落

hover 或交互时 从元素中心扩散的墨滴效果

- 用伪元素 radial-gradient 实现
- background: radial-gradient(circle, rgba(inkColor, 0.15) 0%, transparent 70%)
- transform: scale(0) -> scale(2.5)
- opacity: 0.8 -> 0
- duration: 0.8s
- pointer-events: none

## 卷轴边框

容器左右两侧加卷轴轴头装饰

- 伪元素 before/after
- width: 6px-8px
- height: 110%-120%
- background: 深色 比边框色深
- border-radius: 3px-4px
- position: absolute top: 50% transform: translateY(-50%)
- left: -3px / right: -3px

## 墨迹飞溅

点击时从点击位置向外溅出的小墨点

- 用 JS 生成 4-8 个小 div
- 尺寸: 3px-8px 随机
- background: rgba(inkColor, 0.3-0.6)
- border-radius: 50%
- 向四周随机方向飞出 距离 20px-60px
- 同时缩小并透明消失
- duration: 0.4s-0.7s
- easing: ease-out

## CSS 滤镜模拟水墨画

将图片转为水墨画风格

- filter: grayscale(100%) contrast(1.1) brightness(1.05) sepia(15%)
- 或 filter: grayscale(90%) sepia(20%) contrast(1.05)
- 可叠加宣纸纹理层 mix-blend-mode: multiply