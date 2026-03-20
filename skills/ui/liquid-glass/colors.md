# 配色体系

## 主题 1 暗色黑绿 (默认)

### 背景层

元素	变量	rgba
页面底层	--color-bg	rgba(5,5,5,1)
表面/侧边栏底色	--color-surface	rgba(17,17,17,1)
模态框底色	--color-modal	rgba(34,34,34,1)
下拉菜单底色	--color-dropdown	rgba(28,28,28,1)
tooltip底色	--color-tooltip	rgba(40,40,40,1)

### 玻璃叠加层

元素	背景rgba	边框rgba
侧边栏	rgba(17,17,17,0.6)	rgba(255,255,255,0.06)
顶栏	rgba(17,17,17,0.5)	rgba(255,255,255,0.06)
卡片	rgba(255,255,255,0.04)	rgba(255,255,255,0.08)
输入框	rgba(255,255,255,0.05)	rgba(255,255,255,0.1)
按钮(默认)	rgba(22,109,59,0.3)	rgba(22,109,59,0.3)
按钮(悬停)	rgba(26,133,72,0.4)	rgba(26,133,72,0.4)
按钮(按下)	rgba(22,109,59,0.5)	rgba(22,109,59,0.5)
按钮(禁用)	rgba(22,109,59,0.1)	rgba(22,109,59,0.1)
AI气泡	rgba(255,255,255,0.05)	rgba(255,255,255,0.08)
用户气泡	rgba(22,109,59,0.35)	rgba(22,109,59,0.3)
下拉菜单	rgba(28,28,28,0.85)	rgba(255,255,255,0.08)
tooltip	rgba(40,40,40,0.9)	rgba(255,255,255,0.1)

### 文字

元素	变量	rgba
主文字 正文/标签	--color-text	rgba(183,183,183,1)
暗文字 说明/占位符	--color-text-dim	rgba(119,119,119,1)
亮文字 标题/选中项	--color-text-bright	rgba(224,224,224,1)
禁用文字	--color-text-disabled	rgba(85,85,85,1)
链接文字	--color-text-link	rgba(22,109,59,1)
链接悬停	--color-text-link-hover	rgba(26,133,72,1)

### 强调色

元素	变量	rgba
强调默认 按钮/选中滑块/图标高亮	--color-accent	rgba(22,109,59,1)
强调悬停 按钮hover/滑块hover	--color-accent-hover	rgba(26,133,72,1)
强调按下 按钮active	--color-accent-active	rgba(18,90,48,1)
强调淡色 标签背景/选中行	--color-accent-dim	rgba(22,109,59,0.15)
强调光晕 focus-ring/脉冲动画	--color-accent-glow	rgba(22,109,59,0.4)

### 边框

元素	变量	rgba
默认边框 卡片/分割线	--color-border	rgba(51,51,51,1)
悬停边框 卡片hover/输入框hover	--color-border-hover	rgba(68,68,68,1)
聚焦边框 输入框focus	--color-border-focus	rgba(22,109,59,0.6)
淡边框 表格行/列表分割	--color-border-dim	rgba(255,255,255,0.04)

### 状态色

元素	变量	rgba	用途
危险	--color-danger	rgba(220,38,38,1)	删除按钮/错误提示/必填标记
危险淡色	--color-danger-dim	rgba(220,38,38,0.15)	错误背景/危险toast
成功	--color-success	rgba(22,163,74,1)	成功提示/完成图标
成功淡色	--color-success-dim	rgba(22,163,74,0.15)	成功背景/成功toast
警告	--color-warning	rgba(234,179,8,1)	警告图标/注意提示
警告淡色	--color-warning-dim	rgba(234,179,8,0.15)	警告背景/警告toast
信息	--color-info	rgba(59,130,246,1)	帮助图标/信息提示
信息淡色	--color-info-dim	rgba(59,130,246,0.15)	信息背景/信息toast

### 输入组件

元素	rgba
输入框背景	rgba(255,255,255,0.05)
输入框边框 默认	rgba(255,255,255,0.1)
输入框边框 悬停	rgba(255,255,255,0.15)
输入框边框 聚焦	rgba(22,109,59,0.6)
输入框占位符	rgba(119,119,119,1)
选择框选中项背景	rgba(22,109,59,0.2)
滑块轨道	rgba(255,255,255,0.08)
滑块填充	rgba(22,109,59,1)
滑块旋钮	rgba(224,224,224,1)

### 滚动条

元素	rgba
轨道	rgba(0,0,0,0)
滑块 默认	rgba(255,255,255,0.1)
滑块 悬停	rgba(255,255,255,0.2)

### 阴影

元素	值
卡片阴影	0 2px 8px rgba(0,0,0,0.3)
模态框阴影	0 8px 32px rgba(0,0,0,0.5)
下拉菜单阴影	0 4px 16px rgba(0,0,0,0.4)
按钮发光(hover)	0 0 12px rgba(22,109,59,0.3)

---

## 主题 2 亮色白底蓝白

### 背景层

元素	变量	rgba
页面底层	--color-bg	rgba(245,247,250,1)
表面色	--color-surface	rgba(255,255,255,1)
模态框底色	--color-modal	rgba(255,255,255,1)
下拉菜单底色	--color-dropdown	rgba(255,255,255,1)
tooltip底色	--color-tooltip	rgba(30,30,50,0.9)

### 玻璃叠加层

元素	背景rgba	边框rgba
侧边栏	rgba(255,255,255,0.7)	rgba(0,0,0,0.06)
顶栏	rgba(255,255,255,0.6)	rgba(0,0,0,0.06)
卡片	rgba(255,255,255,0.8)	rgba(0,0,0,0.08)
输入框	rgba(255,255,255,0.9)	rgba(0,0,0,0.1)
按钮(默认)	rgba(74,105,189,0.9)	rgba(74,105,189,0.3)
按钮(悬停)	rgba(60,88,165,1)	rgba(60,88,165,0.4)
按钮(按下)	rgba(50,75,145,1)	rgba(50,75,145,0.5)
按钮(禁用)	rgba(74,105,189,0.3)	rgba(74,105,189,0.1)
AI气泡	rgba(245,247,250,0.9)	rgba(0,0,0,0.06)
用户气泡	rgba(74,105,189,0.1)	rgba(74,105,189,0.15)
下拉菜单	rgba(255,255,255,0.95)	rgba(0,0,0,0.08)
tooltip	rgba(30,30,50,0.9)	rgba(255,255,255,0.1)

### 文字

元素	变量	rgba
主文字	--color-text	rgba(26,26,46,0.85)
暗文字	--color-text-dim	rgba(26,26,46,0.5)
亮文字	--color-text-bright	rgba(26,26,46,1)
禁用文字	--color-text-disabled	rgba(26,26,46,0.3)
链接文字	--color-text-link	rgba(74,105,189,1)
链接悬停	--color-text-link-hover	rgba(60,88,165,1)
按钮文字	--color-text-btn	rgba(255,255,255,1)

### 强调色

元素	变量	rgba
强调默认	--color-accent	rgba(74,105,189,1)
强调悬停	--color-accent-hover	rgba(60,88,165,1)
强调按下	--color-accent-active	rgba(50,75,145,1)
强调淡色	--color-accent-dim	rgba(74,105,189,0.1)
强调光晕	--color-accent-glow	rgba(74,105,189,0.3)

### 边框

元素	变量	rgba
默认边框	--color-border	rgba(0,0,0,0.1)
悬停边框	--color-border-hover	rgba(0,0,0,0.15)
聚焦边框	--color-border-focus	rgba(74,105,189,0.5)
淡边框	--color-border-dim	rgba(0,0,0,0.05)

### 状态色

元素	变量	rgba
危险	--color-danger	rgba(220,38,38,1)
危险淡色	--color-danger-dim	rgba(220,38,38,0.1)
成功	--color-success	rgba(22,163,74,1)
成功淡色	--color-success-dim	rgba(22,163,74,0.1)
警告	--color-warning	rgba(234,179,8,1)
警告淡色	--color-warning-dim	rgba(234,179,8,0.1)
信息	--color-info	rgba(59,130,246,1)
信息淡色	--color-info-dim	rgba(59,130,246,0.1)

### 滚动条

元素	rgba
轨道	rgba(0,0,0,0)
滑块 默认	rgba(0,0,0,0.12)
滑块 悬停	rgba(0,0,0,0.2)

### 阴影

元素	值
卡片阴影	0 2px 8px rgba(0,0,0,0.06)
模态框阴影	0 8px 32px rgba(0,0,0,0.12)
下拉菜单阴影	0 4px 16px rgba(0,0,0,0.08)

---

## 主题 3 亮色蓝底蓝白

### 背景层

元素	变量	rgba
页面底层	--color-bg	rgba(26,26,46,1)
表面色	--color-surface	rgba(36,36,66,1)
模态框底色	--color-modal	rgba(245,247,250,1)
下拉菜单底色	--color-dropdown	rgba(245,247,250,1)
tooltip底色	--color-tooltip	rgba(20,20,40,0.95)

### 玻璃叠加层

元素	背景rgba	边框rgba
侧边栏	rgba(26,26,46,0.7)	rgba(255,255,255,0.08)
顶栏	rgba(26,26,46,0.6)	rgba(255,255,255,0.08)
卡片	rgba(255,255,255,0.06)	rgba(255,255,255,0.1)
输入框(深色区)	rgba(255,255,255,0.08)	rgba(255,255,255,0.12)
输入框(浅色modal内)	rgba(0,0,0,0.04)	rgba(0,0,0,0.1)
按钮(默认)	rgba(74,105,189,0.9)	rgba(74,105,189,0.3)
按钮(悬停)	rgba(60,88,165,1)	rgba(60,88,165,0.4)
按钮(按下)	rgba(50,75,145,1)	rgba(50,75,145,0.5)
按钮(禁用)	rgba(74,105,189,0.3)	rgba(74,105,189,0.1)
AI气泡	rgba(255,255,255,0.06)	rgba(255,255,255,0.08)
用户气泡	rgba(74,105,189,0.25)	rgba(74,105,189,0.2)
下拉菜单	rgba(245,247,250,0.95)	rgba(0,0,0,0.08)
tooltip	rgba(20,20,40,0.95)	rgba(255,255,255,0.1)

### 文字

元素	变量	rgba
主文字(深色区)	--color-text	rgba(200,200,220,0.85)
暗文字(深色区)	--color-text-dim	rgba(200,200,220,0.5)
亮文字(深色区)	--color-text-bright	rgba(240,240,255,1)
主文字(浅色modal)	--color-text-modal	rgba(26,26,46,0.85)
暗文字(浅色modal)	--color-text-modal-dim	rgba(26,26,46,0.5)
禁用文字	--color-text-disabled	rgba(200,200,220,0.3)
链接文字	--color-text-link	rgba(120,150,220,1)
按钮文字	--color-text-btn	rgba(255,255,255,1)

### 强调色

元素	变量	rgba
强调默认	--color-accent	rgba(74,105,189,1)
强调悬停	--color-accent-hover	rgba(90,120,200,1)
强调按下	--color-accent-active	rgba(60,88,165,1)
强调淡色	--color-accent-dim	rgba(74,105,189,0.15)
强调光晕	--color-accent-glow	rgba(74,105,189,0.35)

### 边框

元素	变量	rgba
默认边框(深色区)	--color-border	rgba(255,255,255,0.1)
悬停边框(深色区)	--color-border-hover	rgba(255,255,255,0.15)
默认边框(浅色modal)	--color-border-modal	rgba(0,0,0,0.1)
聚焦边框	--color-border-focus	rgba(74,105,189,0.5)
淡边框	--color-border-dim	rgba(255,255,255,0.05)

### 状态色

元素	变量	rgba
危险	--color-danger	rgba(239,68,68,1)
危险淡色	--color-danger-dim	rgba(239,68,68,0.15)
成功	--color-success	rgba(34,197,94,1)
成功淡色	--color-success-dim	rgba(34,197,94,0.15)
警告	--color-warning	rgba(250,204,21,1)
警告淡色	--color-warning-dim	rgba(250,204,21,0.15)
信息	--color-info	rgba(96,165,250,1)
信息淡色	--color-info-dim	rgba(96,165,250,0.15)

### 滚动条

元素	rgba
轨道	rgba(0,0,0,0)
滑块(深色区)	rgba(255,255,255,0.12)
滑块(深色区 悬停)	rgba(255,255,255,0.2)
滑块(浅色modal)	rgba(0,0,0,0.12)

### 阴影

元素	值
卡片阴影	0 2px 8px rgba(0,0,0,0.2)
模态框阴影	0 8px 32px rgba(0,0,0,0.3)
下拉菜单阴影	0 4px 16px rgba(0,0,0,0.15)

---

## 主题 4 暗色灰彩

### 背景层

元素	变量	rgba
页面底层	--color-bg	rgba(40,44,52,1)
表面色	--color-surface	rgba(50,54,64,1)
模态框底色	--color-modal	rgba(90,99,116,1)
下拉菜单底色	--color-dropdown	rgba(55,60,72,1)
tooltip底色	--color-tooltip	rgba(65,70,82,0.95)

### 玻璃叠加层

元素	背景rgba	边框rgba
侧边栏	rgba(40,44,52,0.7)	rgba(255,255,255,0.06)
顶栏	rgba(40,44,52,0.6)	rgba(255,255,255,0.06)
卡片	rgba(255,255,255,0.04)	rgba(255,255,255,0.08)
输入框	rgba(255,255,255,0.06)	rgba(255,255,255,0.1)
按钮 绿色/主操作	rgba(152,195,121,0.25)	rgba(152,195,121,0.3)
按钮 红色/危险	rgba(224,108,117,0.25)	rgba(224,108,117,0.3)
按钮 蓝色/信息	rgba(86,182,194,0.25)	rgba(86,182,194,0.3)
按钮 黄色/警告	rgba(229,192,123,0.25)	rgba(229,192,123,0.3)
按钮(悬停 通用)	alpha+0.15	alpha+0.1
按钮(禁用 通用)	alpha×0.3	alpha×0.3
AI气泡	rgba(255,255,255,0.05)	rgba(255,255,255,0.08)
用户气泡	rgba(152,195,121,0.15)	rgba(152,195,121,0.2)
下拉菜单	rgba(55,60,72,0.92)	rgba(255,255,255,0.08)
tooltip	rgba(65,70,82,0.95)	rgba(255,255,255,0.1)

### 文字

元素	变量	rgba
主文字	--color-text	rgba(220,223,228,1)
暗文字	--color-text-dim	rgba(160,165,175,1)
亮文字	--color-text-bright	rgba(245,245,250,1)
禁用文字	--color-text-disabled	rgba(120,125,135,1)
链接文字	--color-text-link	rgba(86,182,194,1)

### 强调色 四色体系

角色	变量	rgba	用途
主操作/确认	--color-accent-green	rgba(152,195,121,1)	提交/保存/确认按钮 滑块开启
危险/删除	--color-accent-red	rgba(224,108,117,1)	删除/取消/错误
信息/导航	--color-accent-blue	rgba(86,182,194,1)	链接/信息/帮助
警告/提示	--color-accent-yellow	rgba(229,192,123,1)	警告/注意/标记

### 边框

元素	变量	rgba
默认边框	--color-border	rgba(255,255,255,0.08)
悬停边框	--color-border-hover	rgba(255,255,255,0.14)
聚焦边框(绿)	--color-border-focus	rgba(152,195,121,0.5)
淡边框	--color-border-dim	rgba(255,255,255,0.04)

### 滚动条

元素	rgba
轨道	rgba(0,0,0,0)
滑块 默认	rgba(255,255,255,0.1)
滑块 悬停	rgba(255,255,255,0.18)

### 阴影

元素	值
卡片阴影	0 2px 8px rgba(0,0,0,0.2)
模态框阴影	0 8px 32px rgba(0,0,0,0.35)
下拉菜单阴影	0 4px 16px rgba(0,0,0,0.25)

---

## 主题 5 暗色灰橘

### 背景层

元素	变量	rgba
页面底层	--color-bg	rgba(38,38,38,1)
表面色	--color-surface	rgba(48,48,46,1)
模态框底色	--color-modal	rgba(48,48,46,1)
下拉菜单底色	--color-dropdown	rgba(42,42,40,1)
tooltip底色	--color-tooltip	rgba(55,55,52,0.95)

### 玻璃叠加层

元素	背景rgba	边框rgba
侧边栏	rgba(38,38,38,0.7)	rgba(255,255,255,0.05)
顶栏	rgba(38,38,38,0.6)	rgba(255,255,255,0.05)
卡片	rgba(255,255,255,0.03)	rgba(255,255,255,0.06)
输入框	rgba(255,255,255,0.05)	rgba(255,255,255,0.08)
按钮(默认)	rgba(198,97,63,0.35)	rgba(198,97,63,0.3)
按钮(悬停)	rgba(218,115,78,0.45)	rgba(218,115,78,0.4)
按钮(按下)	rgba(178,82,50,0.5)	rgba(178,82,50,0.5)
按钮(禁用)	rgba(198,97,63,0.12)	rgba(198,97,63,0.1)
AI气泡	rgba(255,255,255,0.04)	rgba(255,255,255,0.06)
用户气泡	rgba(198,97,63,0.2)	rgba(198,97,63,0.2)
下拉菜单	rgba(42,42,40,0.92)	rgba(255,255,255,0.06)
tooltip	rgba(55,55,52,0.95)	rgba(255,255,255,0.08)

### 文字

元素	变量	rgba
主文字	--color-text	rgba(156,154,146,1)
暗文字	--color-text-dim	rgba(120,118,112,1)
亮文字	--color-text-bright	rgba(210,208,200,1)
禁用文字	--color-text-disabled	rgba(90,88,82,1)
链接文字	--color-text-link	rgba(198,97,63,1)
链接悬停	--color-text-link-hover	rgba(218,115,78,1)

### 强调色

元素	变量	rgba
强调默认	--color-accent	rgba(198,97,63,1)
强调悬停	--color-accent-hover	rgba(218,115,78,1)
强调按下	--color-accent-active	rgba(178,82,50,1)
强调淡色	--color-accent-dim	rgba(198,97,63,0.15)
强调光晕	--color-accent-glow	rgba(198,97,63,0.35)

### 边框

元素	变量	rgba
默认边框	--color-border	rgba(255,255,255,0.07)
悬停边框	--color-border-hover	rgba(255,255,255,0.12)
聚焦边框	--color-border-focus	rgba(198,97,63,0.5)
淡边框	--color-border-dim	rgba(255,255,255,0.03)

### 状态色

元素	变量	rgba
危险	--color-danger	rgba(220,38,38,1)
危险淡色	--color-danger-dim	rgba(220,38,38,0.15)
成功	--color-success	rgba(34,197,94,1)
成功淡色	--color-success-dim	rgba(34,197,94,0.15)
警告	--color-warning	rgba(234,179,8,1)
警告淡色	--color-warning-dim	rgba(234,179,8,0.15)
信息	--color-info	rgba(59,130,246,1)
信息淡色	--color-info-dim	rgba(59,130,246,0.15)

### 滚动条

元素	rgba
轨道	rgba(0,0,0,0)
滑块 默认	rgba(255,255,255,0.08)
滑块 悬停	rgba(255,255,255,0.16)

### 阴影

元素	值
卡片阴影	0 2px 8px rgba(0,0,0,0.25)
模态框阴影	0 8px 32px rgba(0,0,0,0.4)
下拉菜单阴影	0 4px 16px rgba(0,0,0,0.3)
