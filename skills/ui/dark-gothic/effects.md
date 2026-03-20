# Dark Gothic Effects

## 尖拱边框

### 尖拱容器
- clip-path: polygon(0% 8%, 50% 0%, 100% 8%, 100% 100%, 0% 100%)
- 适用于 modal header card-header hero-section
- 变体(陡峭): polygon(0% 12%, 50% 0%, 100% 12%, 100% 100%, 0% 100%)
- 变体(平缓): polygon(0% 5%, 50% 0%, 100% 5%, 100% 100%, 0% 100%)

### 尖拱按钮
- clip-path: polygon(50% 0%, 100% 15%, 100% 100%, 0% 100%, 0% 15%)
- padding-top 额外增加 6px 补偿尖拱裁切

### 菱形装饰
- clip-path: polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%)
- 用于图标容器 分隔装饰 角饰

### 八边形
- clip-path: polygon(30% 0%, 70% 0%, 100% 30%, 100% 70%, 70% 100%, 30% 100%, 0% 70%, 0% 30%)
- 用于头像框 图标按钮

## 彩窗玻璃效果

### 基础彩窗
- background: linear-gradient(135deg, var(--accent-primary) 0%, transparent 40%), linear-gradient(225deg, var(--accent-secondary) 0%, transparent 40%), var(--glass-bg)
- backdrop-filter: blur(12px) saturate(1.2)
- border: 1px solid var(--glass-border)
- box-shadow: inset 0 0 30px rgba(0,0,0,0.3)

### 彩窗高光条纹
- background-image: repeating-linear-gradient(60deg, transparent, transparent 20px, rgba(255,255,255,0.02) 20px, rgba(255,255,255,0.02) 22px)
- 叠加在彩窗效果之上 模拟铅条分隔

### 彩窗光斑
- 伪元素 position absolute
- background: radial-gradient(ellipse, var(--accent-glow), transparent 70%)
- width: 200px height: 300px
- opacity: 0.3
- animation: stainedGlassShimmer 8s ease-in-out infinite

## 烛火光影

### 烛火光源
- box-shadow: 0 0 60px 20px rgba(var(--accent-primary-rgb), 0.08), 0 0 120px 40px rgba(var(--accent-primary-rgb), 0.04)
- animation: candleFlicker 3s ease-in-out infinite
- 适用于标题 图标 关键装饰元素

### 烛火渐变背景
- background: radial-gradient(ellipse at 50% 30%, rgba(var(--accent-primary-rgb), 0.06) 0%, transparent 50%)
- animation: candleGlow 4s ease-in-out infinite

### 烛火文字
- text-shadow: 0 0 10px rgba(var(--accent-primary-rgb), 0.3), 0 0 30px rgba(var(--accent-primary-rgb), 0.15)
- animation: candleFlicker 3s ease-in-out infinite

## 铁链装饰线

### 水平铁链
- background-image: repeating-linear-gradient(90deg, var(--border-decorative) 0px, var(--border-decorative) 12px, transparent 12px, transparent 16px, var(--border-decorative) 16px, var(--border-decorative) 20px, transparent 20px, transparent 28px)
- height: 4px
- opacity: 0.4

### 垂直铁链
- background-image: repeating-linear-gradient(180deg, var(--border-decorative) 0px, var(--border-decorative) 12px, transparent 12px, transparent 16px, var(--border-decorative) 16px, var(--border-decorative) 20px, transparent 20px, transparent 28px)
- width: 4px
- opacity: 0.4

### 铁链边框
- border-image: repeating-linear-gradient(90deg, var(--border-decorative) 0px, var(--border-decorative) 8px, transparent 8px, transparent 12px) 4
- border-width: 2px
- border-style: solid

## 蔷薇纹样

### 角落蔷薇
- 伪元素 content: "❧"
- position: absolute
- font-size: 1.2rem
- color: var(--accent-primary)
- opacity: 0.3
- 四角位置: top 8px left/right 12px bottom 8px left/right 12px
- transform: rotate(0deg/90deg/180deg/270deg) 分别对应四角

### 蔷薇分隔线
- 中间元素 content: "❧" 或 "✦"
- 两侧线条 flex: 1 max-width: 180px height: 1px
- 线条 background: linear-gradient(90deg, transparent, var(--border-decorative), transparent)
- 中间符号 color: var(--accent-primary) font-size: 1.2rem

### 蔷薇边框图案
- border-image: url("data:image/svg+xml,...") 形式内联 SVG 荆棘纹样
- 或用 background-image 的 repeating pattern 模拟

## 雾气效果

### 底部雾气
- 伪元素 position fixed bottom 0
- background: linear-gradient(to top, rgba(var(--bg-primary-rgb), 0.8) 0%, transparent 100%)
- height: 150px
- pointer-events: none
- animation: fogDrift 12s ease-in-out infinite

### 飘动雾气层
- background: radial-gradient(ellipse at var(--fog-x, 50%) var(--fog-y, 80%), rgba(var(--bg-secondary-rgb), 0.4) 0%, transparent 60%)
- width: 100% height: 100%
- position: fixed
- pointer-events: none
- animation: fogFloat 20s linear infinite
- opacity: 0.15

## 裂纹纹理

### 裂纹叠加
- 用多层 linear-gradient 模拟细线裂纹:
  - background-image: linear-gradient(127deg, transparent 48%, rgba(255,255,255,0.015) 48.5%, transparent 49%), linear-gradient(73deg, transparent 47%, rgba(255,255,255,0.01) 47.5%, transparent 48%), linear-gradient(162deg, transparent 49%, rgba(255,255,255,0.012) 49.3%, transparent 49.6%)
- background-size: 400px 400px
- opacity: 0.5
- pointer-events: none

### 碎裂边框
- border-image: linear-gradient(var(--border-decorative), transparent 20%, var(--border-decorative) 40%, transparent 60%, var(--border-decorative) 80%, transparent) 1
- 营造不均匀断裂感

## 暗角效果

### 全局暗角
- 伪元素 position fixed inset 0
- background: radial-gradient(ellipse at center, transparent 40%, rgba(0,0,0,0.5) 100%)
- pointer-events: none
- z-index: 0

### 图片暗角
- 伪元素覆盖在图片上
- background: radial-gradient(ellipse at center, transparent 50%, rgba(0,0,0,0.6) 100%)

## 十字架/宗教符号装饰

### 顶部十字架
- content: "♰" 或 "✝" 或 "☩"
- position: absolute top: -16px left: 50% transform: translateX(-50%)
- background: var(--bg-primary) padding: 0 15px
- color: var(--accent-primary)
- font-size: 1.5rem

### 符号选集
- 分隔用: ✦ ✠ ⚜
- 宗教/庄严: ♰ ✝ ☩
- 蔷薇/自然: ❧ ☽
- 角饰: ✦ (小号 6-8px)
