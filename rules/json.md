---
paths:
  - "**/*.json"
  - "**/*.jsonc"
  - "**/*.json5"
---

# JSON 书写规范

## 格式

- 2 空格缩进
- UTF-8 编码
- 文件末尾换行
- 不允许尾随逗号
- 不允许注释 需要注释用 JSONC 或 JSON5

## 命名

- 键名 camelCase 为默认风格
- 与后端 API 对接时跟随后端风格 如 snake_case
- 键名用双引号包裹
- 布尔键用 is/has 前缀

## 值

- 字符串用双引号
- 数值不加引号
- 布尔值 true/false 不用 0/1 替代
- 空值用 null 不用空字符串
- 日期用 ISO 8601 格式 如 2024-01-01T00:00:00Z
- 枚举值用字符串 不用数字编码

## 结构

- 数组元素类型一致
- 嵌套不超过 4 层
- 大型配置按功能分文件
- 保持键的顺序稳定 方便 diff

## 配置文件

- package.json 键顺序遵循社区惯例 name > version > description > main > scripts > dependencies
- tsconfig.json 启用 strict 模式
- 敏感信息不入库 用环境变量替代
