---
name: fetch-spa
description: 抓取SPA页面的HTML内容，用于获取支付宝文档等使用JavaScript动态加载的网页。当需要获取opendocs.alipay.com或其他SPA页面内容时使用此技能。
allowed-tools: Bash(python:*)
---

# 抓取SPA页面内容

用于获取SPA(单页应用)页面的渲染后HTML，支持等待JavaScript加载完成。

## 使用方法

```bash
python "C:\Users\Nix\.claude\skills\fetch-spa\scripts\fetch_spa.py" "<URL>" [--wait <毫秒>] [--no-scroll]
```

## 参数

- `URL` (必需): 要抓取的网页地址
- `--wait <毫秒>`: 等待时间，默认5000ms
- `--no-scroll`: 不滚动页面

## 示例

```bash
python "C:\Users\Nix\.claude\skills\fetch-spa\scripts\fetch_spa.py" "https://opendocs.alipay.com/mini/api/xxx"
```

## 输出

脚本会输出清理后的HTML内容（已移除script/style/svg/img等标签）。

## 依赖

需要安装playwright:
```bash
pip install playwright
playwright install chromium
```

# 关于支付宝接口文档

支付宝接口文档使用了SPA技术 因此普通的WebFetch无法正常获得其内容 并且内容中包含了大量冗余的文本 会占用大量的context窗口 因此我写了一个简单的[脚本](scripts/fetch_spa.py)来协助你获取纯文本信息

## 接口分类

所有的支付宝接口主要分为三类
- 发送信息
  这代表使用POST/GET等方法主动向支付宝服务器发送消息 并期待获得一些回复 这是最常见的文档种类
- 接收消息(回调/订阅)
  这代表支付宝服务器将会向己方服务器发送一些消息 这些消息是我在支付宝控制台订阅的 因此这随时可能会发生 但是因为我在支付宝控制台指定了接口 因此必定只会有这个接口会收到来自支付宝的消息
  可以通过期内携带的method字段判断这是哪种消息
- 上传文件
  本质上也是一种发送消息的方式 但是支付宝有base64编码并附加到指定字段 以及直接附加二进制内容两种上传文件的方式 这种接口最少见

## 页面结构

支付宝接口需要查看以下几项 来确定后端如何请求和接收回复 以下几个词可以作为标志词 对HTML文档进行搜索 以便快速定位
- 公共请求参数
- 业务请求参数 这部分一般作为公共请求参数的biz_content的子项 请识别列表 并递归创建所有键
- 常见请求示例(cURL/Java/C#/PHP) 可以查看发送的具体内容
- 公共响应参数
- 业务响应参数 一般被包装在一个形如alipay_open_mini_icp_apply_response的键内 code=10000为成功 否则为失败
- 响应示例(正常示例/异常示例) 可以查看具体的响应代码