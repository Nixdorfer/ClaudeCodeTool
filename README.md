# Claude Code 工具包安装指南

## 第一步 安装VSCode

1. 打开浏览器 访问 https://code.visualstudio.com
2. 点击页面上的大按钮下载安装包
3. 双击下载的文件 一路点"下一步"完成安装

## 第二步 在VSCode中安装Claude Code

1. 打开VSCode
2. 点左边栏的方块图标(扩展) 或按 `Ctrl+Shift+X`
3. 搜索框输入 `Claude Code`
4. 找到 Anthropic 发布的那个 点 `Install`
5. 安装完成后左边栏出现Claude图标 点击即可使用
6. 首次使用需要登录Anthropic账号

## 第三步 安装工具包环境

需要先安装 Python 3.11+ (https://python.org)

右键 `setup.ps1` 选择"使用 PowerShell 运行" 等待完成即可

## 第四步 为项目启用code-RAG

将 `mcp/code-RAG/.mcp.json` 复制到你的项目根目录

按你的需求修改其中的
- `ragIgnoreDirs` - 不需要索引的文件夹
- `ragLibs` - 额外需要索引的目录
一般而言 你不需要额外配置