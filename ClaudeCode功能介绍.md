# Claude Code 完整特性指南

## 目录

1. [CLAUDE.md 指令系统](#1-claudemd-指令系统)
2. [Settings 配置文件](#2-settings-配置文件)
3. [Permission 权限系统](#3-permission-权限系统)
4. [Hooks 生命周期钩子](#4-hooks-生命周期钩子)
5. [MCP 服务器配置](#5-mcp-服务器配置)
6. [Subagents 自定义子代理](#6-subagents-自定义子代理)
7. [Plugins 插件系统](#7-plugins-插件系统)
8. [Skills 技能](#8-skills-技能)
9. [Keybindings 快捷键](#9-keybindings-快捷键)
10. [Slash Commands 斜杠命令](#10-slash-commands-斜杠命令)
11. [Memory 记忆系统](#11-memory-记忆系统)
12. [Background Tasks 后台任务](#12-background-tasks-后台任务)
13. [Extended Thinking 深度思考](#13-extended-thinking-深度思考)
14. [Vim Mode](#14-vim-mode)
15. [IDE 集成](#15-ide-集成)
16. [Cloud Providers 云服务商](#16-cloud-providers-云服务商)
17. [Environment Variables 环境变量](#17-environment-variables-环境变量)
18. [特殊文件完整索引](#18-特殊文件完整索引)

---

## 1. CLAUDE.md 指令系统

Claude Code 启动时自动加载的指令文件，用于注入项目规范、编码风格、工作流约束等。

### 文件层级（优先级从高到低）

| 文件路径 | 作用域 | 是否提交版控 |
|---------|--------|------------|
| 托管策略目录下的 `CLAUDE.md` | 组织强制 | 由管理员控制 |
| `.claude/CLAUDE.md` 或 `./CLAUDE.md` | 项目共享 | 是 |
| `.claude/rules/*.md` | 项目模块化规则 | 是 |
| `~/.claude/CLAUDE.md` | 用户全局 | - |
| `.claude.local.md` | 项目私密 | 否（自动 gitignore） |
| Auto Memory `MEMORY.md` | 自动学习 | - |

### @import 语法

在 CLAUDE.md 中引用其他文件：

```markdown
@README.md                        # 相对项目根目录
@docs/architecture.md             # 相对路径
@~/.claude/company-standards.md   # 用户 home 目录
@//C:/absolute/path.md            # 绝对路径
```

### .claude/rules/ 条件规则

可通过 YAML 前置声明限定规则的适用文件范围：

```markdown
---
paths:
  - "src/**/*.ts"
  - "tests/**/*.test.ts"
---

所有 TypeScript 文件必须使用 strict 模式。
```

无前置声明的 `.md` 文件会无条件加载。

### 典型场景

- 统一团队编码风格（缩进、命名、注释规范）
- 声明项目架构约束（"逻辑写 Rust，渲染写 TS"）
- 注入 i18n、安全审查等工作流要求
- 通过 rules/ 对不同目录施加不同规则

---

## 2. Settings 配置文件

### 文件位置与优先级（高→低）

| 优先级 | 路径 | 说明 |
|-------|------|------|
| 1 | 托管策略 `managed-settings.json` | 组织强制，不可覆盖 |
| 2 | CLI 参数 `--model sonnet` | 会话级 |
| 3 | `.claude/settings.local.json` | 项目本地，不提交 |
| 4 | `.claude/settings.json` | 项目共享，提交到版控 |
| 5 | `~/.claude/settings.json` | 用户全局 |

### 完整 Schema 示例

```json
{
  "defaultMode": "default",
  "permissions": {
    "allow": ["Bash(npm run *)", "Read"],
    "deny": ["Bash(rm -rf *)"]
  },
  "model": "claude-opus-4-6",
  "alwaysThinkingEnabled": false,
  "env": {
    "NODE_ENV": "development"
  },
  "apiKeyHelper": "/bin/get-api-key.sh",
  "hooks": { },
  "sandbox": {
    "enabled": true,
    "autoAllowBashIfSandboxed": true
  },
  "additionalDirectories": ["/path/to/shared/code"],
  "language": "english",
  "outputStyle": "Explanatory"
}
```

### 典型场景

- 项目统一权限规则（提交 `settings.json`）
- 本地开发覆盖（`settings.local.json` 中放个人偏好）
- 组织级安全策略（managed-settings 禁用 bypassPermissions）

---

## 3. Permission 权限系统

细粒度控制 Claude 可以使用哪些工具、访问哪些文件。

### 权限模式

| 模式 | 行为 |
|------|------|
| `default` | 标准交互确认 |
| `acceptEdits` | 自动接受文件编辑，其他仍需确认 |
| `plan` | 只读探索，不修改任何文件 |
| `dontAsk` | 不确认=自动拒绝 |
| `bypassPermissions` | 跳过所有权限检查（慎用） |
| `delegate` | Agent Team 协调模式 |

### 规则语法

```json
{
  "permissions": {
    "allow": [
      "Bash(npm run *)",
      "Read",
      "Edit(/src/**/*.ts)",
      "WebFetch(domain:github.com)",
      "mcp__github__*",
      "Task(Explore)"
    ],
    "deny": [
      "Bash(rm -rf *)",
      "Read(.env*)"
    ]
  }
}
```

**路径匹配规则**：
- `/path` — 相对 settings 文件
- `./path` — 相对当前目录
- `~/path` — home 目录
- `//path` — 绝对路径
- `**` `*` — glob 通配符

**评估顺序**: deny → ask → allow（首个匹配即停止）

### 典型场景

- 允许所有 `npm run` 但禁止 `rm -rf`
- 禁止读取 `.env` 等敏感文件
- 只允许特定 MCP 工具
- 限制子代理的工具访问

---

## 4. Hooks 生命周期钩子

在 Claude 的工作流中特定时刻自动运行命令、提示或代理。

### 14 个生命周期事件

| 事件 | 触发时机 | 可阻止 |
|------|---------|-------|
| `SessionStart` | 会话开始/恢复 | 否 |
| `UserPromptSubmit` | 用户发送提示前 | 是 |
| `PreToolUse` | 工具调用前 | 是 |
| `PostToolUse` | 工具调用成功后 | 是 |
| `PostToolUseFailure` | 工具调用失败 | 否 |
| `PermissionRequest` | 权限对话出现 | 是 |
| `Notification` | 发送通知 | 否 |
| `SubagentStart` | 子代理启动 | 否 |
| `SubagentStop` | 子代理完成 | 是 |
| `Stop` | Claude 完成响应 | 是 |
| `TeammateIdle` | Agent Team 成员空闲 | 是 |
| `TaskCompleted` | 任务标记完成 | 是 |
| `PreCompact` | 上下文压缩前 | 否 |
| `SessionEnd` | 会话结束 | 否 |

### 三种 Hook 类型

**Command** — 执行 shell 命令：
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "npx prettier --write $(jq -r '.tool_input.file_path')",
            "timeout": 600
          }
        ]
      }
    ]
  }
}
```

**Prompt** — 单轮 LLM 判断：
```json
{
  "type": "prompt",
  "prompt": "Check if the output contains sensitive data: $ARGUMENTS",
  "model": "haiku",
  "timeout": 30
}
```

**Agent** — 多轮子代理验证：
```json
{
  "type": "agent",
  "prompt": "Run tests and verify all pass: $ARGUMENTS",
  "timeout": 120
}
```

### Matcher 模式

```json
"matcher": "Bash"                 // 精确匹配
"matcher": "Edit|Write"           // 正则 OR
"matcher": "mcp__github__.*"      // MCP 工具匹配
"matcher": "compact"              // SessionStart: startup|resume|clear|compact
```

### Exit Code

| 退出码 | 含义 |
|--------|------|
| 0 | 允许，处理 JSON 输出 |
| 2 | 阻止操作，stderr 作为反馈 |
| 其他 | 非阻塞错误 |

### 典型场景

- 每次写文件后自动 format（PostToolUse + prettier）
- 提交前自动 lint 检查（PreToolUse + matcher: Bash + eslint）
- 会话启动时自动拉取最新代码（SessionStart）
- 响应结束后自动验证测试通过（Stop + agent hook）
- 异步运行长时间测试（`async: true`）

---

## 5. MCP 服务器配置

Model Context Protocol — 为 Claude 扩展外部工具和数据源。

### .mcp.json（项目级）

```json
{
  "code-RAG": {
    "type": "stdio",
    "command": "node",
    "args": ["path/to/server.js"],
    "env": {
      "DB_PATH": ".claude/mcp/code-RAG"
    }
  },
  "github": {
    "type": "http",
    "url": "http://localhost:3000"
  },
  "slack": {
    "type": "sse",
    "url": "http://localhost:3001"
  }
}
```

支持 `${ENV_VAR}` 语法展开环境变量。

### 传输类型

| 类型 | 说明 |
|------|------|
| `stdio` | 标准输入输出，最常用 |
| `http` | HTTP 流式传输 |
| `sse` | Server-Sent Events |

### 管理命令

```bash
/mcp                    # 交互式管理
claude mcp add <name>   # CLI 添加
claude mcp remove <name>
claude mcp list
```

### 典型场景

- 代码搜索（code-RAG）
- GitHub PR/Issue 操作
- 数据库查询
- Slack 消息发送
- 自定义业务 API 接入

---

## 6. Subagents 自定义子代理

独立的 AI 代理，拥有自己的工具集、权限和记忆。

### 文件位置

```
.claude/agents/        # 项目级
~/.claude/agents/      # 用户全局
```

### 完整 YAML 配置

```yaml
---
name: code-reviewer
description: >
  审查代码质量和安全性。代码变更后自动使用。
model: sonnet
permissionMode: default
maxTurns: 50
tools: Read, Grep, Glob, Bash
disallowedTools: Write, Edit
memory: project
skills:
  - code-review-rules
mcpServers:
  github: {}
hooks:
  Stop:
    - hooks:
        - type: prompt
          prompt: "All issues found?"
---

You are a senior code reviewer. For each change:
1. Check for security vulnerabilities
2. Verify error handling
3. Assess test coverage
4. Suggest improvements
```

### 配置字段说明

| 字段 | 类型 | 说明 |
|------|------|------|
| `name` | string | 代理名称 |
| `description` | string | 描述（含"proactively"时会主动触发） |
| `model` | sonnet/opus/haiku/inherit | 使用的模型 |
| `permissionMode` | string | 权限模式 |
| `maxTurns` | number | 最大交互轮次 |
| `tools` | string | 允许使用的工具，逗号分隔 |
| `disallowedTools` | string | 禁止使用的工具 |
| `memory` | user/project/local | 持久记忆作用域 |
| `skills` | string[] | 附加技能 |
| `mcpServers` | object | 可用的 MCP 服务器 |
| `hooks` | object | 代理专属 hooks |

### 代理记忆

设置 `memory: project` 后，代理会在以下目录维护持久记忆：
```
.claude/agent-memory/<agent-name>/
├── MEMORY.md
├── patterns.md
└── troubleshooting.md
```

### 典型场景

- **code-reviewer**: 代码审查代理，只有读权限，检查安全和质量
- **debugger**: 调试代理，可运行测试和读日志
- **architect**: 架构分析代理，只读探索模式
- **migrator**: 数据库迁移代理，限定特定工具

---

## 7. Plugins 插件系统

可打包、分发和共享的 Claude Code 扩展。

### 目录结构

```
my-plugin/
├── .claude-plugin/
│   └── plugin.json         # 插件清单
├── commands/               # 技能（model-invoked）
│   └── review/
│       └── SKILL.md
├── skills/                 # 用户可调用技能
│   └── format/
│       └── SKILL.md
├── agents/                 # 子代理
│   └── reviewer.md
├── hooks/                  # Hooks
│   └── hooks.json
├── .mcp.json               # MCP 服务器
├── .lsp.json               # LSP 服务器
└── README.md
```

### plugin.json

```json
{
  "name": "my-plugin",
  "displayName": "My Custom Plugin",
  "description": "Adds code review and formatting",
  "version": "1.0.0",
  "author": { "name": "Your Name" },
  "license": "MIT",
  "components": {
    "skills": "skills/",
    "commands": "commands/",
    "agents": "agents/",
    "hooks": "hooks/",
    "mcpServers": ".mcp.json",
    "lspServers": ".lsp.json"
  }
}
```

### .lsp.json（语言服务器集成）

```json
{
  "rust": {
    "command": "rust-analyzer",
    "extensionToLanguage": { ".rs": "rust" }
  }
}
```

### 加载方式

```bash
claude --plugin-dir ./my-plugin
claude --plugin-dir ./plugin1 --plugin-dir ./plugin2
```

插件内技能使用命名空间调用：`/my-plugin:skill-name`

### 典型场景

- 公司内部开发规范插件（lint + format + review hooks）
- 特定框架支持插件（如 React/Vue/Rust 专用工具链）
- CI/CD 集成插件（GitHub Actions + 部署 hooks）

---

## 8. Skills 技能

Claude 可调用的专用知识和工作流模块。

### 文件位置

```
.claude/commands/       # 项目级
~/.claude/commands/     # 用户全局
```

### SKILL.md 格式

```markdown
---
name: commit
description: Smart git commit with conventional format
model: haiku
tools: Bash, Read, Grep
---

You are a git commit assistant. Steps:
1. Run `git status` and `git diff --cached`
2. Analyze changes
3. Generate conventional commit message
4. Execute commit
```

### 调用方式

```
/commit                   # 用户在聊天中输入
/my-plugin:commit         # 插件命名空间
```

### 典型场景

- `/commit` — 智能 git 提交
- `/review-pr` — PR 审查
- `/coding` — 代码规范加载
- `/fetch-spa` — 抓取 SPA 页面
- 自定义项目特有的工作流

---

## 9. Keybindings 快捷键

### 配置文件

`~/.claude/keybindings.json`

### 17 个 Context

Global, Chat, Autocomplete, Confirmation, HistorySearch, Transcript, Task, Help, ThemePicker, Tabs, Attachments, Footer, MessageSelector, DiffDialog, ModelPicker, Select, Plugin

### 配置示例

```json
{
  "bindings": [
    {
      "context": "Global",
      "bindings": {
        "ctrl+c": "app:interrupt",
        "ctrl+d": "app:exit",
        "ctrl+t": "app:toggleTodos"
      }
    },
    {
      "context": "Chat",
      "bindings": {
        "enter": "chat:submit",
        "ctrl+g": "chat:externalEditor",
        "ctrl+k ctrl+s": "chat:stash"
      }
    }
  ]
}
```

### 支持的按键格式

```
ctrl+s            # 单修饰符
ctrl+shift+p      # 多修饰符
ctrl+k ctrl+s     # Chord（按键序列）
K                 # 大写 = Shift+K
"ctrl+s": null    # 解除绑定
```

### 典型场景

- 重新绑定 submit 键（Enter → Ctrl+Enter）
- 添加 Chord 快捷键（Ctrl+K Ctrl+F 格式化）
- Vim 用户自定义导航键

---

## 10. Slash Commands 斜杠命令

### 完整命令列表

| 命令 | 功能 | 使用场景 |
|------|------|---------|
| `/help` | 显示帮助 | 查看可用命令 |
| `/clear` | 清除会话 | 重新开始对话 |
| `/compact` | 压缩上下文 | 接近 token 上限时手动压缩 |
| `/resume` | 恢复历史会话 | 继续之前中断的工作 |
| `/rewind` | 回退到检查点 | 操作出错需要回滚 |
| `/checkpoint` | 创建检查点 | 重要操作前保存状态 |
| `/model` | 切换模型 | 在 Opus/Sonnet/Haiku 间切换 |
| `/fast` | 切换快速模式 | 同模型加速输出 |
| `/config` | 打开配置 | 编辑 settings |
| `/permissions` | 管理权限 | 查看/修改工具权限 |
| `/memory` | 编辑记忆 | 修改 CLAUDE.md 或 MEMORY.md |
| `/init` | 初始化项目 | 新项目创建 CLAUDE.md |
| `/hooks` | 管理 hooks | 添加/编辑/删除钩子 |
| `/agents` | 管理子代理 | 创建/查看自定义代理 |
| `/plugin` | 管理插件 | 安装/配置插件 |
| `/mcp` | 管理 MCP | 添加/删除 MCP 服务器 |
| `/vim` | Vim 模式 | 切换 vi 编辑模式 |
| `/plan` | 计划模式 | 进入只读规划模式 |
| `/tasks` | 后台任务 | 查看运行中的任务 |
| `/todos` | 待办列表 | 查看任务进度 |
| `/task` | 创建后台任务 | 启动新的后台任务 |
| `/teams` | Agent Teams | 管理代理团队 |
| `/cost` | 显示成本 | 查看当前会话消耗 |
| `/stats` | 统计信息 | 查看使用统计 |
| `/doctor` | 诊断问题 | 排查配置/连接问题 |
| `/debug` | 调试模式 | 查看详细运行信息 |
| `/bug` | 报告 bug | 提交问题报告 |
| `/feedback` | 反馈 | 发送使用反馈 |
| `/version` | 版本号 | 查看 Claude Code 版本 |
| `/export` | 导出对话 | 导出当前会话记录 |
| `/copy` | 复制输出 | 复制最后一条回复 |
| `/add-dir` | 添加目录 | 会话中添加额外工作目录 |
| `/keybindings` | 快捷键 | 编辑快捷键配置 |
| `/statusline` | 状态行 | 配置底部状态栏 |
| `/rename` | 重命名会话 | 修改当前会话名称 |
| `/settings` | 设置 | 打开设置编辑器 |

---

## 11. Memory 记忆系统

Claude Code 具有跨会话持久记忆能力。

### Auto Memory

位置：`~/.claude/projects/<project-hash>/memory/`

```
memory/
├── MEMORY.md        # 主索引（前200行自动载入 system prompt）
├── patterns.md      # 项目模式
├── debugging.md     # 调试经验
└── architecture.md  # 架构笔记
```

Claude 会在工作过程中自动学习并写入这些文件。可通过 `/memory` 手动编辑。

### 子代理记忆

```
.claude/agent-memory/<agent-name>/MEMORY.md
~/.claude/agent-memory/<agent-name>/MEMORY.md
```

### 禁用自动记忆

```bash
CLAUDE_CODE_DISABLE_AUTO_MEMORY=1
```

### 典型场景

- 自动记住常犯错误的修复方式
- 记录项目架构决策
- 跨会话积累调试经验
- 子代理独立学习项目特定知识

---

## 12. Background Tasks 后台任务

### 使用方式

```
Ctrl+B     # 将当前任务转入后台
/tasks     # 查看所有后台任务
/task      # 创建新后台任务
```

### 特性

- 并发执行，不阻塞主会话
- 权限在启动时预批准
- 完成后输出返回主会话
- 不支持 MCP 工具调用

### 典型场景

- 长时间运行的测试套件
- 大规模代码重构
- 并行处理多个独立任务
- 后台持续监控构建状态

---

## 13. Extended Thinking 深度思考

### 开启方式

```
Cmd+T / Meta+T   # 快捷键切换
/model            # 在模型选择中调整
```

或在配置中永久开启：
```json
{
  "alwaysThinkingEnabled": true
}
```

### 典型场景

- 复杂架构设计决策
- 多文件关联的 bug 分析
- 复杂算法实现
- 需要深度推理的代码审查

---

## 14. Vim Mode

### 开启

```
/vim              # 切换 Vim 模式
```

### 支持的操作

| 类别 | 命令 |
|------|------|
| 模式切换 | `i` `a` `o` `Esc` `v` |
| 移动 | `h` `j` `k` `l` `w` `b` `e` `$` `^` `0` `gg` `G` |
| 编辑 | `d` `c` `y` `p` `x` `r` `u` `Ctrl+R` |
| 文本对象 | `iw` `aw` `i(` `a(` `i{` `a{` `i"` `a"` |
| 搜索 | `/pattern` `?pattern` `n` `N` |

### 典型场景

- Vim 用户保持肌肉记忆的输入习惯
- 快速编辑长输入内容

---

## 15. IDE 集成

### VS Code Extension

- 嵌入式终端面板
- 多会话管理
- 后台任务监控
- Git diff 可视化
- 文件链接点击跳转（`[file.ts:42](src/file.ts#L42)`）
- 用户选中代码作为上下文

### JetBrains Plugin

- 支持 IntelliJ、PyCharm、WebStorm 等全系列
- 侧边栏工具窗口
- 选中代码上下文

### Desktop App

- 并行多会话
- Diff 查看器
- 远程任务管理

### GitHub Actions / GitLab CI

- CI/CD 中运行 Claude Code
- 自动 PR 审查和修复

### 典型场景

- VS Code 中边写代码边与 Claude 协作
- CI 流水线中自动代码审查
- GitHub Issue 自动分析和修复

---

## 16. Cloud Providers 云服务商

### Amazon Bedrock

```json
{
  "apiProvider": "bedrock",
  "model": "claude-opus-4-6",
  "awsRegion": "us-east-1"
}
```

### Google Vertex AI

```json
{
  "apiProvider": "vertexai",
  "model": "claude-opus-4-6",
  "vertexaiProjectId": "my-project",
  "vertexaiRegion": "us-central1"
}
```

### Microsoft Foundry

```json
{
  "apiProvider": "foundry",
  "model": "claude-opus-4-6"
}
```

### LLM Gateway (LiteLLM)

用于代理和负载均衡。

### 典型场景

- 企业内部合规要求使用特定云服务商
- 通过企业 IAM 管理 API 访问
- 多区域部署降低延迟

---

## 17. Environment Variables 环境变量

| 变量 | 说明 |
|------|------|
| `ANTHROPIC_API_KEY` | API 密钥 |
| `ANTHROPIC_MODEL` | 覆盖默认模型 |
| `CLAUDE_CODE_SHELL` | 指定 shell |
| `CLAUDE_CODE_DISABLE_AUTO_MEMORY` | 禁用自动记忆 |
| `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS` | 禁用后台任务 |
| `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` | 压缩阈值（如 50 = 50%时压缩） |
| `CLAUDE_CODE_ENABLE_TELEMETRY` | 启用遥测 |
| `CLAUDE_ENV_FILE` | Hooks 环境变量持久化文件 |
| `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD` | 额外 CLAUDE.md 搜索目录 |

---

## 18. 特殊文件完整索引

### 指令文件

| 文件 | 用途 |
|------|------|
| `~/.claude/CLAUDE.md` | 用户全局指令 |
| `.claude/CLAUDE.md` | 项目共享指令 |
| `./CLAUDE.md` | 项目根指令（等同上） |
| `.claude.local.md` | 项目私密指令 |
| `.claude/rules/*.md` | 模块化条件规则 |

### 配置文件

| 文件 | 用途 |
|------|------|
| `~/.claude/settings.json` | 用户全局设置 |
| `.claude/settings.json` | 项目共享设置 |
| `.claude/settings.local.json` | 项目本地设置 |
| `~/.claude/keybindings.json` | 快捷键 |
| `~/.claude.json` | 凭证、MCP 缓存 |
| `.mcp.json` | 项目 MCP 配置 |

### 代理和记忆

| 路径 | 用途 |
|------|------|
| `.claude/agents/*.md` | 项目子代理 |
| `~/.claude/agents/*.md` | 用户全局子代理 |
| `.claude/commands/*.md` | 项目技能 |
| `~/.claude/commands/*.md` | 用户全局技能 |
| `~/.claude/projects/<hash>/memory/` | 自动记忆 |
| `.claude/agent-memory/<name>/` | 项目子代理记忆 |
| `~/.claude/agent-memory/<name>/` | 用户子代理记忆 |

### 插件

| 路径 | 用途 |
|------|------|
| `.claude-plugin/plugin.json` | 插件清单 |
| `.claude-plugin/` 下的子目录 | commands/ skills/ agents/ hooks/ |
| `.lsp.json` | 语言服务器配置 |

### 托管策略（组织级）

| 路径（macOS 示例） | 用途 |
|-------------------|------|
| `/Library/Application Support/ClaudeCode/managed-settings.json` | 强制设置 |
| `/Library/Application Support/ClaudeCode/managed-mcp.json` | 强制 MCP |
| `/Library/Application Support/ClaudeCode/CLAUDE.md` | 强制指令 |
