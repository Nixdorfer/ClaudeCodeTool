# 配色体系

## 主题 1 经典报纸 (默认)

### 背景层

元素	变量	rgba
页面底层	--color-bg	rgba(250,248,245,1)
表面/侧边栏底色	--color-surface	rgba(240,236,228,1)
模态框底色	--color-modal	rgba(250,248,245,1)
下拉菜单底色	--color-dropdown	rgba(255,255,255,1)
tooltip底色	--color-tooltip	rgba(245,242,236,0.97)

### 玻璃叠加层

元素	背景rgba	边框rgba
侧边栏	rgba(250,248,245,0.95)	rgba(204,204,204,0.5)
顶栏	rgba(250,248,245,0.98)	rgba(204,204,204,0.4)
卡片	rgba(255,255,255,0)	rgba(204,204,204,0.6)
输入框	rgba(255,255,255,1)	rgba(204,204,204,1)
按钮(默认)	rgba(17,17,17,1)	rgba(17,17,17,1)
按钮(悬停)	rgba(51,51,51,1)	rgba(51,51,51,1)
按钮(按下)	rgba(0,0,0,1)	rgba(0,0,0,1)
按钮(禁用)	rgba(204,204,204,1)	rgba(204,204,204,1)
AI气泡	rgba(240,236,228,0.95)	rgba(204,204,204,0.5)
用户气泡	rgba(255,255,255,0.95)	rgba(204,204,204,0.5)
下拉菜单	rgba(255,255,255,0.98)	rgba(204,204,204,0.6)
tooltip	rgba(245,242,236,0.97)	rgba(204,204,204,0.5)

### 文字

元素	变量	rgba
主文字 正文/标签	--color-text	rgba(42,42,42,1)
暗文字 说明/占位符	--color-text-dim	rgba(102,102,102,1)
亮文字 标题/选中项	--color-text-bright	rgba(0,0,0,1)
禁用文字	--color-text-disabled	rgba(170,170,170,1)
链接文字	--color-text-link	rgba(196,30,58,1)
链接悬停	--color-text-link-hover	rgba(160,20,45,1)

### 强调色

元素	变量	rgba	用途
主强调默认 按钮/选中/图标高亮	--color-accent	rgba(196,30,58,1)	编辑红
主强调悬停	--color-accent-hover	rgba(160,20,45,1)	深编辑红
主强调按下	--color-accent-active	rgba(140,15,38,1)	暗编辑红
主强调淡色 标签背景/选中行	--color-accent-dim	rgba(196,30,58,0.08)	编辑红淡底
主强调光晕	--color-accent-glow	rgba(196,30,58,0.2)	编辑红柔光

### 边框

元素	变量	rgba
默认边框 卡片/分割线	--color-border	rgba(204,204,204,1)
悬停边框	--color-border-hover	rgba(170,170,170,1)
聚焦边框 输入框focus	--color-border-focus	rgba(17,17,17,1)
淡边框 表格行/列表分割	--color-border-dim	rgba(230,226,220,1)

### 状态色

元素	变量	rgba	用途
危险	--color-danger	rgba(180,30,30,1)	删除按钮/错误提示/必填标记
危险淡色	--color-danger-dim	rgba(180,30,30,0.08)	错误背景/危险toast
成功	--color-success	rgba(40,120,60,1)	成功提示/完成图标
成功淡色	--color-success-dim	rgba(40,120,60,0.08)	成功背景/成功toast
警告	--color-warning	rgba(180,130,20,1)	警告图标/注意提示
警告淡色	--color-warning-dim	rgba(180,130,20,0.08)	警告背景/警告toast
信息	--color-info	rgba(40,80,150,1)	帮助图标/信息提示
信息淡色	--color-info-dim	rgba(40,80,150,0.08)	信息背景/信息toast

### 输入组件

元素	rgba
输入框背景	rgba(255,255,255,1)
输入框边框 默认	rgba(204,204,204,1)
输入框边框 悬停	rgba(170,170,170,1)
输入框边框 聚焦	rgba(17,17,17,1)
输入框占位符	rgba(170,170,170,1)
选择框选中项背景	rgba(196,30,58,0.06)
滑块轨道	rgba(204,204,204,1)
滑块填充	rgba(17,17,17,1)
滑块旋钮	rgba(17,17,17,1)

### 滚动条

元素	rgba
轨道	rgba(250,248,245,1)
滑块 默认	rgba(204,204,204,1)
滑块 悬停	rgba(170,170,170,1)

### 阴影

元素	值
卡片阴影	none
模态框阴影	0 20px 50px rgba(0,0,0,0.12)
下拉菜单阴影	0 4px 16px rgba(0,0,0,0.08)
按钮阴影(hover)	none

---

## 主题 2 杂志光泽

### 背景层

元素	变量	rgba
页面底层	--color-bg	rgba(255,255,255,1)
表面色	--color-surface	rgba(248,248,250,1)
模态框底色	--color-modal	rgba(255,255,255,1)
下拉菜单底色	--color-dropdown	rgba(255,255,255,1)
tooltip底色	--color-tooltip	rgba(248,248,250,0.97)

### 玻璃叠加层

元素	背景rgba	边框rgba
侧边栏	rgba(255,255,255,0.95)	rgba(20,40,80,0.1)
顶栏	rgba(255,255,255,0.98)	rgba(20,40,80,0.08)
卡片	rgba(255,255,255,0)	rgba(20,40,80,0.12)
输入框	rgba(255,255,255,1)	rgba(20,40,80,0.2)
按钮(默认)	rgba(20,40,80,1)	rgba(20,40,80,1)
按钮(悬停)	rgba(35,60,110,1)	rgba(35,60,110,1)
按钮(按下)	rgba(12,28,60,1)	rgba(12,28,60,1)
按钮(禁用)	rgba(200,200,205,1)	rgba(200,200,205,1)
AI气泡	rgba(248,248,250,0.95)	rgba(20,40,80,0.1)
用户气泡	rgba(255,255,255,0.95)	rgba(20,40,80,0.1)
下拉菜单	rgba(255,255,255,0.98)	rgba(20,40,80,0.12)
tooltip	rgba(248,248,250,0.97)	rgba(20,40,80,0.12)

### 文字

元素	变量	rgba
主文字	--color-text	rgba(40,40,48,1)
暗文字	--color-text-dim	rgba(110,110,120,1)
亮文字	--color-text-bright	rgba(20,40,80,1)
禁用文字	--color-text-disabled	rgba(180,180,185,1)
链接文字	--color-text-link	rgba(180,145,50,1)
链接悬停	--color-text-link-hover	rgba(155,120,30,1)

### 强调色

元素	变量	rgba	用途
主强调默认	--color-accent	rgba(180,145,50,1)	杂志金
主强调悬停	--color-accent-hover	rgba(155,120,30,1)	深杂志金
主强调按下	--color-accent-active	rgba(135,105,20,1)	暗杂志金
主强调淡色	--color-accent-dim	rgba(180,145,50,0.08)	杂志金淡底
主强调光晕	--color-accent-glow	rgba(180,145,50,0.2)	杂志金柔光

### 边框

元素	变量	rgba
默认边框	--color-border	rgba(20,40,80,0.12)
悬停边框	--color-border-hover	rgba(20,40,80,0.25)
聚焦边框	--color-border-focus	rgba(20,40,80,0.6)
淡边框	--color-border-dim	rgba(20,40,80,0.06)

### 状态色

元素	变量	rgba	用途
危险	--color-danger	rgba(170,35,35,1)	删除/错误
危险淡色	--color-danger-dim	rgba(170,35,35,0.08)	错误背景
成功	--color-success	rgba(35,110,55,1)	成功提示
成功淡色	--color-success-dim	rgba(35,110,55,0.08)	成功背景
警告	--color-warning	rgba(175,125,15,1)	警告提示
警告淡色	--color-warning-dim	rgba(175,125,15,0.08)	警告背景
信息	--color-info	rgba(30,75,145,1)	信息提示
信息淡色	--color-info-dim	rgba(30,75,145,0.08)	信息背景

### 输入组件

元素	rgba
输入框背景	rgba(255,255,255,1)
输入框边框 默认	rgba(20,40,80,0.2)
输入框边框 悬停	rgba(20,40,80,0.35)
输入框边框 聚焦	rgba(20,40,80,0.6)
输入框占位符	rgba(110,110,120,0.6)
选择框选中项背景	rgba(180,145,50,0.08)
滑块轨道	rgba(20,40,80,0.1)
滑块填充	rgba(20,40,80,1)
滑块旋钮	rgba(20,40,80,1)

### 滚动条

元素	rgba
轨道	rgba(248,248,250,1)
滑块 默认	rgba(20,40,80,0.2)
滑块 悬停	rgba(20,40,80,0.4)

### 阴影

元素	值
卡片阴影	0 1px 4px rgba(20,40,80,0.06)
模态框阴影	0 20px 50px rgba(20,40,80,0.15)
下拉菜单阴影	0 4px 16px rgba(20,40,80,0.1)
按钮阴影(hover)	0 2px 8px rgba(20,40,80,0.15)

---

## 主题 3 复古牛皮纸

### 背景层

元素	变量	rgba
页面底层	--color-bg	rgba(215,195,170,1)
表面色	--color-surface	rgba(200,180,155,1)
模态框底色	--color-modal	rgba(225,205,180,1)
下拉菜单底色	--color-dropdown	rgba(220,200,175,1)
tooltip底色	--color-tooltip	rgba(210,190,165,0.97)

### 玻璃叠加层

元素	背景rgba	边框rgba
侧边栏	rgba(215,195,170,0.95)	rgba(80,50,30,0.15)
顶栏	rgba(215,195,170,0.98)	rgba(80,50,30,0.12)
卡片	rgba(225,205,180,0)	rgba(80,50,30,0.2)
输入框	rgba(225,205,180,1)	rgba(80,50,30,0.3)
按钮(默认)	rgba(80,50,30,1)	rgba(80,50,30,1)
按钮(悬停)	rgba(100,65,40,1)	rgba(100,65,40,1)
按钮(按下)	rgba(60,35,18,1)	rgba(60,35,18,1)
按钮(禁用)	rgba(180,165,145,1)	rgba(180,165,145,1)
AI气泡	rgba(200,180,155,0.95)	rgba(80,50,30,0.15)
用户气泡	rgba(225,205,180,0.95)	rgba(80,50,30,0.15)
下拉菜单	rgba(220,200,175,0.98)	rgba(80,50,30,0.2)
tooltip	rgba(210,190,165,0.97)	rgba(80,50,30,0.2)

### 文字

元素	变量	rgba
主文字	--color-text	rgba(55,35,20,1)
暗文字	--color-text-dim	rgba(110,85,65,1)
亮文字	--color-text-bright	rgba(40,22,10,1)
禁用文字	--color-text-disabled	rgba(160,140,120,1)
链接文字	--color-text-link	rgba(130,30,30,1)
链接悬停	--color-text-link-hover	rgba(100,18,18,1)

### 强调色

元素	变量	rgba	用途
主强调默认	--color-accent	rgba(130,30,30,1)	暗红
主强调悬停	--color-accent-hover	rgba(100,18,18,1)	深暗红
主强调按下	--color-accent-active	rgba(85,12,12,1)	极暗红
主强调淡色	--color-accent-dim	rgba(130,30,30,0.1)	暗红淡底
主强调光晕	--color-accent-glow	rgba(130,30,30,0.2)	暗红柔光

### 边框

元素	变量	rgba
默认边框	--color-border	rgba(80,50,30,0.25)
悬停边框	--color-border-hover	rgba(80,50,30,0.4)
聚焦边框	--color-border-focus	rgba(80,50,30,0.7)
淡边框	--color-border-dim	rgba(80,50,30,0.1)

### 状态色

元素	变量	rgba	用途
危险	--color-danger	rgba(160,30,30,1)	删除/错误
危险淡色	--color-danger-dim	rgba(160,30,30,0.1)	错误背景
成功	--color-success	rgba(50,100,45,1)	成功提示
成功淡色	--color-success-dim	rgba(50,100,45,0.1)	成功背景
警告	--color-warning	rgba(160,110,20,1)	警告提示
警告淡色	--color-warning-dim	rgba(160,110,20,0.1)	警告背景
信息	--color-info	rgba(50,75,120,1)	信息提示
信息淡色	--color-info-dim	rgba(50,75,120,0.1)	信息背景

### 输入组件

元素	rgba
输入框背景	rgba(225,205,180,1)
输入框边框 默认	rgba(80,50,30,0.3)
输入框边框 悬停	rgba(80,50,30,0.45)
输入框边框 聚焦	rgba(80,50,30,0.7)
输入框占位符	rgba(110,85,65,0.6)
选择框选中项背景	rgba(130,30,30,0.08)
滑块轨道	rgba(80,50,30,0.15)
滑块填充	rgba(80,50,30,1)
滑块旋钮	rgba(80,50,30,1)

### 滚动条

元素	rgba
轨道	rgba(215,195,170,1)
滑块 默认	rgba(80,50,30,0.3)
滑块 悬停	rgba(80,50,30,0.5)

### 阴影

元素	值
卡片阴影	none
模态框阴影	0 15px 40px rgba(40,25,10,0.2)
下拉菜单阴影	0 4px 16px rgba(40,25,10,0.15)
按钮阴影(hover)	none

---

## 主题 4 夜间阅读

### 背景层

元素	变量	rgba
页面底层	--color-bg	rgba(38,38,42,1)
表面色	--color-surface	rgba(48,48,54,1)
模态框底色	--color-modal	rgba(45,45,50,1)
下拉菜单底色	--color-dropdown	rgba(50,50,56,1)
tooltip底色	--color-tooltip	rgba(55,55,60,0.97)

### 玻璃叠加层

元素	背景rgba	边框rgba
侧边栏	rgba(38,38,42,0.95)	rgba(200,190,175,0.08)
顶栏	rgba(38,38,42,0.98)	rgba(200,190,175,0.06)
卡片	rgba(48,48,54,0)	rgba(200,190,175,0.1)
输入框	rgba(55,55,60,1)	rgba(200,190,175,0.2)
按钮(默认)	rgba(200,190,175,1)	rgba(200,190,175,1)
按钮(悬停)	rgba(220,212,200,1)	rgba(220,212,200,1)
按钮(按下)	rgba(180,170,155,1)	rgba(180,170,155,1)
按钮(禁用)	rgba(75,75,80,1)	rgba(75,75,80,1)
AI气泡	rgba(48,48,54,0.95)	rgba(200,190,175,0.1)
用户气泡	rgba(55,55,60,0.95)	rgba(200,190,175,0.1)
下拉菜单	rgba(50,50,56,0.98)	rgba(200,190,175,0.12)
tooltip	rgba(55,55,60,0.97)	rgba(200,190,175,0.12)

### 文字

元素	变量	rgba
主文字	--color-text	rgba(200,190,175,1)
暗文字	--color-text-dim	rgba(140,132,120,1)
亮文字	--color-text-bright	rgba(240,235,225,1)
禁用文字	--color-text-disabled	rgba(90,88,82,1)
链接文字	--color-text-link	rgba(225,155,60,1)
链接悬停	--color-text-link-hover	rgba(240,175,80,1)

### 强调色

元素	变量	rgba	用途
主强调默认	--color-accent	rgba(225,155,60,1)	暖橙
主强调悬停	--color-accent-hover	rgba(240,175,80,1)	亮暖橙
主强调按下	--color-accent-active	rgba(200,135,45,1)	深暖橙
主强调淡色	--color-accent-dim	rgba(225,155,60,0.1)	暖橙淡底
主强调光晕	--color-accent-glow	rgba(225,155,60,0.2)	暖橙柔光

### 边框

元素	变量	rgba
默认边框	--color-border	rgba(200,190,175,0.12)
悬停边框	--color-border-hover	rgba(200,190,175,0.25)
聚焦边框	--color-border-focus	rgba(200,190,175,0.5)
淡边框	--color-border-dim	rgba(200,190,175,0.06)

### 状态色

元素	变量	rgba	用途
危险	--color-danger	rgba(220,60,60,1)	删除/错误
危险淡色	--color-danger-dim	rgba(220,60,60,0.12)	错误背景
成功	--color-success	rgba(80,180,90,1)	成功提示
成功淡色	--color-success-dim	rgba(80,180,90,0.12)	成功背景
警告	--color-warning	rgba(225,180,50,1)	警告提示
警告淡色	--color-warning-dim	rgba(225,180,50,0.12)	警告背景
信息	--color-info	rgba(80,150,220,1)	信息提示
信息淡色	--color-info-dim	rgba(80,150,220,0.12)	信息背景

### 输入组件

元素	rgba
输入框背景	rgba(55,55,60,1)
输入框边框 默认	rgba(200,190,175,0.2)
输入框边框 悬停	rgba(200,190,175,0.35)
输入框边框 聚焦	rgba(200,190,175,0.5)
输入框占位符	rgba(140,132,120,0.6)
选择框选中项背景	rgba(225,155,60,0.1)
滑块轨道	rgba(200,190,175,0.1)
滑块填充	rgba(225,155,60,1)
滑块旋钮	rgba(240,235,225,1)

### 滚动条

元素	rgba
轨道	rgba(38,38,42,1)
滑块 默认	rgba(200,190,175,0.25)
滑块 悬停	rgba(200,190,175,0.45)

### 阴影

元素	值
卡片阴影	none
模态框阴影	0 20px 50px rgba(0,0,0,0.35)
下拉菜单阴影	0 4px 16px rgba(0,0,0,0.3)
按钮阴影(hover)	none

---

## 主题 5 学术蓝白

### 背景层

元素	变量	rgba
页面底层	--color-bg	rgba(235,240,248,1)
表面色	--color-surface	rgba(225,232,242,1)
模态框底色	--color-modal	rgba(240,244,252,1)
下拉菜单底色	--color-dropdown	rgba(245,248,255,1)
tooltip底色	--color-tooltip	rgba(235,240,248,0.97)

### 玻璃叠加层

元素	背景rgba	边框rgba
侧边栏	rgba(235,240,248,0.95)	rgba(25,50,100,0.1)
顶栏	rgba(235,240,248,0.98)	rgba(25,50,100,0.08)
卡片	rgba(245,248,255,0)	rgba(25,50,100,0.12)
输入框	rgba(255,255,255,1)	rgba(25,50,100,0.2)
按钮(默认)	rgba(25,50,100,1)	rgba(25,50,100,1)
按钮(悬停)	rgba(40,68,125,1)	rgba(40,68,125,1)
按钮(按下)	rgba(15,35,75,1)	rgba(15,35,75,1)
按钮(禁用)	rgba(190,198,210,1)	rgba(190,198,210,1)
AI气泡	rgba(225,232,242,0.95)	rgba(25,50,100,0.1)
用户气泡	rgba(245,248,255,0.95)	rgba(25,50,100,0.1)
下拉菜单	rgba(245,248,255,0.98)	rgba(25,50,100,0.12)
tooltip	rgba(235,240,248,0.97)	rgba(25,50,100,0.12)

### 文字

元素	变量	rgba
主文字	--color-text	rgba(35,45,60,1)
暗文字	--color-text-dim	rgba(90,105,125,1)
亮文字	--color-text-bright	rgba(25,50,100,1)
禁用文字	--color-text-disabled	rgba(165,175,190,1)
链接文字	--color-text-link	rgba(180,35,35,1)
链接悬停	--color-text-link-hover	rgba(150,25,25,1)

### 强调色

元素	变量	rgba	用途
主强调默认	--color-accent	rgba(180,35,35,1)	学术红
主强调悬停	--color-accent-hover	rgba(150,25,25,1)	深学术红
主强调按下	--color-accent-active	rgba(125,18,18,1)	暗学术红
主强调淡色	--color-accent-dim	rgba(180,35,35,0.08)	学术红淡底
主强调光晕	--color-accent-glow	rgba(180,35,35,0.18)	学术红柔光

### 边框

元素	变量	rgba
默认边框	--color-border	rgba(25,50,100,0.12)
悬停边框	--color-border-hover	rgba(25,50,100,0.25)
聚焦边框	--color-border-focus	rgba(25,50,100,0.55)
淡边框	--color-border-dim	rgba(25,50,100,0.06)

### 状态色

元素	变量	rgba	用途
危险	--color-danger	rgba(175,35,35,1)	删除/错误
危险淡色	--color-danger-dim	rgba(175,35,35,0.08)	错误背景
成功	--color-success	rgba(35,115,55,1)	成功提示
成功淡色	--color-success-dim	rgba(35,115,55,0.08)	成功背景
警告	--color-warning	rgba(170,120,15,1)	警告提示
警告淡色	--color-warning-dim	rgba(170,120,15,0.08)	警告背景
信息	--color-info	rgba(25,50,100,1)	信息提示
信息淡色	--color-info-dim	rgba(25,50,100,0.08)	信息背景

### 输入组件

元素	rgba
输入框背景	rgba(255,255,255,1)
输入框边框 默认	rgba(25,50,100,0.2)
输入框边框 悬停	rgba(25,50,100,0.35)
输入框边框 聚焦	rgba(25,50,100,0.55)
输入框占位符	rgba(90,105,125,0.6)
选择框选中项背景	rgba(180,35,35,0.06)
滑块轨道	rgba(25,50,100,0.1)
滑块填充	rgba(25,50,100,1)
滑块旋钮	rgba(25,50,100,1)

### 滚动条

元素	rgba
轨道	rgba(235,240,248,1)
滑块 默认	rgba(25,50,100,0.2)
滑块 悬停	rgba(25,50,100,0.4)

### 阴影

元素	值
卡片阴影	0 1px 3px rgba(25,50,100,0.06)
模态框阴影	0 20px 50px rgba(25,50,100,0.12)
下拉菜单阴影	0 4px 16px rgba(25,50,100,0.08)
按钮阴影(hover)	0 2px 6px rgba(25,50,100,0.12)
