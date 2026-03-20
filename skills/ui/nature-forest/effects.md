# Nature Forest Effects

## 纸张纹理

```css
background-image: url("data:image/svg+xml,...");
feTurbulence: baseFrequency 0.8 numOctaves 4 stitchTiles stitch opacity 0.03
position: fixed;
top: 0;
left: 0;
width: 100%;
height: 100%;
opacity: 0.3;
pointer-events: none;
z-index: 0;
```

## 木纹背景

```css
background-image:
  repeating-linear-gradient(85deg, rgba(139,111,71,0.03) 0px, rgba(139,111,71,0.01) 2px, transparent 2px, transparent 8px),
  repeating-linear-gradient(87deg, rgba(139,111,71,0.02) 0px, transparent 1px, transparent 12px);
background-size: 100% 100%;
```

## 树叶飘落粒子

```
粒子类型: emoji 🍃🌿🍂🍀
生成间隔: 2000ms
起始位置: top -30px left random(0-100)vw
字号范围: 14px - 26px
透明度: 0.5 -> 0
动画时长: 6s - 12s (随机)
动画函数: linear forwards
运动路径: 正弦曲线摇摆 translateX -20px 到 30px
旋转: 0deg -> 360deg
清除时机: 动画结束后 remove
z-index: 9999
pointer-events: none
```

## 光斑闪烁 (阳光穿透)

```css
width: 60px - 120px
height: 60px - 120px
border-radius: 50%
background: radial-gradient(circle, rgba(255,240,200,0.3) 0%, transparent 70%)
position: fixed
pointer-events: none
z-index: 1
animation: sunspot 4s-8s ease-in-out infinite alternate
```

```
@keyframes sunspot
  0%, 100%: opacity 0.3 scale(1)
  50%: opacity 0.5 scale(1.1)
```

## 水滴涟漪

```css
border-radius: 50%
border: 1px solid rgba(45,106,79,0.15)
background: transparent
animation: ripple 2s ease-out forwards
```

```
@keyframes ripple
  0%: width 0 height 0 opacity 0.6
  100%: width 80px height 80px opacity 0
```

## 苔藓纹理

```css
background-image:
  radial-gradient(ellipse 3px 2px at 20% 30%, rgba(100,140,80,0.15) 0%, transparent 100%),
  radial-gradient(ellipse 2px 3px at 60% 70%, rgba(80,120,65,0.12) 0%, transparent 100%),
  radial-gradient(ellipse 4px 2px at 80% 20%, rgba(110,150,90,0.1) 0%, transparent 100%),
  radial-gradient(ellipse 2px 2px at 40% 85%, rgba(90,130,70,0.13) 0%, transparent 100%);
background-size: 200px 200px;
background-repeat: repeat;
opacity: 0.6;
```

## 藤蔓装饰线

```css
height: 2px;
background: repeating-linear-gradient(90deg, rgba(45,106,79,0.3) 0px, rgba(45,106,79,0.3) 12px, transparent 12px, transparent 16px);
position: relative;
```

```css
width: 6px;
height: 6px;
border-radius: 50%;
background: rgba(45,106,79,0.3);
position: absolute;
top: -2px;
```

## 叶脉纹理 (卡片/面板装饰)

```css
background-image:
  linear-gradient(135deg, rgba(45,106,79,0.03) 1px, transparent 1px),
  linear-gradient(225deg, rgba(45,106,79,0.03) 1px, transparent 1px);
background-size: 20px 20px;
background-position: 0 0, 10px 10px;
```

## 晨雾效果

```css
background: linear-gradient(180deg, rgba(250,246,240,0) 0%, rgba(250,246,240,0.6) 40%, rgba(250,246,240,0.8) 60%, rgba(250,246,240,0) 100%);
height: 120px;
position: fixed;
bottom: 0;
width: 100%;
pointer-events: none;
z-index: 2;
animation: mistFloat 8s ease-in-out infinite alternate;
```

```
@keyframes mistFloat
  0%: opacity 0.4 translateY(0)
  100%: opacity 0.7 translateY(-10px)
```

## 树影投射

```css
position: fixed;
top: 0;
right: 0;
width: 300px;
height: 100%;
pointer-events: none;
z-index: 0;
opacity: 0.04;
```

## 泥土地面装饰带

```css
background: linear-gradient(0deg, rgba(139,111,71,0.08) 0%, rgba(139,111,71,0.03) 40%, transparent 100%);
height: 80px;
position: fixed;
bottom: 0;
width: 100%;
pointer-events: none;
```