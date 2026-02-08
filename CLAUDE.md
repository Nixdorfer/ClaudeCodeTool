# 风格
- 只显示待办事项和关键结论 不显示思考/推理过程
- 如果表达不明确 请提供选项而不是猜测
- 如果我的需求并非最优 请先提出更优方案
- 如果已有库 请直接命名而不是手动编写

# 代码
- 不使用注释
- 将共享代码提取到独立的库中
- 使用单一用途的文件；避免代码臃肿
- 优先使用通用代码 + 配置注入 而非硬编码特殊情况
- 展示给用的内容使用中文 否则使用英文
- 使用尽可能简短的 节省token的语句
- 不要写任何标点 用一个空格来替代 用/替代、

# 工作流程
- 优先使用skill:code-RAG代替grep/read
- 处理复杂任务前先在.claude/plans/目录下生成md计划
- 派发3个或更多SubAgent时 使用并行workflow
  1. 派发N个Worker SubAgent(run_in_background=true)收集所有 task_id
  2. 在同一消息中 并行调用N个TaskOutput(id, block=true, timeout=600000)
  3. 所有SubAgent返回后 主Agent继续执行