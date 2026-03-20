# 动画体系

动画	效果	时长
fade-in	opacity 0→1 + translateY 6px→0	0.25s ease-out
modal-in	opacity + scale(0.95→1) + translateY	0.25s ease-out
dropdown-in	opacity + translateY(4px) + scale(0.96)	0.15s ease-out
bg-drift	背景渐变漂移+缩放+旋转	40s infinite
confirm-pulse	绿色光晕脉冲	2s infinite
状态过渡	transition-colors / transition-all	0.2s ease

## 动态背景

body::before 使用径向绿色渐变 配合 bg-drift 40秒缓慢漂移动画 系统状态变化时通过 data-status 属性改变色调:

busy → 色相偏移+饱和度增强
error → 红色化+亮度增强

## 滚动条

细窄6px宽 透明轨道 rgba(255,255,255,0.1) 圆角滑块
