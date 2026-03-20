---
paths:
  - "**/*.yml"
  - "**/*.yaml"
---

# YAML 书写规范

## 格式

- 2 空格缩进 禁用 Tab
- UTF-8 编码
- 文件以 --- 开头标记文档
- 多文档用 --- 分隔 ... 结束
- 行宽 120 字符

## 命名

- 键名 kebab-case 或 snake_case 项目内统一
- 避免特殊字符做键名
- 布尔键用 is/has 前缀

## 值

- 字符串不加引号 除非含特殊字符
- 含冒号/井号的字符串必须引号包裹
- 布尔值用 true/false 不用 yes/no on/off
- 多行字符串用 | 保留换行 > 折叠换行
- 锚点 & 和别名 * 减少重复

## 结构

- 列表项 - 后加空格
- 嵌套映射缩进一致
- 空值显式写 null 或省略值
- 注释 # 后加空格 说明非显而易见的配置

## 场景特定

- Docker Compose 服务按字母排序
- Kubernetes 资源 apiVersion > kind > metadata > spec
- CI/CD 流水线阶段顺序反映执行流程
- GitHub Actions 用 env 集中管理变量

## 安全

- 密钥不硬编码 用密钥管理服务引用
- 引用环境变量用 ${VAR} 语法
- .yamllint 做格式校验
