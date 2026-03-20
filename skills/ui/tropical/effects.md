# Tropical Paradise Effects

## 波浪分区 Wave Divider

```css
.wave-section {
  position: relative;
}

.wave-section::after {
  content: "";
  position: absolute;
  bottom: -2px;
  left: 0;
  width: 100%;
  height: 60px;
  background: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1440 60'%3E%3Cpath fill='%23fdf8f0' d='M0,30 C360,60 720,0 1080,30 C1260,45 1350,20 1440,30 L1440,60 L0,60Z'/%3E%3C/svg%3E");
  background-size: cover;
}

.wave-top::before {
  content: "";
  position: absolute;
  top: -2px;
  left: 0;
  width: 100%;
  height: 60px;
  background: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1440 60'%3E%3Cpath fill='%23fdf8f0' d='M0,30 C360,0 720,60 1080,30 C1260,15 1350,40 1440,30 L1440,0 L0,0Z'/%3E%3C/svg%3E");
  background-size: cover;
}
```

| 参数 | 值 |
|------|------|
| wave-height | 60px |
| wave-color | 使用 var(--bg-sand) 替换 SVG fill |
| wave-complexity | 2-3 curves per 1440px |

## 棕榈树剪影 Palm Silhouette

```css
.palm-decoration {
  position: absolute;
  width: 120px;
  height: 200px;
  background: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 120 200'%3E%3Cpath d='M60 200 L60 80 Q30 40 10 20 Q40 50 60 60 Q35 20 25 0 Q50 35 60 55 Q70 20 90 0 Q75 40 60 60 Q85 45 110 20 Q80 50 60 80Z' fill='%230d4730' opacity='0.1'/%3E%3C/svg%3E") no-repeat center;
  background-size: contain;
  pointer-events: none;
}
```

| 参数 | 值 |
|------|------|
| palm-width | 80-200px |
| palm-opacity | 0.05-0.15 |
| palm-color | var(--text-heading) 低不透明度 |

## 日落渐变 Sunset Gradient

```css
.sunset-gradient {
  background: linear-gradient(
    180deg,
    rgba(255, 182, 130, 0.3) 0%,
    rgba(255, 140, 90, 0.15) 30%,
    rgba(253, 245, 230, 0) 60%
  );
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 400px;
  pointer-events: none;
}
```

| 参数 | 值 |
|------|------|
| gradient-height | 300-500px |
| start-opacity | 0.2-0.4 |
| mid-opacity | 0.1-0.2 |

## 水面反光 Water Reflection

```css
.water-reflection {
  position: relative;
  overflow: hidden;
}

.water-reflection::after {
  content: "";
  position: absolute;
  top: 0;
  left: -50%;
  width: 200%;
  height: 100%;
  background: linear-gradient(
    90deg,
    transparent 0%,
    rgba(255, 255, 255, 0.08) 45%,
    rgba(255, 255, 255, 0.15) 50%,
    rgba(255, 255, 255, 0.08) 55%,
    transparent 100%
  );
  animation: waterShimmer 3s ease-in-out infinite;
}

@keyframes waterShimmer {
  0% { transform: translateX(-30%); }
  100% { transform: translateX(30%); }
}
```

| 参数 | 值 |
|------|------|
| shimmer-duration | 3s |
| shimmer-opacity | 0.08-0.15 |
| shimmer-width | 10% of total |

## 沙滩纹理 Sand Texture

```css
.sand-texture {
  background-image: url("data:image/svg+xml,%3Csvg width='40' height='40' xmlns='http://www.w3.org/2000/svg'%3E%3Ccircle cx='10' cy='10' r='0.5' fill='%23d4b896' opacity='0.3'/%3E%3Ccircle cx='30' cy='25' r='0.4' fill='%23d4b896' opacity='0.2'/%3E%3Ccircle cx='20' cy='35' r='0.6' fill='%23d4b896' opacity='0.25'/%3E%3C/svg%3E");
  background-size: 40px 40px;
}
```

| 参数 | 值 |
|------|------|
| grain-size | 0.3-0.8px |
| grain-opacity | 0.15-0.3 |
| tile-size | 40px |

## 贝壳装饰 Shell Decoration

```css
.shell-accent {
  position: relative;
}

.shell-accent::before {
  content: "";
  position: absolute;
  width: 24px;
  height: 24px;
  background: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23ff6b4a' stroke-width='1.5'%3E%3Cpath d='M12 22C12 22 4 16 4 10C4 6 8 2 12 2C16 2 20 6 20 10C20 16 12 22 12 22Z'/%3E%3Cpath d='M12 2v20M4 10h16'/%3E%3C/svg%3E") no-repeat center;
  background-size: contain;
  opacity: 0.3;
}
```

| 参数 | 值 |
|------|------|
| shell-size | 16-32px |
| shell-color | var(--accent-primary) |
| shell-opacity | 0.2-0.4 |

## 热带花卉边框 Floral Border

```css
.floral-border {
  border-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='100' height='20'%3E%3Ccircle cx='10' cy='10' r='4' fill='%23f472b6' opacity='0.3'/%3E%3Ccircle cx='30' cy='10' r='3' fill='%23ff6b4a' opacity='0.2'/%3E%3Ccircle cx='50' cy='10' r='4' fill='%2316a34a' opacity='0.25'/%3E%3Ccircle cx='70' cy='10' r='3' fill='%23facc15' opacity='0.2'/%3E%3Ccircle cx='90' cy='10' r='4' fill='%230ea5e9' opacity='0.3'/%3E%3C/svg%3E") 20 round;
  border-width: 0 0 4px 0;
  border-style: solid;
}
```

| 参数 | 值 |
|------|------|
| border-width | 3-6px |
| pattern-repeat | round |
| flower-opacity | 0.2-0.35 |

## 卡片彩虹顶边 Rainbow Top

```css
.rainbow-top::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 4px;
  background: linear-gradient(
    90deg,
    var(--accent-primary),
    var(--accent-highlight),
    var(--accent-tertiary),
    var(--accent-quaternary)
  );
}
```

| 参数 | 值 |
|------|------|
| stripe-height | 3-5px |
| gradient-stops | 4 accent colors |
