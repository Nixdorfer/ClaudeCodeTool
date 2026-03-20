# 武侠水墨风 排版规范

## 字体族

标题字体: Ma Shan Zheng, ZCOOL XiaoWei, cursive
正文字体: Noto Serif SC, SimSun, STSong, serif
英文字体: Noto Serif, serif
Google Fonts 引入: Ma Shan Zheng, ZCOOL XiaoWei, Noto Serif SC

## 字号体系

| 级别 | 尺寸 | 用途 |
|------|------|------|
| display | clamp(2.5rem, 7vw, 5rem) | 主标题/英雄区 |
| h1 | clamp(2rem, 5vw, 3rem) | 页面标题 |
| h2 | clamp(1.5rem, 3.5vw, 2.2rem) | 章节标题 |
| h3 | clamp(1.2rem, 2.5vw, 1.6rem) | 小节标题 |
| h4 | 1.15rem | 段落标题 |
| body | 1rem (16px) | 正文 |
| small | 0.875rem | 辅助文字 |
| caption | 0.75rem | 标注/脚注 |

## 字重

- 标题: 400 (书法字体本身无需加粗)
- 正文: 400
- 强调文字: 600
- 辅助文字: 400

## 竖排模式

适用于装饰性文字/侧边标注/诗词展示

- writing-mode: vertical-rl
- text-orientation: mixed
- letter-spacing: 0.25em-0.35em
- 字体: 书法字体
- 行距调整: line-height 与水平模式不同 建议 1.6-1.8

## 文字颜色层级

| 层级 | 用途 | 不透明度参考 |
|------|------|-------------|
| primary | 标题 | 100% |
| secondary | 正文 | 降低明度或使用专色 |
| tertiary | 次要说明 | 约 60% 视觉权重 |
| placeholder | 占位符/禁用 | 约 40% 视觉权重 |
| accent | 链接/强调 | 使用强调色 |
| inverse | 深色背景上的文字 | 使用反色文字 |

## 间距

### 字间距 (letter-spacing)
- display: 0.15em-0.2em
- h1: 0.12em-0.15em
- h2: 0.1em-0.12em
- h3: 0.08em-0.1em
- body: 0.02em-0.04em
- 竖排: 0.25em-0.35em

### 行高 (line-height)
- 标题: 1.3-1.5
- 正文: 1.8-2.0
- 紧凑: 1.5-1.6

### 段落间距
- 段落间: 1.2em-1.5em
- 标题与段落: 0.6em-0.8em
- 章节间: 2em-3em

## 圆角

极小或无圆角 保持方正古朴

| 元素 | 圆角 |
|------|------|
| 按钮 | 0-2px |
| 卡片 | 0 |
| 输入框 | 0 |
| modal | 0 |
| 印章 | 2px-4px |
| 头像 | 0 (方形) 或 50% (圆形印章) |
| 标签 | 0-2px |
| 滚动条滑块 | 3px |

## 标题装饰

- 章节标题两侧加装饰线 使用强调色
- display 标题可配印章组件
- 标题下方可加水墨分隔线
- 标题字体统一使用书法字体

## 文字特效

墨色渐变文字:
- background: linear-gradient(180deg, titleColor 0%, lighterColor 100%)
- -webkit-background-clip: text
- -webkit-text-fill-color: transparent

文字阴影 (谨慎使用):
- text-shadow: 1px 1px 2px rgba(0,0,0,0.1)
- 仅用于 display 级别标题

## 对齐

- 标题: 居中 text-align center
- 正文: 两端对齐 text-align justify
- 诗词/引用: 居中或竖排
- 导航: 均匀分布