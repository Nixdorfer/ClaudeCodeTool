---
paths:
  - "**/*.toml"
---

# TOML 书写规范

## 格式

- 2 空格缩进 或不缩进 表头层级靠表头路径表达
- UTF-8 编码
- 文件末尾换行
- 每个键值对独占一行

## 命名

- 键名 kebab-case 为推荐风格
- 表名 用方括号 [table]
- 数组表 用双方括号 [[array]]
- 键名不需要引号 除非含特殊字符

## 值

- 字符串用双引号 多行用三引号
- 字面量字符串用单引号 不转义
- 日期时间用 RFC 3339 格式
- 整数可用下划线分隔 1_000_000
- 布尔值 true/false 小写

## 结构

- 相关配置放在同一个表下
- 表的顺序 顶层元数据 > 主要配置 > 次要配置
- 内联表 {} 仅用于简短的少量键值
- 注释放在被注释项的上方

## Rust 项目 Cargo.toml

- [package] 在最前 name > version > edition > description
- [dependencies] 按字母排序
- 版本号用语义化版本 "1.2" 不用 "*"
- workspace 成员按功能分组
- features 显式声明 不依赖隐式传递

## Python 项目 pyproject.toml

- [project] 遵循 PEP 621
- [tool.xxx] 工具配置统一放在 pyproject.toml
- 依赖版本约束明确 >= 和 < 组合
