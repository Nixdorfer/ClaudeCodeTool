# Vue书写规范

## 基本要求

- 使用Vue3 Composition API
- 使用Vite作为构建工具
- 使用Pinia作为状态管理
- 单个.vue文件不要太长 长文件分散为多个组件

## 组件结构

```vue
<script setup lang="ts">
// imports
// props/emits
// reactive state
// computed
// methods
// lifecycle hooks
</script>

<template>
</template>

<style scoped>
</style>
```

## 命名规范

- 组件文件名使用PascalCase 例如UserProfile.vue
- 组件在template中使用kebab-case 例如<user-profile>
- props使用camelCase 例如userName
- emits使用kebab-case 例如@update-user

## Props定义

```ts
defineProps<{
  userName: string
  userId: number
  isActive?: boolean
}>()
```

## Emits定义

```ts
const emit = defineEmits<{
  'update-user': [id: number, name: string]
  'delete': [id: number]
}>()
```