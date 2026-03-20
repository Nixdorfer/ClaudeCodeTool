---
paths:
  - "**/*.java"
---

# Java 编码规范

## 命名

- PascalCase 用于类 接口 枚举 注解
- camelCase 用于方法 变量 参数
- UPPER_SNAKE_CASE 用于常量
- 包名全小写 反向域名格式
- 接口不加 `I` 前缀 实现类加 `Impl` 或具体语义后缀
- 泛型参数用 `T` `E` `K` `V` 或语义化名称如 `TKey` `TValue`

## 格式

- 4 空格缩进
- 行宽 120 字符
- 花括号不换行 K&R 风格
- import 不用通配符 `*` 逐个导入
- 类成员顺序 静态字段 > 实例字段 > 构造器 > 方法

## 类设计

- 不可变优先 `final` 字段加无 setter
- 组合优于继承
- 接口定义行为 抽象类共享实现
- `record` 类做数据载体
- `sealed` 类约束继承层次
- `Optional` 表达可空返回值 不用于参数

## 错误处理

- 受检异常用于可恢复场景
- 运行时异常用于编程错误
- `try-with-resources` 管理资源
- 不捕获后忽略 至少记录日志
- 自定义异常带上下文信息

## 集合与流

- `List.of` `Map.of` 创建不可变集合
- Stream API 做数据转换和过滤
- 并行流仅在大数据量且无共享状态时使用
- `Collectors` 做终结操作

## 并发

- `CompletableFuture` 异步编程
- 虚拟线程 Virtual Thread 替代线程池
- `ConcurrentHashMap` 线程安全集合
- 避免 `synchronized` 方法 用细粒度锁
- `volatile` 保证可见性 不保证原子性

## 测试

- JUnit 5 为默认测试框架
- 测试方法名格式 `should_行为_when_条件`
- Mockito mock 外部依赖
- AssertJ 流式断言
- 单元测试不访问外部资源

## 构建

- Maven 或 Gradle 标准目录结构
- 依赖版本集中管理
- 多模块项目按功能划分
