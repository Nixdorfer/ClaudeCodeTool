# Vaporwave Effects

## 透视网格地面

```css
.grid-floor {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 45vh;
  background:
    linear-gradient(var(--grid-color) 1px, transparent 1px),
    linear-gradient(90deg, var(--grid-color) 1px, transparent 1px);
  background-size: 60px 40px;
  transform: perspective(400px) rotateX(60deg);
  transform-origin: bottom center;
  pointer-events: none;
  z-index: 0;
  mask-image: linear-gradient(to top, rgba(0,0,0,0.6), transparent);
  -webkit-mask-image: linear-gradient(to top, rgba(0,0,0,0.6), transparent);
}
```

--grid-color 默认值: rgba(1, 205, 254, 0.3)
background-size 控制网格密度 移动端可增大至 80px 50px
perspective 值越小透视感越强 推荐范围 300-500px
rotateX 推荐范围 55-65deg
mask-image 使网格向远处渐隐

## 日落圆盘

```css
.sunset-sun {
  position: fixed;
  bottom: 25vh;
  left: 50%;
  transform: translateX(-50%);
  width: 250px;
  height: 250px;
  border-radius: 50%;
  background: var(--sun-gradient);
  z-index: 0;
  opacity: 0.5;
  mask-image: repeating-linear-gradient(
    0deg,
    #000 0px, #000 4px,
    transparent 4px, transparent 8px
  );
  -webkit-mask-image: repeating-linear-gradient(
    0deg,
    #000 0px, #000 4px,
    transparent 4px, transparent 8px
  );
}
```

--sun-gradient 默认值: linear-gradient(180deg, #ff8b3a 0%, #ff71ce 50%, #b967ff 100%)
横纹 mask 的 4px/8px 比例可调 数值越小条纹越密
移动端建议 width/height 缩至 150px

## CRT 扫描线

```css
.crt-overlay::after {
  content: '';
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: repeating-linear-gradient(
    0deg,
    transparent,
    transparent 2px,
    rgba(0, 0, 0, 0.08) 2px,
    rgba(0, 0, 0, 0.08) 4px
  );
  pointer-events: none;
  z-index: 9999;
}
```

扫描线透明度 0.05-0.12 之间调节 过高会影响可读性
行高 2px/4px 可调 更密集: 1px/2px

## 色差效果 (Chromatic Aberration)

```css
.chroma-text {
  text-shadow:
    -2px 0 var(--chroma-left),
    2px 0 var(--chroma-right);
}
```

--chroma-left 默认值: rgba(1, 205, 254, 0.6)
--chroma-right 默认值: rgba(255, 113, 206, 0.6)
偏移量 1-3px 过大会影响可读性
仅用于标题或装饰文字 不可用于正文

## 棕榈树剪影

```css
.palm-left,
.palm-right {
  position: fixed;
  bottom: 0;
  width: 200px;
  height: 70vh;
  background-size: contain;
  background-repeat: no-repeat;
  background-position: bottom;
  opacity: 0.18;
  pointer-events: none;
  z-index: 1;
}

.palm-left {
  left: -20px;
  transform: scaleX(-1);
}

.palm-right {
  right: -20px;
}
```

使用纯黑色 SVG 剪影图 通过 opacity 控制
移动端 display: none

## Win95 窗口边框

```css
.win95-window {
  border: 2px solid var(--accent-tertiary);
  box-shadow:
    inset 1px 1px 0 rgba(255, 255, 255, 0.1),
    inset -1px -1px 0 rgba(0, 0, 0, 0.3),
    0 0 40px var(--shadow-modal);
}

.win95-titlebar {
  background: var(--titlebar-gradient);
  padding: 6px 10px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-family: 'Space Mono', monospace;
  font-size: 0.75rem;
  color: #ffffff;
  letter-spacing: 0.05em;
  user-select: none;
}

.win95-btn-group {
  display: flex;
  gap: 3px;
}

.win95-btn {
  width: 18px;
  height: 18px;
  background: var(--bg-primary);
  border: 1px solid #ffffff;
  color: #ffffff;
  font-size: 0.55rem;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  padding: 0;
  line-height: 1;
}
```

## 毛玻璃叠加

```css
.glass-panel {
  background: var(--glass-overlay);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border: 1px solid var(--glass-border);
}
```

blur 范围 8-15px
不支持 backdrop-filter 的浏览器需要更高的背景不透明度作为回退

## 霓虹发光

```css
.neon-glow {
  text-shadow:
    0 0 10px var(--accent-primary),
    0 0 30px var(--accent-primary),
    0 0 60px color-mix(in srgb, var(--accent-primary) 40%, transparent);
}

.neon-box-glow {
  box-shadow:
    0 0 20px var(--shadow-primary),
    0 0 40px var(--shadow-secondary);
}
```

## 渐变分隔线

```css
.vapor-divider {
  height: 2px;
  background: var(--divider-gradient);
  margin: 50px 0;
  border: none;
}
```

## 日文装饰文字层

```css
.jp-deco {
  position: fixed;
  font-family: 'Noto Sans JP', sans-serif;
  color: var(--accent-tertiary);
  opacity: 0.12;
  font-size: 1.2rem;
  letter-spacing: 0.3em;
  writing-mode: vertical-rl;
  pointer-events: none;
  z-index: 1;
  user-select: none;
}
```

常用装饰文字: アエステティック / ヴェイパーウェイヴ / 新しい世界 / 永遠に
