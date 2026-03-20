# 动画体系

## 星空漂移

名称: star-drift
效果: 整个星空容器缓慢平移 模拟太空漂移感
关键帧: translateX(0)translateY(0) > translateX(-20px)translateY(-15px) > translateX(10px)translateY(-30px) > translateX(0)translateY(0)
时长: 120s
缓动: linear
循环: infinite

## 星星闪烁

名称: twinkle
效果: 单个星星透明度周期变化
关键帧: opacity 0.3 > 1 > 0.3
时长: 2s + 随机4s (每个星星独立)
缓动: ease-in-out
循环: infinite
延迟: 每个星星随机 0-3s

## 全息闪烁

名称: holo-flicker
效果: 全息面板透明度微弱抖动 模拟投影不稳定
关键帧: opacity 1 > 0.97 > 1 > 0.95 > 1 > 0.98 > 1
时长: 4s
缓动: step-end (硬切换 非平滑)
循环: infinite

## 全息干扰

名称: holo-glitch
效果: 水平位移+色彩偏移 短暂干扰
关键帧: translateX(0) > translateX(-3px) skewX(-1deg) > translateX(2px) > translateX(0)
叠加: 伪元素 clip-path随机条纹 rgba(74,168,216,0.1) 快速闪现
时长: 0.3s
缓动: step-end
触发: class添加时执行一次 或 2% 概率随机触发

## 雷达旋转

名称: radar-sweep
效果: 扫描臂360度匀速旋转
关键帧: rotate(0deg) > rotate(360deg)
时长: 4s
缓动: linear
循环: infinite

## 能量脉冲

名称: energy-pulse
效果: 能量条/指示灯周期性亮度脉冲
关键帧: opacity 0.7 + box-shadow 0 0 4px > opacity 1 + box-shadow 0 0 12px > opacity 0.7 + box-shadow 0 0 4px
颜色: 跟随当前强调色
时长: 2s
缓动: ease-in-out
循环: infinite

## 能量流动

名称: energy-flow
效果: 能量条纹理向右滚动
关键帧: background-position 0% > 200%
时长: 2s
缓动: linear
循环: infinite

## 引擎尾焰

名称: engine-trail
效果: 引擎喷射口发光+粒子向后扩散消散
粒子: 3-5个圆点 从喷口向外扩散
关键帧: scale(1) opacity(0.8) > scale(2.5) opacity(0) translateX(-30px)
颜色: 核心 rgba(232,118,42,0.9) 外围 rgba(232,118,42,0.3)
喷口发光: box-shadow 0 0 20px rgba(232,118,42,0.5)
时长: 1.5s
缓动: ease-out
循环: infinite
延迟: 粒子间错开 0.3s

## 数据流滚动

名称: data-scroll
效果: 数据面板内文字/数字向上滚动 模拟实时数据流
关键帧: translateY(0) > translateY(-100%)
时长: 10s (可按数据量调整)
缓动: linear
循环: infinite
上下遮罩: 顶部和底部各20px渐变到透明 遮盖滚动边缘

## 警报闪烁

名称: alert-flash
效果: 警报状态全局/局部红色闪烁
关键帧:
- 边框: rgba(220,60,60,0.3) > rgba(220,60,60,0.8) > rgba(220,60,60,0.3)
- 背景: 叠加 rgba(220,60,60,0.02) > rgba(220,60,60,0.06) > rgba(220,60,60,0.02)
- 可选: 全局 body::after 叠加红色 vignette
时长: 1.5s
缓动: ease-in-out
循环: infinite
触发: data-status="alert" 或 .alert-active class

## 扫描线

名称: scan-line
效果: 水平光线从上到下扫描面板
关键帧: translateY(-100%) > translateY(容器高度)
线条: 高度2px 宽度100%
颜色: linear-gradient(90deg, transparent, rgba(74,168,216,0.6), transparent)
发光: box-shadow 0 0 12px rgba(74,168,216,0.3)
时长: 2s
缓动: ease-in-out
循环: infinite

## 流星划过

名称: shooting-star
效果: 随机位置出现的快速流星
关键帧: translateX(0)translateY(0) opacity(1) > translateX(300px)translateY(200px) opacity(0)
元素: 2px圆点 白色 + 拖尾 box-shadow
时长: 1s
缓动: ease-out
循环: forwards (单次)
触发: JS定时随机生成 间隔 8-15s

## 轨道旋转

名称: orbit
效果: 元素绕中心点椭圆轨道运动
关键帧: rotate(0deg) translateX(80px) rotate(0deg) > rotate(360deg) translateX(80px) rotate(-360deg)
时长: 20s
缓动: linear
循环: infinite

## 状态过渡

名称: 通用 transition
属性: color/background/border-color/box-shadow/opacity/transform
时长: 0.2s
缓动: ease
适用: 所有交互元素的 hover/focus/active 状态切换

## 进场动画

fade-in: opacity 0>1 + translateY(8px>0) 0.25s ease-out
modal-in: opacity 0>1 + scale(0.95>1) + translateY(10px>0) 0.25s ease-out
dropdown-in: opacity 0>1 + translateY(4px>0) + scale(0.96>1) 0.15s ease-out
slide-in-left: opacity 0>1 + translateX(-20px>0) 0.3s ease-out
slide-in-right: opacity 0>1 + translateX(20px>0) 0.3s ease-out

## 星云漂移

名称: nebula-drift
效果: body::before 星云渐变缓慢移动+缩放
关键帧: background-position 0% 0% scale(1) > 30% 20% scale(1.1) > 60% 40% scale(1.05) > 0% 0% scale(1)
时长: 60s
缓动: ease-in-out
循环: infinite

## 系统状态色调变化

通过 data-status 属性控制全局色调
idle: 默认蓝橙色调
busy: filter hue-rotate(10deg) saturate(1.2) 星云渐变增强
error: 叠加红色 vignette + alert-flash 动画
success: 短暂绿色脉冲 0.5s后恢复
