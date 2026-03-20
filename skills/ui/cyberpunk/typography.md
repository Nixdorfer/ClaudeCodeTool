# 排版规范

## 字体栈

用途	字体
英文标题	Orbitron, sans-serif
英文正文	Rajdhani, sans-serif
等宽/数据	Share Tech Mono, monospace
中文回退	Noto Sans SC, Microsoft YaHei, sans-serif

## 字号层级

层级	大小	字重	颜色变量	letter-spacing
Hero标题	clamp(2rem, 6vw, 4.5rem)	900	--color-text-bright	0.1em
页面标题 H1	clamp(1.5rem, 4vw, 2.5rem)	700	--color-text-bright	0.08em
区块标题 H2	1.25rem (20px)	700	--color-text-bright	0.06em
卡片标题 H3	1rem (16px)	600	--color-text-bright	0.04em
正文	0.9rem (14.4px)	400	--color-text	0.02em
标签/说明	0.8rem (12.8px)	400	--color-text-dim	0.02em
小字/辅助	0.75rem (12px)	400	--color-text-dim	0.01em

## 字重使用

字重	数值	使用场景
Black	900	Hero 标题
Bold	700	页面标题 区块标题
Semibold	600	卡片标题 按钮文字
Medium	500	强调正文 导航链接
Regular	400	正文 标签 说明

## 文字处理

所有标题使用 text-transform: uppercase
标题配合 text-shadow 霓虹发光效果 (参见 effects.md)
正文行高 1.6
标题行高 1.2
段落间距 1em

## 等宽字体使用场景

场景	说明
代码块	所有代码显示
数据表格	数字/ID/状态码列
终端输出	命令行/日志显示
计数器/时钟	数字显示
标签/编号	技术标签 序列号

## 间距规范

层级	大小	用途
xs	4px	紧凑元素内间距
sm	8px	标签间距 图标与文字间距
md	12px	卡片内边距 列表项间距
lg	16px	区块内边距 输入框内边距
xl	24px	卡片padding 区块间距
2xl	32px	页面区块间距
3xl	48px	大区块/section间距

## 切角规范 (替代圆角)

组件	切角方式	切角尺寸
按钮小	平行四边形	6px
按钮大	平行四边形	10px
输入框	平行四边形	4px
卡片	六角切角	15px
模态框	六角切角	20px
tooltip	六角切角	8px
徽章/标签	平行四边形	4px
头像/缩略图	六角切角	10px

赛博朋克风格中所有元素禁止使用 border-radius 圆角 统一使用 clip-path 切角

## 文字颜色层次

层次	变量	用途
最亮	--color-text-bright	标题 选中项 高亮文字 配合 text-shadow
标准	--color-text	正文 标签 默认文字
暗淡	--color-text-dim	说明 占位符 次要信息
禁用	--color-text-disabled	不可交互文字
强调	--color-accent	链接 关键数据 交互文字
副强调	--color-accent-secondary	警示 装饰文字
