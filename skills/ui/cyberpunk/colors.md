# 配色体系

## 主题 1 经典霓虹蓝 (默认)

### 背景层

元素	变量	rgba
页面底层	--color-bg	rgba(10,10,26,1)
表面/侧边栏底色	--color-surface	rgba(13,13,43,1)
模态框底色	--color-modal	rgba(26,10,46,1)
下拉菜单底色	--color-dropdown	rgba(15,15,35,1)
tooltip底色	--color-tooltip	rgba(20,20,45,0.95)

### 玻璃叠加层

元素	背景rgba	边框rgba
侧边栏	rgba(10,10,26,0.7)	rgba(0,240,255,0.08)
顶栏	rgba(10,10,26,0.6)	rgba(0,240,255,0.08)
卡片	rgba(13,13,43,0.9)	rgba(0,240,255,0.2)
输入框	rgba(0,240,255,0.05)	rgba(0,240,255,0.3)
按钮(默认)	rgba(0,0,0,0)	rgba(0,240,255,1)
按钮(悬停)	rgba(0,240,255,0.15)	rgba(0,240,255,1)
按钮(按下)	rgba(0,240,255,0.25)	rgba(0,240,255,1)
按钮(禁用)	rgba(0,240,255,0.03)	rgba(0,240,255,0.3)
AI气泡	rgba(13,13,43,0.8)	rgba(0,240,255,0.15)
用户气泡	rgba(0,240,255,0.1)	rgba(0,240,255,0.25)
下拉菜单	rgba(15,15,35,0.92)	rgba(0,240,255,0.15)
tooltip	rgba(20,20,45,0.95)	rgba(0,240,255,0.2)

### 文字

元素	变量	rgba
主文字 正文/标签	--color-text	rgba(192,200,216,1)
暗文字 说明/占位符	--color-text-dim	rgba(100,110,130,1)
亮文字 标题/选中项	--color-text-bright	rgba(255,255,255,1)
禁用文字	--color-text-disabled	rgba(70,75,90,1)
链接文字	--color-text-link	rgba(0,240,255,1)
链接悬停	--color-text-link-hover	rgba(100,250,255,1)

### 强调色

元素	变量	rgba	用途
主强调默认 按钮/选中滑块/图标高亮	--color-accent	rgba(0,240,255,1)	霓虹青
主强调悬停 按钮hover/滑块hover	--color-accent-hover	rgba(100,250,255,1)	亮霓虹青
主强调按下 按钮active	--color-accent-active	rgba(0,200,215,1)	深霓虹青
主强调淡色 标签背景/选中行	--color-accent-dim	rgba(0,240,255,0.12)	霓虹青淡底
主强调光晕 focus-ring/脉冲动画	--color-accent-glow	rgba(0,240,255,0.4)	霓虹青光晕
副强调色 关闭按钮/警示高亮	--color-accent-secondary	rgba(255,0,170,1)	霓虹粉
第三强调色 装饰/渐变端点	--color-accent-tertiary	rgba(176,0,255,1)	霓虹紫

### 边框

元素	变量	rgba
默认边框 卡片/分割线	--color-border	rgba(0,240,255,0.15)
悬停边框 卡片hover/输入框hover	--color-border-hover	rgba(0,240,255,0.35)
聚焦边框 输入框focus	--color-border-focus	rgba(0,240,255,0.6)
淡边框 表格行/列表分割	--color-border-dim	rgba(0,240,255,0.06)

### 状态色

元素	变量	rgba	用途
危险	--color-danger	rgba(255,50,50,1)	删除按钮/错误提示/必填标记
危险淡色	--color-danger-dim	rgba(255,50,50,0.15)	错误背景/危险toast
成功	--color-success	rgba(0,255,136,1)	成功提示/完成图标
成功淡色	--color-success-dim	rgba(0,255,136,0.15)	成功背景/成功toast
警告	--color-warning	rgba(255,230,0,1)	警告图标/注意提示
警告淡色	--color-warning-dim	rgba(255,230,0,0.15)	警告背景/警告toast
信息	--color-info	rgba(0,150,255,1)	帮助图标/信息提示
信息淡色	--color-info-dim	rgba(0,150,255,0.15)	信息背景/信息toast

### 输入组件

元素	rgba
输入框背景	rgba(0,240,255,0.05)
输入框边框 默认	rgba(0,240,255,0.3)
输入框边框 悬停	rgba(0,240,255,0.45)
输入框边框 聚焦	rgba(0,240,255,0.7)
输入框占位符	rgba(192,200,216,0.4)
选择框选中项背景	rgba(0,240,255,0.15)
滑块轨道	rgba(0,240,255,0.1)
滑块填充	rgba(0,240,255,1)
滑块旋钮	rgba(255,255,255,1)

### 滚动条

元素	rgba
轨道	rgba(10,10,26,1)
滑块 默认	rgba(0,240,255,0.6)
滑块 悬停	rgba(0,240,255,0.9)

### 阴影

元素	值
卡片阴影	0 2px 12px rgba(0,240,255,0.1)
模态框阴影	0 0 30px rgba(0,240,255,0.2), inset 0 0 30px rgba(0,240,255,0.05)
下拉菜单阴影	0 4px 20px rgba(0,0,0,0.5)
按钮发光(hover)	0 0 15px rgba(0,240,255,0.5), inset 0 0 15px rgba(0,240,255,0.1)

---

## 主题 2 霓虹粉紫

### 背景层

元素	变量	rgba
页面底层	--color-bg	rgba(18,6,31,1)
表面色	--color-surface	rgba(25,10,42,1)
模态框底色	--color-modal	rgba(35,15,55,1)
下拉菜单底色	--color-dropdown	rgba(22,8,38,1)
tooltip底色	--color-tooltip	rgba(30,12,48,0.95)

### 玻璃叠加层

元素	背景rgba	边框rgba
侧边栏	rgba(18,6,31,0.7)	rgba(255,0,170,0.08)
顶栏	rgba(18,6,31,0.6)	rgba(255,0,170,0.08)
卡片	rgba(25,10,42,0.9)	rgba(255,0,170,0.2)
输入框	rgba(255,0,170,0.05)	rgba(255,0,170,0.3)
按钮(默认)	rgba(0,0,0,0)	rgba(255,0,170,1)
按钮(悬停)	rgba(255,0,170,0.15)	rgba(255,0,170,1)
按钮(按下)	rgba(255,0,170,0.25)	rgba(255,0,170,1)
按钮(禁用)	rgba(255,0,170,0.03)	rgba(255,0,170,0.3)
AI气泡	rgba(25,10,42,0.8)	rgba(255,0,170,0.15)
用户气泡	rgba(255,0,170,0.1)	rgba(255,0,170,0.25)
下拉菜单	rgba(22,8,38,0.92)	rgba(255,0,170,0.15)
tooltip	rgba(30,12,48,0.95)	rgba(255,0,170,0.2)

### 文字

元素	变量	rgba
主文字	--color-text	rgba(200,185,210,1)
暗文字	--color-text-dim	rgba(120,100,140,1)
亮文字	--color-text-bright	rgba(255,255,255,1)
禁用文字	--color-text-disabled	rgba(80,65,95,1)
链接文字	--color-text-link	rgba(255,0,170,1)
链接悬停	--color-text-link-hover	rgba(255,100,200,1)

### 强调色

元素	变量	rgba	用途
主强调默认	--color-accent	rgba(255,0,170,1)	霓虹粉
主强调悬停	--color-accent-hover	rgba(255,100,200,1)	亮霓虹粉
主强调按下	--color-accent-active	rgba(210,0,140,1)	深霓虹粉
主强调淡色	--color-accent-dim	rgba(255,0,170,0.12)	霓虹粉淡底
主强调光晕	--color-accent-glow	rgba(255,0,170,0.4)	霓虹粉光晕
副强调色	--color-accent-secondary	rgba(176,0,255,1)	霓虹紫
第三强调色	--color-accent-tertiary	rgba(0,240,255,1)	霓虹青

### 边框

元素	变量	rgba
默认边框	--color-border	rgba(255,0,170,0.15)
悬停边框	--color-border-hover	rgba(255,0,170,0.35)
聚焦边框	--color-border-focus	rgba(255,0,170,0.6)
淡边框	--color-border-dim	rgba(255,0,170,0.06)

### 状态色

元素	变量	rgba
危险	--color-danger	rgba(255,50,50,1)
危险淡色	--color-danger-dim	rgba(255,50,50,0.15)
成功	--color-success	rgba(0,255,136,1)
成功淡色	--color-success-dim	rgba(0,255,136,0.15)
警告	--color-warning	rgba(255,230,0,1)
警告淡色	--color-warning-dim	rgba(255,230,0,0.15)
信息	--color-info	rgba(176,0,255,1)
信息淡色	--color-info-dim	rgba(176,0,255,0.15)

### 输入组件

元素	rgba
输入框背景	rgba(255,0,170,0.05)
输入框边框 默认	rgba(255,0,170,0.3)
输入框边框 悬停	rgba(255,0,170,0.45)
输入框边框 聚焦	rgba(255,0,170,0.7)
输入框占位符	rgba(200,185,210,0.4)
选择框选中项背景	rgba(255,0,170,0.15)
滑块轨道	rgba(255,0,170,0.1)
滑块填充	rgba(255,0,170,1)
滑块旋钮	rgba(255,255,255,1)

### 滚动条

元素	rgba
轨道	rgba(18,6,31,1)
滑块 默认	rgba(255,0,170,0.6)
滑块 悬停	rgba(255,0,170,0.9)

### 阴影

元素	值
卡片阴影	0 2px 12px rgba(255,0,170,0.1)
模态框阴影	0 0 30px rgba(255,0,170,0.2), inset 0 0 30px rgba(255,0,170,0.05)
下拉菜单阴影	0 4px 20px rgba(0,0,0,0.5)
按钮发光(hover)	0 0 15px rgba(255,0,170,0.5), inset 0 0 15px rgba(255,0,170,0.1)

---

## 主题 3 黑客绿

### 背景层

元素	变量	rgba
页面底层	--color-bg	rgba(0,0,0,1)
表面色	--color-surface	rgba(8,8,8,1)
模态框底色	--color-modal	rgba(5,15,5,1)
下拉菜单底色	--color-dropdown	rgba(6,10,6,1)
tooltip底色	--color-tooltip	rgba(10,18,10,0.95)

### 玻璃叠加层

元素	背景rgba	边框rgba
侧边栏	rgba(0,0,0,0.7)	rgba(0,255,65,0.06)
顶栏	rgba(0,0,0,0.6)	rgba(0,255,65,0.06)
卡片	rgba(0,15,0,0.9)	rgba(0,255,65,0.15)
输入框	rgba(0,255,65,0.04)	rgba(0,255,65,0.25)
按钮(默认)	rgba(0,0,0,0)	rgba(0,255,65,1)
按钮(悬停)	rgba(0,255,65,0.12)	rgba(0,255,65,1)
按钮(按下)	rgba(0,255,65,0.2)	rgba(0,255,65,1)
按钮(禁用)	rgba(0,255,65,0.03)	rgba(0,255,65,0.25)
AI气泡	rgba(0,10,0,0.8)	rgba(0,255,65,0.12)
用户气泡	rgba(0,255,65,0.08)	rgba(0,255,65,0.2)
下拉菜单	rgba(6,10,6,0.92)	rgba(0,255,65,0.12)
tooltip	rgba(10,18,10,0.95)	rgba(0,255,65,0.15)

### 文字

元素	变量	rgba
主文字	--color-text	rgba(0,200,50,1)
暗文字	--color-text-dim	rgba(0,130,30,1)
亮文字	--color-text-bright	rgba(0,255,65,1)
禁用文字	--color-text-disabled	rgba(0,80,20,1)
链接文字	--color-text-link	rgba(0,255,65,1)
链接悬停	--color-text-link-hover	rgba(100,255,150,1)

### 强调色

元素	变量	rgba	用途
主强调默认	--color-accent	rgba(0,255,65,1)	矩阵绿
主强调悬停	--color-accent-hover	rgba(100,255,150,1)	亮矩阵绿
主强调按下	--color-accent-active	rgba(0,200,50,1)	深矩阵绿
主强调淡色	--color-accent-dim	rgba(0,255,65,0.1)	矩阵绿淡底
主强调光晕	--color-accent-glow	rgba(0,255,65,0.35)	矩阵绿光晕
副强调色	--color-accent-secondary	rgba(0,180,255,1)	数据蓝
第三强调色	--color-accent-tertiary	rgba(255,255,0,1)	警报黄

### 边框

元素	变量	rgba
默认边框	--color-border	rgba(0,255,65,0.12)
悬停边框	--color-border-hover	rgba(0,255,65,0.3)
聚焦边框	--color-border-focus	rgba(0,255,65,0.55)
淡边框	--color-border-dim	rgba(0,255,65,0.05)

### 状态色

元素	变量	rgba
危险	--color-danger	rgba(255,30,30,1)
危险淡色	--color-danger-dim	rgba(255,30,30,0.12)
成功	--color-success	rgba(0,255,65,1)
成功淡色	--color-success-dim	rgba(0,255,65,0.12)
警告	--color-warning	rgba(255,255,0,1)
警告淡色	--color-warning-dim	rgba(255,255,0,0.12)
信息	--color-info	rgba(0,180,255,1)
信息淡色	--color-info-dim	rgba(0,180,255,0.12)

### 输入组件

元素	rgba
输入框背景	rgba(0,255,65,0.04)
输入框边框 默认	rgba(0,255,65,0.25)
输入框边框 悬停	rgba(0,255,65,0.4)
输入框边框 聚焦	rgba(0,255,65,0.65)
输入框占位符	rgba(0,200,50,0.4)
选择框选中项背景	rgba(0,255,65,0.12)
滑块轨道	rgba(0,255,65,0.08)
滑块填充	rgba(0,255,65,1)
滑块旋钮	rgba(0,255,65,1)

### 滚动条

元素	rgba
轨道	rgba(0,0,0,1)
滑块 默认	rgba(0,255,65,0.5)
滑块 悬停	rgba(0,255,65,0.8)

### 阴影

元素	值
卡片阴影	0 2px 12px rgba(0,255,65,0.08)
模态框阴影	0 0 30px rgba(0,255,65,0.15), inset 0 0 30px rgba(0,255,65,0.03)
下拉菜单阴影	0 4px 20px rgba(0,0,0,0.6)
按钮发光(hover)	0 0 15px rgba(0,255,65,0.4), inset 0 0 15px rgba(0,255,65,0.08)

---

## 主题 4 烈焰橙

### 背景层

元素	变量	rgba
页面底层	--color-bg	rgba(15,12,10,1)
表面色	--color-surface	rgba(25,20,18,1)
模态框底色	--color-modal	rgba(35,25,20,1)
下拉菜单底色	--color-dropdown	rgba(20,16,14,1)
tooltip底色	--color-tooltip	rgba(30,22,18,0.95)

### 玻璃叠加层

元素	背景rgba	边框rgba
侧边栏	rgba(15,12,10,0.7)	rgba(255,100,0,0.08)
顶栏	rgba(15,12,10,0.6)	rgba(255,100,0,0.08)
卡片	rgba(25,20,18,0.9)	rgba(255,100,0,0.2)
输入框	rgba(255,100,0,0.05)	rgba(255,100,0,0.3)
按钮(默认)	rgba(0,0,0,0)	rgba(255,100,0,1)
按钮(悬停)	rgba(255,100,0,0.15)	rgba(255,100,0,1)
按钮(按下)	rgba(255,100,0,0.25)	rgba(255,100,0,1)
按钮(禁用)	rgba(255,100,0,0.03)	rgba(255,100,0,0.3)
AI气泡	rgba(25,20,18,0.8)	rgba(255,100,0,0.15)
用户气泡	rgba(255,100,0,0.1)	rgba(255,100,0,0.25)
下拉菜单	rgba(20,16,14,0.92)	rgba(255,100,0,0.15)
tooltip	rgba(30,22,18,0.95)	rgba(255,100,0,0.2)

### 文字

元素	变量	rgba
主文字	--color-text	rgba(200,190,180,1)
暗文字	--color-text-dim	rgba(130,120,110,1)
亮文字	--color-text-bright	rgba(255,255,255,1)
禁用文字	--color-text-disabled	rgba(80,72,65,1)
链接文字	--color-text-link	rgba(255,100,0,1)
链接悬停	--color-text-link-hover	rgba(255,150,60,1)

### 强调色

元素	变量	rgba	用途
主强调默认	--color-accent	rgba(255,100,0,1)	霓虹橙
主强调悬停	--color-accent-hover	rgba(255,150,60,1)	亮霓虹橙
主强调按下	--color-accent-active	rgba(210,80,0,1)	深霓虹橙
主强调淡色	--color-accent-dim	rgba(255,100,0,0.12)	霓虹橙淡底
主强调光晕	--color-accent-glow	rgba(255,100,0,0.4)	霓虹橙光晕
副强调色	--color-accent-secondary	rgba(255,30,30,1)	烈焰红
第三强调色	--color-accent-tertiary	rgba(255,230,0,1)	电弧黄

### 边框

元素	变量	rgba
默认边框	--color-border	rgba(255,100,0,0.15)
悬停边框	--color-border-hover	rgba(255,100,0,0.35)
聚焦边框	--color-border-focus	rgba(255,100,0,0.6)
淡边框	--color-border-dim	rgba(255,100,0,0.06)

### 状态色

元素	变量	rgba
危险	--color-danger	rgba(255,30,30,1)
危险淡色	--color-danger-dim	rgba(255,30,30,0.15)
成功	--color-success	rgba(0,230,100,1)
成功淡色	--color-success-dim	rgba(0,230,100,0.15)
警告	--color-warning	rgba(255,230,0,1)
警告淡色	--color-warning-dim	rgba(255,230,0,0.15)
信息	--color-info	rgba(0,150,255,1)
信息淡色	--color-info-dim	rgba(0,150,255,0.15)

### 输入组件

元素	rgba
输入框背景	rgba(255,100,0,0.05)
输入框边框 默认	rgba(255,100,0,0.3)
输入框边框 悬停	rgba(255,100,0,0.45)
输入框边框 聚焦	rgba(255,100,0,0.7)
输入框占位符	rgba(200,190,180,0.4)
选择框选中项背景	rgba(255,100,0,0.15)
滑块轨道	rgba(255,100,0,0.1)
滑块填充	rgba(255,100,0,1)
滑块旋钮	rgba(255,255,255,1)

### 滚动条

元素	rgba
轨道	rgba(15,12,10,1)
滑块 默认	rgba(255,100,0,0.6)
滑块 悬停	rgba(255,100,0,0.9)

### 阴影

元素	值
卡片阴影	0 2px 12px rgba(255,100,0,0.1)
模态框阴影	0 0 30px rgba(255,100,0,0.2), inset 0 0 30px rgba(255,100,0,0.05)
下拉菜单阴影	0 4px 20px rgba(0,0,0,0.5)
按钮发光(hover)	0 0 15px rgba(255,100,0,0.5), inset 0 0 15px rgba(255,100,0,0.1)

---

## 主题 5 冰蓝白

### 背景层

元素	变量	rgba
页面底层	--color-bg	rgba(12,16,24,1)
表面色	--color-surface	rgba(18,24,36,1)
模态框底色	--color-modal	rgba(22,30,45,1)
下拉菜单底色	--color-dropdown	rgba(15,20,32,1)
tooltip底色	--color-tooltip	rgba(20,28,42,0.95)

### 玻璃叠加层

元素	背景rgba	边框rgba
侧边栏	rgba(12,16,24,0.7)	rgba(180,220,255,0.08)
顶栏	rgba(12,16,24,0.6)	rgba(180,220,255,0.08)
卡片	rgba(18,24,36,0.9)	rgba(180,220,255,0.18)
输入框	rgba(180,220,255,0.04)	rgba(180,220,255,0.25)
按钮(默认)	rgba(0,0,0,0)	rgba(180,220,255,1)
按钮(悬停)	rgba(180,220,255,0.12)	rgba(180,220,255,1)
按钮(按下)	rgba(180,220,255,0.2)	rgba(180,220,255,1)
按钮(禁用)	rgba(180,220,255,0.03)	rgba(180,220,255,0.25)
AI气泡	rgba(18,24,36,0.8)	rgba(180,220,255,0.12)
用户气泡	rgba(180,220,255,0.08)	rgba(180,220,255,0.2)
下拉菜单	rgba(15,20,32,0.92)	rgba(180,220,255,0.12)
tooltip	rgba(20,28,42,0.95)	rgba(180,220,255,0.18)

### 文字

元素	变量	rgba
主文字	--color-text	rgba(180,200,220,1)
暗文字	--color-text-dim	rgba(110,130,155,1)
亮文字	--color-text-bright	rgba(240,248,255,1)
禁用文字	--color-text-disabled	rgba(70,85,100,1)
链接文字	--color-text-link	rgba(180,220,255,1)
链接悬停	--color-text-link-hover	rgba(220,240,255,1)

### 强调色

元素	变量	rgba	用途
主强调默认	--color-accent	rgba(180,220,255,1)	冰蓝白
主强调悬停	--color-accent-hover	rgba(220,240,255,1)	亮冰蓝
主强调按下	--color-accent-active	rgba(140,185,225,1)	深冰蓝
主强调淡色	--color-accent-dim	rgba(180,220,255,0.1)	冰蓝淡底
主强调光晕	--color-accent-glow	rgba(180,220,255,0.35)	冰蓝光晕
副强调色	--color-accent-secondary	rgba(0,240,255,1)	霓虹青
第三强调色	--color-accent-tertiary	rgba(140,120,255,1)	冷紫

### 边框

元素	变量	rgba
默认边框	--color-border	rgba(180,220,255,0.12)
悬停边框	--color-border-hover	rgba(180,220,255,0.3)
聚焦边框	--color-border-focus	rgba(180,220,255,0.55)
淡边框	--color-border-dim	rgba(180,220,255,0.05)

### 状态色

元素	变量	rgba
危险	--color-danger	rgba(255,60,60,1)
危险淡色	--color-danger-dim	rgba(255,60,60,0.12)
成功	--color-success	rgba(0,230,130,1)
成功淡色	--color-success-dim	rgba(0,230,130,0.12)
警告	--color-warning	rgba(255,220,50,1)
警告淡色	--color-warning-dim	rgba(255,220,50,0.12)
信息	--color-info	rgba(100,160,255,1)
信息淡色	--color-info-dim	rgba(100,160,255,0.12)

### 输入组件

元素	rgba
输入框背景	rgba(180,220,255,0.04)
输入框边框 默认	rgba(180,220,255,0.25)
输入框边框 悬停	rgba(180,220,255,0.4)
输入框边框 聚焦	rgba(180,220,255,0.65)
输入框占位符	rgba(180,200,220,0.4)
选择框选中项背景	rgba(180,220,255,0.12)
滑块轨道	rgba(180,220,255,0.08)
滑块填充	rgba(180,220,255,1)
滑块旋钮	rgba(240,248,255,1)

### 滚动条

元素	rgba
轨道	rgba(12,16,24,1)
滑块 默认	rgba(180,220,255,0.45)
滑块 悬停	rgba(180,220,255,0.75)

### 阴影

元素	值
卡片阴影	0 2px 12px rgba(180,220,255,0.06)
模态框阴影	0 0 30px rgba(180,220,255,0.15), inset 0 0 30px rgba(180,220,255,0.03)
下拉菜单阴影	0 4px 20px rgba(0,0,0,0.5)
按钮发光(hover)	0 0 15px rgba(180,220,255,0.4), inset 0 0 15px rgba(180,220,255,0.08)
