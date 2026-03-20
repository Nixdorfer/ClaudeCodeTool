# Tropical Paradise Base

## 风格定义

热带度假风 椰林树影 碧海蓝天 浓烈色彩在阳光下绽放 永远处于黄金时刻的度假天堂
灵感来源 热带旅行海报 Tiki文化 冲浪品牌 巴厘岛/夏威夷明信片

## 页面

```css
body {
  background: linear-gradient(180deg, var(--bg-sky) 0%, var(--bg-sand) 30%, var(--bg-sand) 100%);
  color: var(--text-primary);
  font-family: 'Nunito', 'Noto Sans SC', sans-serif;
  line-height: 1.7;
  min-height: 100vh;
  overflow-x: hidden;
}

html {
  scroll-behavior: smooth;
}

*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

::selection {
  background: var(--accent-primary);
  color: #ffffff;
}
```

## 字体加载

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Pacifico&family=Leckerli+One&family=Josefin+Sans:wght@400;600;700&family=Nunito:wght@400;600;700;800&display=swap" rel="stylesheet">
```

| 用途 | 字体 | 回退 |
|------|------|------|
| 标题/品牌 | Pacifico / Leckerli One | cursive |
| 副标题/标签/按钮 | Josefin Sans | sans-serif |
| 正文 | Nunito | Noto Sans SC, sans-serif |

## 图标

热带线条风图标 推荐 Phosphor Icons 或 Lucide 的 outline 变体

| 场景 | 尺寸 | 线宽 |
|------|------|------|
| 导航 | 20px | 1.5px |
| 按钮内嵌 | 18px | 1.5px |
| 卡片图标 | 24px | 2px |
| 空状态/装饰 | 48px | 1.5px |

推荐图标 palm-tree sun waves fish umbrella-beach shell flower-lotus cocktail flamingo

## 按钮

```css
.btn {
  font-family: 'Josefin Sans', sans-serif;
  font-size: 0.95rem;
  font-weight: 700;
  border-radius: 50px;
  cursor: pointer;
  transition: all 0.3s ease;
  border: none;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  text-decoration: none;
  white-space: nowrap;
}

.btn-lg { padding: 14px 36px; font-size: 0.95rem; }
.btn-md { padding: 10px 24px; font-size: 0.85rem; }
.btn-sm { padding: 6px 16px; font-size: 0.75rem; }

.btn-primary {
  background: linear-gradient(135deg, var(--btn-primary-bg-from), var(--btn-primary-bg-to));
  color: var(--btn-primary-text);
  box-shadow: var(--shadow-btn);
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-btn-hover);
  background: linear-gradient(135deg, var(--btn-primary-hover-from), var(--btn-primary-hover-to));
}

.btn-primary:active {
  transform: translateY(0);
  background: linear-gradient(135deg, var(--btn-primary-active-from), var(--btn-primary-active-to));
}

.btn-primary:disabled {
  opacity: 0.5;
  cursor: not-allowed;
  transform: none;
  background: var(--btn-primary-disabled);
}

.btn-secondary {
  background: var(--glass-bg);
  color: var(--accent-tertiary);
  border: 2px solid var(--accent-tertiary);
}

.btn-secondary:hover {
  background: var(--accent-tertiary);
  color: #ffffff;
}

.btn-ghost {
  background: transparent;
  color: var(--text-primary);
  padding: 10px 16px;
}

.btn-ghost:hover {
  background: var(--glass-bg);
}
```

## Modal

```css
.modal-overlay {
  position: fixed;
  inset: 0;
  background: var(--glass-overlay);
  backdrop-filter: blur(6px);
  z-index: 1000;
  display: flex;
  align-items: center;
  justify-content: center;
}

.modal-content {
  background: var(--bg-surface);
  border-radius: 20px;
  padding: 40px;
  max-width: 460px;
  width: 90%;
  box-shadow: var(--shadow-xl);
  position: relative;
  border-top: 4px solid var(--accent-tertiary);
}

.modal-content::before {
  content: '';
  position: absolute;
  top: -18px;
  left: 50%;
  transform: translateX(-50%);
  width: 36px;
  height: 36px;
  background: var(--bg-surface) url("data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 24 24%27 fill=%27none%27 stroke=%27%2316a34a%27 stroke-width=%272%27%3E%3Cpath d=%27M12 2c-4 4-8 6-8 10s4 8 8 4c4 4 8 0 8-4s-4-6-8-10z%27/%3E%3C/svg%3E") center/24px no-repeat;
  border-radius: 50%;
}

.modal-close {
  position: absolute;
  top: 14px;
  right: 14px;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: var(--glass-bg);
  border: none;
  color: var(--accent-tertiary);
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  justify-content: center;
}

.modal-close:hover {
  background: var(--glass-bg-hover);
}

.modal-title {
  font-family: 'Pacifico', cursive;
  font-size: 1.5rem;
  color: var(--text-heading);
  margin-bottom: 16px;
}

.modal-body {
  color: var(--text-primary);
  font-size: 0.95rem;
  line-height: 1.7;
}

.modal-footer {
  display: flex;
  gap: 12px;
  justify-content: flex-end;
  margin-top: 24px;
}
```

## 滚动条

```css
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: var(--scrollbar-track); }
::-webkit-scrollbar-thumb { background: var(--scrollbar-thumb); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: var(--scrollbar-thumb-hover); }
```

## 卡片

```css
.card {
  background: var(--bg-surface);
  border-radius: 16px;
  padding: 28px;
  box-shadow: var(--shadow-md);
  transition: all 0.3s ease;
  overflow: hidden;
  position: relative;
}

.card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-lg);
}

.card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 4px;
  background: linear-gradient(90deg, var(--accent-primary), var(--accent-highlight), var(--accent-tertiary), var(--accent-quaternary));
}
```

## 导航栏

```css
.navbar {
  position: fixed;
  top: 0;
  width: 100%;
  padding: 12px 32px;
  background: var(--glass-navbar);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--border-light);
  display: flex;
  justify-content: space-between;
  align-items: center;
  z-index: 100;
}

.nav-brand {
  font-family: 'Pacifico', cursive;
  color: var(--text-heading);
  font-size: 1.3rem;
}

.nav-link {
  color: var(--text-primary);
  text-decoration: none;
  font-family: 'Josefin Sans', sans-serif;
  font-weight: 600;
  font-size: 0.85rem;
  transition: color 0.3s;
}

.nav-link:hover { color: var(--accent-primary); }
```

## 输入框

```css
.input-field {
  background: var(--input-bg);
  border: 2px solid var(--input-border);
  color: var(--input-text);
  padding: 12px 18px;
  font-family: 'Nunito', sans-serif;
  font-size: 0.95rem;
  width: 100%;
  border-radius: 12px;
  transition: all 0.3s;
  outline: none;
}

.input-field::placeholder { color: var(--input-placeholder); }

.input-field:focus {
  border-color: var(--input-focus-border);
  box-shadow: var(--input-focus-shadow);
}

.input-field:disabled {
  background: var(--input-disabled-bg);
  color: var(--input-disabled-text);
  cursor: not-allowed;
}

.input-field.error { border-color: var(--state-error); }

.input-label {
  font-family: 'Josefin Sans', sans-serif;
  font-size: 0.8rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--text-secondary);
  margin-bottom: 6px;
  display: block;
}
```

## 分隔线

```css
.divider {
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 50px 0;
  gap: 12px;
}

.divider::before,
.divider::after {
  content: '';
  flex: 1;
  max-width: 120px;
  height: 2px;
  background: linear-gradient(90deg, transparent, var(--accent-tertiary), transparent);
}
```

## 标签

```css
.tag {
  font-family: 'Josefin Sans', sans-serif;
  font-size: 0.7rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: var(--accent-primary);
  background: var(--glass-tag);
  padding: 4px 12px;
  border-radius: 20px;
  display: inline-block;
}
```

## 设计原则

1. 色彩大胆鲜艳 高饱和度
2. 圆角 12-20px 柔和友好
3. 波浪曲线是核心装饰元素
4. 渐变温暖 从海到天 从日出到黄昏
5. 字体活泼 手写体标题 + 圆润无衬线正文
6. 所有颜色通过 CSS 变量引用 不硬编码
