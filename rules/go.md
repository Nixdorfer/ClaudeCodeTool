---
paths:
  - "**/*.go"
---

# Go 编码规范

## 命名

- 包名 小写单词 不用下划线 不用复数
- 导出符号用 PascalCase 未导出用 camelCase
- 接口名用 -er 后缀 如 Reader Writer Closer Stringer
- 缩写词全大写 如 HTTP URL ID RPC API
- 避免包名重复前缀 如 http.HTTPServer 应为 http.Server
- 变量名短小精悍 循环变量用 i j k 上下文变量用 ctx 错误用 err
- 接收者名取类型首字母小写 保持一致 不用 self this
- 常量用 PascalCase 不用全大写下划线风格

## 格式

- gofmt 强制执行 提交前必须格式化
- goimports 管理 import 自动增删
- 行宽 120 字符软限制 超出需有充分理由
- import 分三组 标准库 / 第三方 / 本地包 组间空行分隔
- 函数参数超过 3 个考虑封装为结构体
- 同类型多返回值考虑命名返回值增强可读性

## 错误处理

- 不忽略 error 必须处理或显式 _ 丢弃并注释原因
- 自定义错误用 fmt.Errorf + %w 包装保留调用链
- errors.Is / errors.As 做判断 不用 == 直接比较
- 错误信息小写开头 不带标点 可拼接组合
- panic 仅用于不可恢复场景 如程序启动配置缺失
- 库代码禁止 panic 由调用方决定如何处理
- 避免在循环中重复包装相同错误 只在边界处包装一次
- 哨兵错误用 var ErrXxx = errors.New(...) 定义在包级别

## 并发

- goroutine 必须有退出机制 context 取消或 done channel
- channel 优先于 mutex 但不滥用 共享状态用 mutex 更清晰
- sync.WaitGroup 管理 goroutine 生命周期
- 避免裸 go func() 封装为可控结构并命名
- context 作为函数第一个参数 命名为 ctx
- 不在结构体中存储 context 通过参数传递
- sync.Once 保证单次初始化 替代 init() 全局副作用
- 读多写少用 sync.RWMutex 替代 sync.Mutex

## 结构设计

- 小接口优于大接口 1-3 方法为佳
- 组合优于继承 嵌入结构体实现复用
- 依赖注入通过接口参数传入 不用全局变量
- init() 尽量避免 显式初始化函数优先
- 构造函数命名为 New 或 NewXxx 返回具体类型或接口
- 零值可用 结构体设计使零值有意义
- 选项模式 functional options 处理可选配置参数
- 避免返回指针到栈分配对象 让逃逸分析自然发生

## 测试

- 表驱动测试为默认模式 用 []struct 组织用例
- 测试文件 _test.go 与源文件同包 白盒测试
- 跨包集成测试放 xxx_test 包 黑盒测试
- mock 通过接口实现 不用反射魔法
- 基准测试 Benchmark 前缀 性能敏感路径必须有
- 测试辅助函数用 t.Helper() 标记
- 用 testify/assert 简化断言 不手写 if diff
- 避免测试依赖外部服务 用接口隔离并 mock

## 项目结构

- cmd/ 入口程序 internal/ 私有包 pkg/ 公共可复用包
- 按功能分包 不按类型分包 避免 util common helper 包名
- 一个包一个职责 包名即文档
- main 包只做组装 业务逻辑下沉到内部包
- 避免循环依赖 依赖方向单向流动
- 大型项目用 internal/ 防止包被外部误用

## 性能

- 预分配 slice 和 map 容量 make([]T n cap)
- 字符串拼接用 strings.Builder 不用 +=
- 避免在热路径中分配内存 复用对象用 sync.Pool
- 结构体字段按大小降序排列减少内存对齐浪费
- defer 有开销 极致性能路径考虑手动展开

## 其他

- 使用 any 替代 interface{} Go 1.18+
- 泛型用于消除重复的类型断言 不滥用
- 日志用结构化日志库 slog 或 zap 不用 fmt.Println
- 配置通过环境变量或配置文件注入 不硬编码
- 版本信息通过 ldflags 注入 不写死在代码中
