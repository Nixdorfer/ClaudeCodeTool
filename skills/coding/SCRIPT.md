# Script书写规范

- 函数名使用驼峰名 例如getAppAuthCode
- 变量名使用蛇形命名 例如app_auth_code
- 函数内不要有空行 尽可能保持代码简洁
- 两个块之间有一个空行
- 脚本优先使用powershell
- 使用尽可能紧凑的格式 如果语法允许 遵循以下规则
  - 如果if/for/do的执行体只有一行 则省略{}直接空一格格 在同一行写出
  - 如果一个try/catch/function只有一行执行体 则直接在同一行写出
  - 在不影响可读性的情况下尽可能减少行数
  - 链式调用需要换行 多个链式调用前有一个缩进
  - 例子
    ```TypeScript
    if (contentType.includes('application/json')) responseBody = await response.json();
    for (const item of all) if (item.key.startsWith(prefix)) await SecureStorage.indexedDB.userRemove(item.key);
    if (serviceWorkerRegistration?.active) serviceWorkerRegistration.active.postMessage({
        type: 'UPDATE_WHITELIST',
        data: { whitelist: whitelistConfig }
    });
    try{doSth();}
    catch{doSth();}
    const res = fetch('xxx')
     .then(xxx)
     .then(xxx);
    ```

# 文件中的块顺序

1. 文件头
   - 对于Go是package
   - 对于PHP是<?php
2. import块
3. type/struct等大结构块
4. var/const等变量块
5. function块

# Go语言风格

- 使用any而不是interface{}