---
paths:
  - "**/*.php"
---

# PHP 编码规范

## 命名

- PSR-12 标准为基础
- PascalCase 用于类名 接口 trait 枚举
- camelCase 用于方法名和变量名
- UPPER_SNAKE_CASE 用于常量
- 命名空间对应目录结构

## 格式

- 4 空格缩进
- 行宽 120 字符
- 类和方法的花括号换行 控制语句花括号同行
- 每个文件必须有 `declare(strict_types=1)` 严格类型声明
- 纯 PHP 文件只用 `<?php` 不加结束标签 `?>`

## 类型

- 参数和返回值必须声明类型
- 联合类型 `string|int` 优于 `mixed`
- 可空类型用 `?Type` 不用 `Type|null`
- 用 `enum` 替代常量组
- `readonly` 标记不可变属性

## 错误处理

- 异常优先于错误码
- 自定义异常类按业务分类
- `try/catch` 精确捕获 不用 `Exception` 兜底
- `finally` 块做资源清理

## 架构

- 依赖注入容器管理对象
- 接口驱动 面向抽象编程
- Repository 模式访问数据层
- DTO 传输数据 不用数组传参
- Service 层放业务逻辑

## 安全

- PDO 预处理语句 禁止拼接 SQL
- `htmlspecialchars` 输出转义
- 表单验证 CSRF token
- 密码用 `password_hash` / `password_verify`
- 过滤并验证所有外部输入

## 现代特性

- 箭头函数 `fn() =>` 用于简短闭包
- `match` 表达式替代 `switch`
- 命名参数提高可读性
- Fiber 协程处理并发
- `Attribute` 替代注释注解
