---
paths:
  - "**/*.js"
  - "**/*.jsx"
  - "**/*.mjs"
  - "**/*.cjs"
---

# JavaScript 编码规范

## 命名

- 变量和函数使用 camelCase 命名
- 类和构造函数使用 PascalCase 命名
- 常量使用 UPPER_SNAKE_CASE 命名
- 布尔值使用 is / has / should 前缀
- 事件处理函数使用 handle / on 前缀

## 格式

- 使用 2 个空格缩进
- 字符串使用单引号 插值场景使用模板字符串
- 必须加分号 不依赖 ASI 自动插入
- 单行宽度上限 100 字符

## 语法偏好

- 优先 const 其次 let 禁止使用 var
- 优先箭头函数 除非需要绑定 this
- 优先解构赋值而非逐个取值
- 用可选链 ?. 和空值合并 ?? 替代冗长的空值判断
- 遍历数组用 for...of 而非 for...in
- 用模板字面量替代字符串拼接

## 异步

- 优先使用 async / await 而非 Promise 链式调用
- 并发任务用 Promise.all 容错场景用 Promise.allSettled
- 禁止回调嵌套超过两层 超出必须重构
- 所有异步错误必须通过 try / catch 或 .catch 处理

## 模块

- 默认使用 ESM import / export 语法
- 优先具名导出而非默认导出
- 代码分割场景使用动态 import()
- 禁止循环依赖

## 质量

- 使用 === 严格相等 禁止使用 ==
- 避免隐式类型转换
- 优先使用 map / filter / reduce 而非手动循环
- 禁止修改函数参数 优先纯函数

## 紧凑格式

- 函数内不要有空行
- 两个块之间有一个空行
- 如果 if/for/do 的执行体只有一行 省略 {} 在同一行写出
- 如果 try/catch/function 只有一行执行体 在同一行写出
- 在不影响可读性的情况下尽可能减少行数
- 链式调用换行 多个链式调用前有一个缩进

## 文件块顺序

1. 文件头
2. import 块
3. type/struct 等大结构块
4. var/const 等变量块
5. function 块
