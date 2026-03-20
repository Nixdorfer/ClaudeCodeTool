# 太空科幻特效体系

## 星空粒子背景

容器: fixed全屏 z-index:0 pointer-events:none
粒子数量: 200个 div 元素
粒子尺寸: 90%概率1px 10%概率2px
粒子颜色: #ffffff
粒子形状: border-radius 50%
粒子分布: 随机 top/left 百分比
粒子透明度: 基础 0.3 + 随机 0.7
粒子动画: twinkle 时长 2s+随机4s ease-in-out infinite 随机延迟0-3s

## 星云渐变叠加

容器: body::before fixed全屏 z-index:1 pointer-events:none
渐变层叠:
- radial-gradient(ellipse at 20% 50%, rgba(106,77,189,0.08) 0%, transparent 50%)
- radial-gradient(ellipse at 80% 30%, rgba(74,168,216,0.06) 0%, transparent 40%)
- radial-gradient(ellipse at 50% 80%, rgba(232,118,42,0.04) 0%, transparent 50%)

## 全息投影效果

适用: 数据面板/HUD元素/重要信息卡片
背景: rgba(10,22,40,0.7)
边框: 1px solid rgba(74,168,216,0.2)
圆角: 8px
扫描线叠加: repeating-linear-gradient(0deg, transparent, transparent 2px, rgba(74,168,216,0.03) 2px, rgba(74,168,216,0.03) 4px)
外发光: box-shadow 0 0 30px rgba(74,168,216,0.06)
backdrop-filter: blur(10px)

## HUD边框

适用: 面板/卡片四角装饰
实现: ::before和::after伪元素绘制角标线条
角标尺寸: 12px x 12px
角标粗细: 2px
角标颜色: rgba(74,168,216,0.4)
四角定位:
- ::before 左上角 border-top + border-left
- ::after 右下角 border-bottom + border-right
- 额外元素处理右上和左下

## 雷达扫描线

容器: 正方形 position relative overflow hidden border-radius 50%
底盘: 圆形 border 1px solid rgba(74,168,216,0.2)
同心圆: 3层 25%/50%/75% 半径 相同边框
十字线: 水平+垂直1px线 rgba(74,168,216,0.15)
扫描臂: ::after 伪元素 从圆心到边缘的锥形渐变
扫描颜色: conic-gradient(from 0deg, transparent 0deg, rgba(74,168,216,0.3) 30deg, transparent 30deg)
扫描动画: radar-sweep 360deg旋转 4s linear infinite
扫描拖尾: 30度锥形渐变产生扫描尾迹

## 能量条

容器: 高度6px 圆角3px 背景rgba(74,168,216,0.1)
填充条: 高度100% 圆角3px 渐变背景
填充渐变: linear-gradient(90deg, rgba(74,168,216,0.6), rgba(74,168,216,1))
填充动画: energy-flow 背景位置从0%到200% 2s linear infinite
填充纹理: repeating-linear-gradient(90deg, transparent, transparent 4px, rgba(255,255,255,0.1) 4px, rgba(255,255,255,0.1) 6px)
末端发光: ::after 4px圆点 rgba(74,168,216,1) + box-shadow 0 0 8px rgba(74,168,216,0.6)

## 数据面板发光

适用: HUD数据面板/仪表盘
静态发光: box-shadow 0 0 20px rgba(74,168,216,0.05) inset, 0 0 30px rgba(74,168,216,0.06)
数据行分隔: border-bottom 1px solid rgba(74,168,216,0.08)
数值闪烁: 关键数据使用 data-blink 动画 opacity 1>0.6>1 1.5s infinite
数据更新: 数值变化时 color 短暂变为 rgba(232,118,42,1) 0.3s后恢复

## 扫描动画

适用: 加载状态/数据读取/搜索中
类型: 水平扫描线从上到下
实现: ::after伪元素 高度2px 宽度100%
颜色: linear-gradient(90deg, transparent, rgba(74,168,216,0.6), transparent)
动画: scan-line translateY从0%到容器高度 2s ease-in-out infinite
发光: box-shadow 0 0 12px rgba(74,168,216,0.3)

## 流星效果

触发: 随机间隔 或页面加载时
元素: 2px x 2px 白色圆点
尾迹: box-shadow 模拟 -20px偏移的淡白色拖尾
动画: translateX(0)translateY(0) 到 translateX(300px)translateY(200px) opacity 1到0
时长: 1s ease-out forwards
起始位置: 随机顶部区域

## 脉冲呼吸环

适用: 状态指示灯/在线标记/活跃元素
动画: box-shadow 从 0 0 0 0 rgba(74,168,216,0.3) 到 0 0 0 15px rgba(74,168,216,0) 再回到初始
时长: 2s ease-in-out infinite

## 全息干扰条纹

适用: 加载/错误/过渡状态
实现: 随机水平条纹 2-4px高 rgba(74,168,216,0.15) 快速闪烁
动画: 条纹位置随机变化 0.1s step-end infinite
触发: 添加 .holo-glitch class

## 组件玻璃态参数

组件	背景	模糊度	边框
侧边栏	rgba(10,22,40,0.7)	blur(20px) saturate(130%)	rgba(74,168,216,0.1)
顶栏	rgba(5,8,15,0.85)	blur(15px) saturate(120%)	rgba(74,168,216,0.1)
卡片	rgba(10,22,40,0.6)	blur(10px)	rgba(74,168,216,0.15)
输入框	rgba(10,22,40,0.5)	blur(12px) saturate(120%)	rgba(74,168,216,0.2)
按钮	rgba(232,118,42,0.25)	blur(8px)	rgba(232,118,42,0.3)
AI气泡	rgba(10,22,40,0.6)	blur(12px)	rgba(74,168,216,0.12)
用户气泡	rgba(232,118,42,0.15)	blur(12px)	rgba(232,118,42,0.2)
HUD面板	rgba(10,22,40,0.7)	blur(10px)	rgba(74,168,216,0.2)
