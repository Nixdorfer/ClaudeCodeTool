- 我不是专业人士 如果我提出的要求并不是最优解 告知我更好的方案是什么
- 多subagent并行工作流 (当需要派发3个以上subagent时必须使用):
  1. 派发N个worker subagent (run_in_background=true), 收集所有task_id
  2. 派发1个Bash supervisor subagent (非background), 命令为:
     `powershell -File C:/Users/Nix/.claude/supervisor/poll.ps1 -TaskIds "id1","id2","id3" -TimeoutSeconds 600`
     supervisor会每秒轮询所有worker的output文件, 全部完成后输出汇总并退出
  3. 主agent阻塞等待supervisor返回 (supervisor本身就是阻塞调用)
  4. supervisor返回后, 主agent用 TaskOutput 逐个读取各worker结果, 然后继续工作
  - 脚本: ~/.claude/supervisor/poll.ps1 (轮询) + parse-result.ps1 (解析单个worker输出)
  - poll.ps1输出格式: 首行DONE/TIMEOUT, 后续每行 OK|id 或 FAIL|id|错误数|首条错误
- 代码不要写注释
- 使用简体中文回答问题
- 在多个模块中复用的代码单独提取出来形成一个库
- 每份文件确保功能完整性和单一性 单个文件内完整实现某一项功能 同时不包含其他功能的代码 不要让一份文件的代码过多
- 少使用专用代码(即某个代码只针对于少量特例起作用) 多使用泛化代码+解耦合配置注入
- 如果我的要求可以通过调用某个库来实现 请告知我
- 只在必要情况下解释运行和思考路径 否则不需要向我持续汇报 只展示todo即可