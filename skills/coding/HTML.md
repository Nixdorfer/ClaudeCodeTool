# HTML书写规范

## 基本要求

- 使用语义化标签
- 属性值使用双引号
- 自闭合标签不加斜杠 例如`<input type="text">`
- 布尔属性不写值 例如`<input disabled>`

## 标签嵌套顺序

1. 结构标签 header/main/footer/section/article/nav/aside
2. 容器标签 div/span
3. 内容标签 h1-h6/p/ul/ol/li/table
4. 表单标签 form/input/select/textarea/button
5. 媒体标签 img/video/audio/canvas

## 属性顺序

1. id
2. class
3. name
4. data-*
5. src/href/for/type/value
6. placeholder/title/alt
7. aria-*/role
8. 布尔属性 disabled/checked/readonly

## 示例

```html
<section id="user-profile" class="profile-section" data-user-id="123">
  <h2>用户信息</h2>
  <form id="profile-form" class="form-container">
    <input id="username" class="form-input" name="username" type="text" placeholder="用户名" required>
    <button class="btn-submit" type="submit" disabled>提交</button>
  </form>
</section>
```
