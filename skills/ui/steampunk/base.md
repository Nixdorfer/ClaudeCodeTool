# Steampunk Base

## 核心特征

风格定位: 维多利亚时代工业革命美学 黄铜齿轮与蒸汽管道的复古未来世界
视觉基调: 暗褐背景 黄铜金属质感 铆钉装饰 做旧羊皮纸纹理 煤油灯暖光氛围
关键元素: 齿轮 铆钉 蒸汽管道 压力表 皮革纹理 维多利亚花饰

## 页面

```css
body {
  background-color: #1a1209;
  background-image: radial-gradient(ellipse at center, #2a1f0e 0%, #1a1209 70%);
  min-height: 100vh;
  overflow-x: hidden;
}

body::before {
  content: '';
  position: fixed;
  inset: 0;
  background: radial-gradient(ellipse at center, transparent 50%, rgba(0, 0, 0, 0.6) 100%);
  pointer-events: none;
  z-index: 0;
}
```

## 字体

标题字体: `"Cinzel Decorative", "Playfair Display", "Noto Serif SC", "SimSun", serif`
正文字体: `"Crimson Text", "EB Garamond", "Noto Serif SC", "SimSun", serif`
等宽字体: `"Special Elite", "Courier New", monospace`
数字/仪表字体: `"Special Elite", monospace`

Google Fonts 导入:
```
Cinzel+Decorative:wght@400;700;900
Playfair+Display:wght@400;600;700
Crimson+Text:wght@400;600;700
EB+Garamond:wght@400;500;600;700
Special+Elite
```

## 图标

图标风格: 线性描边 圆角端点 黄铜金色
推荐图标库: Lucide 或 Phosphor (regular weight)
图标默认尺寸: 20px
图标颜色: rgba(200, 160, 50, 0.85)
装饰性 Unicode 符号: ⚙ ⚡ ⛭ ☸ ✦ ◆ ●

## 按钮形状

```css
.btn {
  padding: 12px 32px;
  border-radius: 4px;
  font-family: 'Cinzel Decorative', serif;
  font-size: 0.85rem;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  cursor: pointer;
  position: relative;
  transition: all 0.3s ease;
}
```

铆钉装饰 (伪元素):
```css
.btn::before,
.btn::after {
  content: '●';
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  font-size: 6px;
  color: rgba(219, 184, 80, 0.8);
}

.btn::before { left: 8px; }
.btn::after { right: 8px; }
```

按钮圆角: 4px
按钮最小高度: 44px
按钮内边距: 12px 32px (大) / 8px 20px (中) / 6px 14px (小)

## Modal

```css
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(10, 8, 3, 0.92);
  z-index: 1000;
  display: flex;
  align-items: center;
  justify-content: center;
  backdrop-filter: blur(4px);
}

.modal-content {
  background: linear-gradient(135deg, #2a1f0e, #1a1209);
  border: 3px double rgba(200, 160, 50, 0.7);
  padding: 40px;
  max-width: 560px;
  width: 90%;
  position: relative;
  box-shadow: 0 0 40px rgba(200, 160, 50, 0.1), inset 0 0 60px rgba(0, 0, 0, 0.3);
  border-radius: 6px;
}

.modal-content::before {
  content: '⚙';
  position: absolute;
  top: -15px;
  left: 50%;
  transform: translateX(-50%);
  font-size: 1.8rem;
  color: rgba(200, 160, 50, 0.9);
  background: #1a1209;
  padding: 0 12px;
}
```

Modal 圆角: 6px
Modal 最大宽度: 560px
Modal 内边距: 40px
Modal 边框: 3px double

## 滚动条

```css
::-webkit-scrollbar {
  width: 8px;
  height: 8px;
}

::-webkit-scrollbar-track {
  background: #1a1209;
  border-left: 1px solid rgba(184, 115, 51, 0.2);
}

::-webkit-scrollbar-thumb {
  background: linear-gradient(180deg, #c8a032, #8b6914);
  border-radius: 4px;
  border: 1px solid rgba(219, 184, 80, 0.3);
}

::-webkit-scrollbar-thumb:hover {
  background: linear-gradient(180deg, #dbb850, #a07818);
}

::-webkit-scrollbar-corner {
  background: #1a1209;
}
```

Firefox 滚动条:
```css
* {
  scrollbar-width: thin;
  scrollbar-color: #c8a032 #1a1209;
}
```

## 通用圆角体系

无圆角(铆钉/徽章): 0px
小圆角(按钮/输入框/标签): 4px
中圆角(卡片/Modal): 6px
大圆角(头像/特殊容器): 8px

## 间距体系

基础单位: 4px
xs: 4px
sm: 8px
md: 16px
lg: 24px
xl: 32px
xxl: 48px
