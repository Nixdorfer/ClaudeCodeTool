---
name: go-backend
description: 一个用户基于GIN扩展出的的Go后端框架 当使用了这个架构时 你需要阅读这份文档来了解开发标准
---

# Go后端书写规范

## 基本概念

- 框架基于GIN
- 数据库基于GORM
- 使用Postgresql
- 使用Redis
- 使用RabbitMQ
- RESTful接口设计
- 配置文件采用yaml

# 具体特性

## codegen

该框架会在运行前启动codegen 生成所有格式化数据 这包括

- model
  codegen读取连接的数据库并在runtime/codegen下生成.sql格式的DDL 然后根据DDL在app/model下生成以gen_开头的数据库模型
  但如果数据库的某个字段是jsonb格式的 则需要在app/model/jsonb下新建一个.go文件 指定其结构 修改了jsonb的内容的同时 也需要修改数据库这个jsonb键值的模板

- router
  codegen从config/routes.yaml读取接口文档 并指导生成engine\init\router\gen_router.go接口路由表

- exception
  codegen从config/exceptions.yaml读取异常文档 并指导生成engine\request\request\gen_exception.go异常调用表

- log
  codegen从config/log.yaml读取日志文档 并指导生成engine\log\gen_log.go日志记录表

- task
  codegen从config/task.yaml读取日志文档 并指导生成engine\init\task\gen_task.go任务表

因为每次服务器启动前都会重新生成这些gen_开头的文件 因此不要修改gen_开头的model 这不会产生任何效果 而是会随着服务器重启而消失 所以请在必要情况下直接修改codegen

## Client类

Client中封装了支付宝请求 可以使用如下方式进行调用
```Go
rsp := client.NewClient(req, app).Method("alipay.security.risk.complaint.info.batchquery").Biz(map[string]any{
		"current_page_num": 1,
		"page_size":        5,
	}).Execute()
```

## Request类

Request类包装了如下内容
- gin.Context 该次请求的GIN上下文
- Sn 代表该次请求的序列号
- gorm.Db 数据库连接
- redis.Client Redis连接
- Option 自定义的所有可用选项
- ExceptionRegistry codegen生成的所有异常
- AccountModel 用户账户数据
- jsonBody
- WsBody

Request的所有部分在middleware中就会被注入完毕 当到达Handler时已经完全可用了 因此无论在何处都请传递这个Request的指针 便于以请求为单位 对这个请求本身进行处理 包括
- 使用诸如`req.Exc.Network.Empty()`的方式抛出异常 顶级的recover会处理这个异常并返回合适的错误数据
- 回传数据 `req.JSON(200, complaints)`