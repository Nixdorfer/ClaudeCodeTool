---
paths:
  - "**/*.vue"
---

# Vue 3 编码规范

## 组件

- Composition API + `<script setup>` 为默认写法
- 组件名 PascalCase 多词组合 避免单词组件名
- props 用 defineProps 带 TypeScript 类型声明
- emits 用 defineEmits 显式声明
- 单文件组件顺序 `<script>` `<template>` `<style>`

## 命名

- 组件文件名 PascalCase 如 UserProfile.vue
- 事件名 kebab-case 如 @update-value
- prop 名 camelCase 模板中使用 kebab-case
- 组合函数 use 前缀 如 useAuth useFetch
- 全局组件用前缀 如 App Base The

## 响应式

- ref 用于基本类型 reactive 用于对象
- computed 用于派生状态 不用 watch 做派生
- watch 用于副作用 watchEffect 用于自动追踪
- toRefs 解构 reactive 对象保持响应式
- shallowRef/shallowReactive 用于大对象性能优化

## 模板

- v-for 必须有 :key 且 key 唯一稳定
- v-if 和 v-for 不在同一元素上使用
- 复杂逻辑抽到 computed 不在模板中写
- 组件 prop 传递用 v-bind 简写 :
- 事件绑定用 @ 简写

## 组合函数

- 抽取可复用逻辑到 composables/ 目录
- 返回 ref 而非 reactive 方便解构
- 组合函数内部管理自己的生命周期
- 依赖注入用 provide/inject 不用 prop drilling

## 状态管理

- Pinia 为默认状态管理方案
- Store 按功能模块拆分
- getter 做派生状态 action 做异步操作
- 组件本地状态不放 store

## 性能

- v-once 标记静态内容
- v-memo 缓存大列表项
- defineAsyncComponent 延迟加载组件
- KeepAlive 缓存路由组件
