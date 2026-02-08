# Claude Code(CC) 工具包安装指南

## 第一步 安装VSCode

1. 点击蓝字下载VSCode [点我下载](https://vscode.download.prss.microsoft.com/dbazure/download/stable/bdd88df003631aaa0bcbe057cb0a940b80a476fa/VSCodeUserSetup-x64-1.109.0.exe)
2. 双击下载的文件 一路点"下一步"完成安装

## 第二步 在VSCode中安装CC

1. 打开VSCode
2. 按下 `Ctrl+Shift+X`
3. 搜索框输入 `Claude Code`
4. 找到 Anthropic 发布的那个 点 `Install`
5. 安装完成后右上角出现Claude图标 点击即可开始新对话
6. 首次使用需要登录Anthropic账号(需要科学上网)

## 第三步 安装工具包环境

1. 点击蓝字下载Python 3.11 [点我下载](https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe)
2. 右键 `初始化环境.ps1` 选择"使用 PowerShell 运行" 等待完成即可

## 第四步 为项目启用code-RAG

1. 先关闭打开了这个项目的VSCode
2. 将 `.mcp.json` 复制到你的项目根目录
3. 在VSCode中打开这个项目 它会自动加载
4. 第一次运行时 请在CC的对话窗口输入 `初始化code-RAG索引`
5. 你可以在 `项目根目录\.claude\CLAUDE.md` 中添加以下内容
   ```
   - skill:code-RAG enabled
   - skill:coding enabled
   ```
   来强制启用code-RAG

## code-RAG语法解析说明

code-RAG支持基于tree-sitter的语法分割 目前各语言支持情况如下

### 完整解析索引
| 语言 | 扩展名 |
|------|--------|
| rust | .rs |
| typescript | .ts .tsx |
| javascript | .js .jsx |
| vue | .vue |
| python | .py |
| c | .c .h |
| cpp | .cpp .hpp .cc .cxx .hxx |
| csharp | .cs |
| go | .go |
| php | .php |
| java | .java |
| kotlin | .kt .kts |
| scala | .scala |
| ruby | .rb |
| lua | .lua |
| elixir | .ex .exs |
| haskell | .hs |
| r | .r .R |
| julia | .jl |
| perl | .pl .pm |
| bash | .sh .bash |
| objective_c | .m .mm |

### 有限解析索引
| 语言 | 扩展名 | 说明 |
|------|--------|------|
| sql | .sql | 无符号提取 |
| makefile | .mk + Makefile等文件名 | 有限 |
| dockerfile | Dockerfile文件名 | 无符号提取 |
| ocaml | .ml .mli | 有限 |
| erlang | .erl .hrl | 有限 |

### 纯文本索引
| 语言 | 扩展名 |
|------|--------|
| swift | .swift |
| dart | .dart |
| zig | .zig |
| nim | .nim |
| proto | .proto |
| glsl | .glsl .vert .frag .comp .geom .tesc .tese |
| wgsl | .wgsl |
| hlsl | .hlsl |
| asm | .s .S .asm |
| toml | .toml |
| json | .json |
| yaml | .yaml .yml |
| markdown | .md |
| html | .html |
| css | .css |
| scss | .scss |

## .mcp.json配置详情

一般而言 使用默认配置即可 但是你也可以通过修改项目中的 `.mcp.json` 来进行自定义配置

| 字段 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `ragIgnoreDirs` | `string[]` | `["node_modules", ".git", "target", "dist", "build", "__pycache__", ".cache", "pkg", "wasm-pack-out", ".claude", "venv", ".venv", "env", ".env", "runtime", ".idea", ".vscode", ".next", "coverage", ".nyc_output", ".turbo"]` | 排除目录名 |
| `ragIgnore` | `string[]` | `null` | gitignore风格排除模式 支持通配符 |
| `ragLibs` | `string[]` | `[]` | 外部库目录路径(相对项目根) |
| `ragMaxFileSize` | `number` | `256` | 最大文件大小(KB) |

关于文件如何被排除
- 执行顺序
  1. ragIgnoreDirs
  2. ragLibs排除
  3. 扩展名/文件名检查
  4. 语言过滤
  5. 文件大小限制
  6. ragIgnore
- ragIgnoreDirs和ragIgnore的关键区别
  - ragIgnoreDirs 只能匹配文件夹 不支持通配符 但效率高 直接跳过整棵子树
  - ragIgnore 匹配文件的相对路径 支持gitignore语法 但逐文件检查
- ragLibs的典型使用场景为项目中使用了其他大型外部库(例如diffusers chatterbox等)会带来大量的索引文件 拖慢查找速度 但是你又要调用它的接口 因此不希望CC完全忽略掉其中的代码
- 一个文件夹被加入外部库后 main将排除其中的内容 单独创建一个RAG储存其中的代码 CC将在需要查看其中代码时 自动声明查找位置