---
paths:
  - "**/*.rs"
---

# Rust 编码规范

## 命名

- 变量 函数 模块 文件名使用 snake_case
- 类型 trait 枚举使用 PascalCase
- 常量和静态变量使用 SCREAMING_SNAKE_CASE
- 生命周期参数默认用 'a 'b 有语义时用 'ctx 'conn 'buf
- 布尔变量和函数以 is_ has_ can_ should_ 开头
- 转换函数用 as_xxx to_xxx into_xxx 区分借用/复制/消耗语义
- 枚举变体不重复枚举名前缀 用 Color::Red 而非 Color::ColorRed

## 格式

- rustfmt 强制执行 不得使用 #[rustfmt::skip] 除非极端必要
- rustfmt.toml 设置 max_width = 100
- use 分三组 std 标准库 / 第三方 crate / crate 内部 每组空行分隔
- use 同一路径前缀合并为花括号形式 use std::{ collections::HashMap sync::Arc }
- 不使用 use xxx::* 除 prelude 和测试模块
- 链式调用每个方法独占一行 对齐 .
- 结构体字段每行一个 末尾加逗号
- match 分支体超过一行时加花括号

## 所有权与借用

- 函数参数优先借用 &T 或 &mut T 而非取得所有权
- 返回新值时优先 move 语义 避免不必要引用返回
- 字符串参数类型用 &str 返回类型用 String 或 &str 视生命周期决定
- Cow<'a str> 用于可能需要拥有也可能借用的字符串场景
- Arc 用于多线程共享 Rc 仅用于单线程
- 避免 .clone() 先考虑借用或重构数据流
- 大结构体传参用引用 小 Copy 类型直接传值
- 不用 mem::forget 除非有充分理由

## 错误处理

- 库 crate 用 thiserror 定义具体错误类型
- 应用层用 anyhow::Result 和 Context trait 添加上下文
- 始终用 ? 传播错误 不手动 match Err
- unwrap 和 expect 仅在逻辑上不可能失败时使用 expect 必须写清原因
- 避免 panic! 在库代码中 改为返回 Result
- Option 表达值可能缺失 Result 表达操作可能失败
- 自定义错误实现 std::error::Error + Display + Debug
- 错误信息小写开头 不加句号

## 类型系统

- 新类型模式封装原始类型 struct UserId(u64) 防止参数顺序混淆
- 枚举建模有限状态 避免 bool 标志位组合
- PhantomData<T> 标记类型状态 零成本编译期约束
- 泛型约束超过一个时用 where 子句
- 关联类型优于多余的泛型参数
- 避免过度泛化 先具体类型 确有复用需求再抽象
- derive 宏优先 Clone Copy Debug PartialEq Eq Hash 按需添加
- 用 #[non_exhaustive] 标记对外公开的枚举和结构体

## 并发

- 明确理解 Send 和 Sync 的含义再引入多线程
- 异步运行时默认选 tokio
- async fn 中 Mutex 锁作用域必须在 .await 之前释放
- 避免 async trait 的生命周期问题 用 #[async_trait] 或 RPITIT
- 共享状态优先用消息传递 channel 其次 Arc<Mutex<T>>
- tokio::spawn 的任务必须是 'static + Send
- 不在异步上下文中调用阻塞 IO 用 tokio::task::spawn_blocking 包装
- 并发集合考虑 dashmap 替代 Mutex<HashMap>

## 模块组织

- lib.rs 只做 pub mod 声明和顶层 re-export 无业务逻辑
- 单文件单模块 超过 300 行考虑拆分 超过 500 行必须拆分
- 大模块用目录 mod.rs 或同名文件作为入口
- pub(crate) 优先于 pub 最小化对外暴露
- prelude.rs 收集本 crate 最常用的 re-export 供用户 use crate::prelude::*
- 循环依赖禁止 调整模块层级消除
- 内部实现细节放 impl 块或 private 函数 不提升为模块级

## 测试

- 单元测试写在同文件底部 #[cfg(test)] mod tests { ... }
- 集成测试放 tests/ 目录 每个功能域一个文件
- 属性测试用 proptest 或 quickcheck 覆盖边界条件
- assert_eq!(actual expected) 参数顺序 实际值在前 期望值在后
- 测试函数名描述被测行为 test_parse_returns_err_on_empty_input
- 用 rstest 做参数化测试 替代重复测试函数
- mock 用 mockall 不手写 trait 假实现
- 测试中可以用 unwrap 无需注释原因

## 性能

- 优先 iterator 适配器链 避免中间 Vec 分配
- 栈上能解决的不用 Box 小对象不上堆
- String 拼接用 format! 或 push_str 避免 + 连续操作
- #[inline] 仅在跨 crate 的热路径使用 不滥用
- 用 cargo bench 和 criterion 验证优化前后数据
- 避免在热路径中做 HashMap 频繁 insert/remove 考虑预分配 with_capacity
- 序列化热路径考虑 simd-json 或 rkyv 替代 serde_json
- 大量小对象考虑 arena 分配器 typed-arena bumpalo

## 依赖管理

- Cargo.toml 中 features 精确指定 不用 full
- dev-dependencies 和 build-dependencies 严格分组
- 版本约束用 ^ 语义化版本 不锁死 patch 版本
- 定期运行 cargo audit 检查安全漏洞
- 优先选择维护活跃 无 unsafe 的 crate
- 能用标准库解决的不引入外部依赖

## unsafe

- unsafe 块必须有 SAFETY 注释说明不变量
- unsafe 代码隔离在专门模块或函数中 不散布
- 封装 unsafe 为安全抽象 对外只暴露 safe API
- 每处 unsafe 都要明确说明满足了哪些 Rust 安全约束
- 优先寻找 safe 替代方案 实在无法绕开才用 unsafe
