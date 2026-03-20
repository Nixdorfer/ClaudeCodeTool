# Steampunk Effects

## 金属纹理

金属渐变-黄铜:
```css
background: linear-gradient(180deg, #c8a032 0%, #8b6914 100%);
```

金属渐变-红铜:
```css
background: linear-gradient(135deg, #b87333 0%, #8b5a2b 50%, #cd853f 100%);
```

金属光泽叠加:
```css
background: linear-gradient(
  135deg,
  rgba(255, 255, 255, 0.15) 0%,
  transparent 40%,
  transparent 60%,
  rgba(255, 255, 255, 0.08) 100%
);
```

拉丝金属纹理:
```css
background-image: repeating-linear-gradient(
  90deg,
  rgba(200, 160, 50, 0.03) 0px,
  transparent 1px,
  transparent 3px
);
```

做旧羊皮纸纹理:
```css
background-image:
  radial-gradient(ellipse at 20% 50%, rgba(42, 31, 14, 0.4) 0%, transparent 50%),
  radial-gradient(ellipse at 80% 20%, rgba(42, 31, 14, 0.3) 0%, transparent 40%),
  radial-gradient(ellipse at 50% 80%, rgba(42, 31, 14, 0.35) 0%, transparent 45%);
```

## 齿轮旋转装饰

单齿轮:
```css
.gear {
  display: inline-block;
  animation: gear-spin 15s linear infinite;
  color: rgba(184, 115, 51, 0.6);
  font-size: 2rem;
}

@keyframes gear-spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}
```

反向齿轮 (咬合效果):
```css
.gear-reverse {
  animation: gear-spin 12s linear infinite reverse;
  color: rgba(200, 160, 50, 0.5);
}
```

齿轮组装饰 (容器角落):
```css
.gear-corner::before {
  content: "\2699";
  position: absolute;
  top: -10px;
  right: -10px;
  font-size: 1.4rem;
  color: rgba(200, 160, 50, 0.4);
  animation: gear-spin 20s linear infinite;
}

.gear-corner::after {
  content: "\2699";
  position: absolute;
  bottom: -8px;
  left: -8px;
  font-size: 1rem;
  color: rgba(184, 115, 51, 0.35);
  animation: gear-spin 14s linear infinite reverse;
}
```

## 铆钉边框

单边铆钉 (顶部):
```css
.riveted-top {
  position: relative;
  border-top: 3px solid rgba(184, 115, 51, 0.6);
}

.riveted-top::before {
  content: "\25CF \25CF \25CF \25CF \25CF \25CF \25CF \25CF \25CF \25CF";
  position: absolute;
  top: -8px;
  left: 0;
  right: 0;
  text-align: center;
  font-size: 5px;
  letter-spacing: 12px;
  color: rgba(219, 184, 80, 0.7);
}
```

四边铆钉:
```css
.riveted {
  border: 2px solid rgba(184, 115, 51, 0.5);
  box-shadow:
    inset 4px 4px 0 -2px rgba(219, 184, 80, 0.15),
    inset -4px -4px 0 -2px rgba(0, 0, 0, 0.2);
  background-image:
    radial-gradient(circle at 8px 8px, rgba(219, 184, 80, 0.5) 2px, transparent 2px),
    radial-gradient(circle at calc(100% - 8px) 8px, rgba(219, 184, 80, 0.5) 2px, transparent 2px),
    radial-gradient(circle at 8px calc(100% - 8px), rgba(219, 184, 80, 0.5) 2px, transparent 2px),
    radial-gradient(circle at calc(100% - 8px) calc(100% - 8px), rgba(219, 184, 80, 0.5) 2px, transparent 2px);
  background-repeat: no-repeat;
}
```

## 蒸汽烟雾效果

蒸汽粒子:
```css
.steam-particle {
  position: absolute;
  width: 20px;
  height: 20px;
  background: radial-gradient(circle, rgba(232, 220, 200, 0.3), transparent);
  border-radius: 50%;
  animation: steam-rise 3s ease-out infinite;
  pointer-events: none;
}

@keyframes steam-rise {
  0% {
    opacity: 0;
    transform: translateY(0) scale(1);
  }
  30% {
    opacity: 0.4;
  }
  100% {
    opacity: 0;
    transform: translateY(-80px) scale(2.5);
  }
}
```

蒸汽粒子延迟序列:
```css
.steam-particle:nth-child(1) { left: 20%; animation-delay: 0s; }
.steam-particle:nth-child(2) { left: 40%; animation-delay: 0.8s; }
.steam-particle:nth-child(3) { left: 60%; animation-delay: 1.6s; }
.steam-particle:nth-child(4) { left: 80%; animation-delay: 0.4s; }
.steam-particle:nth-child(5) { left: 50%; animation-delay: 1.2s; }
```

环境蒸汽 (大面积背景):
```css
.ambient-steam {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  height: 200px;
  background: linear-gradient(to top, rgba(232, 220, 200, 0.05), transparent);
  pointer-events: none;
  z-index: 0;
  animation: ambient-steam-pulse 8s ease-in-out infinite;
}

@keyframes ambient-steam-pulse {
  0%, 100% { opacity: 0.3; }
  50% { opacity: 0.7; }
}
```

## 压力表

表盘容器:
```css
.gauge {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 3px solid rgba(184, 115, 51, 0.7);
  background: radial-gradient(circle, rgba(42, 31, 14, 0.9), rgba(26, 18, 9, 1));
  position: relative;
  box-shadow:
    inset 0 0 15px rgba(0, 0, 0, 0.5),
    0 0 8px rgba(200, 160, 50, 0.15);
}
```

表盘刻度 (conic-gradient):
```css
.gauge::before {
  content: "";
  position: absolute;
  inset: 4px;
  border-radius: 50%;
  background: conic-gradient(
    from 210deg,
    rgba(200, 160, 50, 0.6) 0deg,
    rgba(200, 160, 50, 0.6) 2deg,
    transparent 2deg,
    transparent 24deg,
    rgba(200, 160, 50, 0.6) 24deg,
    rgba(200, 160, 50, 0.6) 26deg,
    transparent 26deg,
    transparent 48deg,
    rgba(200, 160, 50, 0.6) 48deg,
    rgba(200, 160, 50, 0.6) 50deg,
    transparent 50deg
  );
  mask: radial-gradient(circle, transparent 55%, black 56%);
  -webkit-mask: radial-gradient(circle, transparent 55%, black 56%);
}
```

指针:
```css
.gauge-needle {
  position: absolute;
  bottom: 50%;
  left: 50%;
  width: 2px;
  height: 30px;
  background: rgba(200, 160, 50, 0.9);
  transform-origin: bottom center;
  transform: translateX(-50%) rotate(var(--gauge-value, -60deg));
  transition: transform 1.5s cubic-bezier(0.34, 1.56, 0.64, 1);
  border-radius: 1px 1px 0 0;
}
```

指针轴心:
```css
.gauge-needle::after {
  content: "";
  position: absolute;
  bottom: -4px;
  left: 50%;
  transform: translateX(-50%);
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(219, 184, 80, 1), rgba(139, 105, 20, 1));
  border: 1px solid rgba(219, 184, 80, 0.5);
}
```

## 管道装饰线

水平管道:
```css
.pipe-horizontal {
  height: 8px;
  background: linear-gradient(
    180deg,
    rgba(184, 115, 51, 0.5) 0%,
    rgba(139, 90, 43, 0.7) 40%,
    rgba(100, 65, 30, 0.7) 60%,
    rgba(184, 115, 51, 0.4) 100%
  );
  border-radius: 4px;
  position: relative;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
}
```

管道接头:
```css
.pipe-joint {
  width: 16px;
  height: 14px;
  background: linear-gradient(
    180deg,
    rgba(200, 160, 50, 0.6) 0%,
    rgba(139, 105, 20, 0.7) 50%,
    rgba(200, 160, 50, 0.5) 100%
  );
  border-radius: 2px;
  border: 1px solid rgba(200, 160, 50, 0.4);
}
```

垂直管道:
```css
.pipe-vertical {
  width: 8px;
  background: linear-gradient(
    90deg,
    rgba(184, 115, 51, 0.5) 0%,
    rgba(139, 90, 43, 0.7) 40%,
    rgba(100, 65, 30, 0.7) 60%,
    rgba(184, 115, 51, 0.4) 100%
  );
  border-radius: 4px;
  box-shadow: 2px 0 4px rgba(0, 0, 0, 0.3);
}
```

## 维多利亚花饰分隔线

```css
.divider-ornate {
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 40px 0;
  gap: 15px;
  color: rgba(184, 115, 51, 0.7);
}

.divider-ornate::before,
.divider-ornate::after {
  content: "";
  flex: 1;
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(184, 115, 51, 0.5), transparent);
}
```

## 暗角效果 (做旧边缘)

```css
.vignette::before {
  content: "";
  position: fixed;
  inset: 0;
  background: radial-gradient(
    ellipse at center,
    transparent 40%,
    rgba(0, 0, 0, 0.4) 80%,
    rgba(0, 0, 0, 0.7) 100%
  );
  pointer-events: none;
  z-index: 9999;
}
```

## 内发光 (金属容器)

```css
.metal-inset {
  box-shadow:
    inset 0 1px 0 rgba(255, 255, 255, 0.08),
    inset 0 -1px 0 rgba(0, 0, 0, 0.3),
    0 4px 12px rgba(0, 0, 0, 0.3);
}
```

## Double Border (维多利亚边框)

```css
.victorian-border {
  border: 3px double rgba(200, 160, 50, 0.6);
  outline: 1px solid rgba(184, 115, 51, 0.2);
  outline-offset: 4px;
}
```
