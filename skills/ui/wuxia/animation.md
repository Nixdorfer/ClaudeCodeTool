# 武侠水墨风 动画体系

## 全局动画原则

- 缓慢优雅 不急促 体现水墨写意的从容
- 默认 duration: 0.8s-1.5s (入场) 0.3s-0.5s (交互)
- 默认 easing: cubic-bezier(0.25, 0.46, 0.45, 0.94)
- 减少弹性动画 多用 ease-out 和自定义缓动
- prefers-reduced-motion 时简化为 opacity 渐变

## 水墨扩散 (inkSpread)

用途: 页面/区块入场

keyframes inkSpread:
  0%:   opacity 0, filter blur(20px), transform scale(0.85)
  60%:  opacity 0.8, filter blur(4px), transform scale(0.98)
  100%: opacity 1, filter blur(0), transform scale(1)

duration: 1.2s
easing: cubic-bezier(0.25, 0.46, 0.45, 0.94)
fill-mode: both

## 卷轴展开 (scrollUnfold)

用途: modal/面板展开

竖向展开 (从中间向上下):

keyframes scrollUnfoldY:
  0%:   clip-path inset(48% 0 48% 0), opacity 0
  40%:  clip-path inset(20% 0 20% 0), opacity 0.6
  100%: clip-path inset(0 0 0 0), opacity 1

duration: 0.8s
easing: cubic-bezier(0.22, 0.61, 0.36, 1)

横向展开 (从中间向左右):

keyframes scrollUnfoldX:
  0%:   clip-path inset(0 48% 0 48%), opacity 0
  40%:  clip-path inset(0 15% 0 15%), opacity 0.7
  100%: clip-path inset(0 0 0 0), opacity 1

duration: 0.7s
easing: cubic-bezier(0.22, 0.61, 0.36, 1)

## 剑气飞掠 (swordSlash)

用途: 按钮点击/重要交互 光芒划过效果

keyframes swordSlash:
  0%:   transform translateX(-120%) rotate(45deg), opacity 0
  20%:  opacity 1
  80%:  opacity 1
  100%: transform translateX(220%) rotate(45deg), opacity 0

伪元素属性:
  width: 2px
  height: 150%
  background: linear-gradient(transparent, rgba(accentColor, 0.6), transparent)
  position: absolute

duration: 0.6s
easing: ease-out
trigger: click
容器: overflow hidden

## 落叶飘零 (fallingLeaf)

用途: 背景装饰/加载等待

keyframes fallingLeaf:
  0%:   transform translateY(-20px) translateX(0) rotate(0deg), opacity 0
  10%:  opacity 0.6
  50%:  transform translateY(50vh) translateX(30px) rotate(180deg), opacity 0.4
  100%: transform translateY(100vh) translateX(-10px) rotate(360deg), opacity 0

叶子属性:
  width: 8px-15px
  height: 12px-20px
  background: rgba(accentColor, 0.3)
  border-radius: 50% 0 50% 0 (叶片形状)

duration: 4s-8s (随机)
easing: ease-in-out
delay: 0-5s (错开)
iteration: infinite
数量: 5-12 片

## 云雾流动 (cloudDrift)

用途: 背景装饰

keyframes cloudDrift:
  0%:   transform translateX(0), opacity 0.25
  50%:  transform translateX(30px), opacity 0.12
  100%: transform translateX(0), opacity 0.25

云属性:
  width: 180px-280px
  height: 50px-80px
  background: radial-gradient(ellipse, rgba(cloudColor, 0.25), transparent)
  border-radius: 50%

duration: 12s-20s
easing: ease-in-out
iteration: infinite

## 印章盖下 (sealStamp)

用途: 印章组件入场/点击

keyframes sealStamp:
  0%:   transform scale(1.6) rotate(-15deg), opacity 0.2
  60%:  transform scale(0.95) rotate(-6deg), opacity 1
  80%:  transform scale(1.05) rotate(-9deg)
  100%: transform scale(1) rotate(-8deg)

duration: 0.5s
easing: cubic-bezier(0.34, 1.56, 0.64, 1)

## 墨滴入水 (inkDrop)

用途: 元素入场/hover 反馈

keyframes inkDrop:
  0%:   伪元素 radial-gradient scale(0), opacity 0.8
  100%: 伪元素 radial-gradient scale(2.5), opacity 0

伪元素:
  background: radial-gradient(circle, rgba(inkColor, 0.15) 0%, transparent 70%)
  pointer-events: none

duration: 0.8s
easing: ease-out

## 书卷翻页 (pageFlip)

用途: 切换页面/tab 内容

keyframes pageFlipOut:
  0%:   transform perspective(800px) rotateY(0deg), opacity 1
  100%: transform perspective(800px) rotateY(-90deg), opacity 0

keyframes pageFlipIn:
  0%:   transform perspective(800px) rotateY(90deg), opacity 0
  100%: transform perspective(800px) rotateY(0deg), opacity 1

duration: 0.5s each
easing: ease-in (out) / ease-out (in)
transform-origin: left center

## 笔走龙蛇 (brushStroke)

用途: 下划线/分隔线 从左到右绘制

keyframes brushStroke:
  0%:   width 0, opacity 0.5
  30%:  opacity 1
  100%: width 100%, opacity 1

应用于伪元素:
  height: 2px
  background: linear-gradient(90deg, accentColor, transparent)

duration: 0.6s-1.0s
easing: cubic-bezier(0.4, 0, 0.2, 1)

## 元素淡入 (fadeInUp)

用途: 列表项/卡片依次入场

keyframes fadeInUp:
  0%:   transform translateY(20px), opacity 0
  100%: transform translateY(0), opacity 1

duration: 0.6s
easing: cubic-bezier(0.25, 0.46, 0.45, 0.94)
stagger delay: 0.08s-0.12s (每项递增)

## 交互反馈

hover 效果:
- 卡片: transform translate(-2px, -2px) + 增加阴影, duration 0.3s
- 按钮: translateY(-1px) + 阴影加深, duration 0.25s
- 链接: color 过渡 + 底部圆点 scale(0)->scale(1), duration 0.3s

active/click 效果:
- 按钮: translateY(1px) 按压感, duration 0.1s
- 剑气飞掠触发

focus 效果:
- 输入框底线颜色过渡 + 宽度 1px->2px, duration 0.3s

## 过渡时长参考

| 场景 | 时长 | 缓动 |
|------|------|------|
| 颜色变化 | 0.3s | ease |
| 位移/尺寸 | 0.3s-0.4s | ease-out |
| 入场动画 | 0.8s-1.4s | cubic-bezier(0.25, 0.46, 0.45, 0.94) |
| 退场动画 | 0.3s-0.5s | ease-in |
| 加载等待 | 循环 | ease-in-out |
| 页面切换 | 0.5s | ease-in-out |

## stagger 规则

列表项/网格项依次入场:
- 基础延迟: 0.08s-0.12s 每项
- 最大延迟上限: 1.2s (避免末尾项等太久)
- 超过 12 项时改为分组 stagger