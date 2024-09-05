<template>
  <n-dropdown :options="options" @select="handleOptionSelect">
    <n-button>用户资料</n-button>
  </n-dropdown>
</template>

<script lang="ts">
import { h, defineComponent } from 'vue'
import type { Component } from 'vue'
import { useRouter } from 'vue-router'  // 引入 Vue Router
import { NIcon } from 'naive-ui'
import {
  PersonCircleOutline as UserIcon,
  Pencil as EditIcon,
  LogOutOutline as LogoutIcon
} from '@vicons/ionicons5'

const renderIcon = (icon: Component) => {
  return () => {
    return h(NIcon, null, {
      default: () => h(icon)
    })
  }
}

export default defineComponent({
  setup () {
    const router = useRouter()  // 使用 Vue Router
    const handleOptionSelect = (key: string) => {
      if (key === 'logout') {
        // 处理退出登录的逻辑
        // 例如清除用户信息、重定向到登录页面等
        router.push('/login')  // 跳转到登录页面
      }
      if(key==='editProfile'){
        router.push('/dashboard/person')
      }
    }

    return {
      options: [
        {
          label: '编辑用户资料',
          key: 'editProfile',
          icon: renderIcon(EditIcon)
        },
        {
          label: '退出登录',
          key: 'logout',
          icon: renderIcon(LogoutIcon)
        }
      ],
      handleOptionSelect
    }
  }
})
</script>

<style scoped>
.n-dropdown,
.n-button {
  background-color: white;
  color: black;
}
</style>
  