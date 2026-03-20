---
paths:
  - "**/*.ts"
  - "**/*.tsx"
  - "**/*.mts"
  - "**/*.cts"
---

# TypeScript 编码规范

> 继承 JavaScript 全部规范 以下为扩展和覆盖规则

## 命名

- 同 JavaScript 命名规则
- 类型和接口使用 PascalCase 命名
- 泛型参数使用单字母大写 T K V 或语义化名称 TResult TKey
- 枚举名称和成员均使用 PascalCase 命名

## 类型系统

- 对象形状优先用 interface 定义 联合/交叉/工具类型用 type
- 禁止使用 any 需要宽泛类型时用 unknown 并在使用前收窄
- 严格模式 strict: true 不可关闭
- 善用 as const 和 satisfies 收窄类型推断
- 禁止 @ts-ignore 改用 @ts-expect-error 并注明原因
- 用可区分联合建模状态 type State = { status: 'loading' } | { status: 'ok'; data: T }

## 泛型

- 泛型约束必须明确 T extends Base
- 禁止超过三层嵌套泛型 超出需重新设计
- 条件类型和映射类型仅用于工具类型库 业务代码保持简洁
- 用 infer 关键字提取嵌套类型

## 函数

- 参数和返回值都必须标注类型
- 重载签名从具体到宽泛排列
- 可选参数用 ? 而非 | undefined
- 超过 3 个参数改用 options 对象

## 枚举

- 优先字符串枚举而非数字枚举
- const enum 仅用于纯编译时常量
- 大量常量集合考虑用 as const 对象替代枚举

## 工具类型

- 善用内置工具类型 Partial Pick Omit Record Required
- 用 ReturnType 和 Parameters 提取函数签名
- 自定义工具类型统一放在 types/ 目录

## 模块

- .d.ts 声明文件仅用于无类型的第三方库
- 用 barrel export (index.ts) 控制模块公共 API
- 类型导入必须使用 import type

> 继承 JavaScript 紧凑格式和文件块顺序规范
