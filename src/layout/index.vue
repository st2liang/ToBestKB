<template>
  <div class="container">
    <div class="left_container">
      <img class="logo" src="/src/assets/logo/logo.png" />
      <div class="chat">
        <create_chat/>
        <el-scrollbar class="scrollbar">
          <!-- 菜单 -->
          <el-menu background-color="white" text-color="black" router>
            <el-menu-item
              v-for="(item, index) in menuItems"
              :key="index"
              :index="item.index"
            >
              {{ item.label }}
            </el-menu-item>
          </el-menu>
        </el-scrollbar>
      </div>
      <div class="db">
        <create_db/>
        <el-scrollbar class="scrollbar">
          <!-- 菜单 -->
          <el-menu background-color="white" text-color="black" router>
            <el-menu-item index="/dashboard/arrangement">日程安排</el-menu-item>
            <el-menu-item index="/dashboard/analyze">分析影像</el-menu-item>
            <el-menu-item index="/dashboard/manage">任务列表</el-menu-item>
            <el-menu-item index="/dashboard/task">病历管理</el-menu-item>
          </el-menu>
        </el-scrollbar>
      </div>
    </div>

    <div class="right_container">
      <div class="topbar">
        <topbar />
      </div>
      <div class="main">
        <!-- 路由出口 -->
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import topbar from '@/components/head/head.vue';
import create_chat from '@/components/dashboard/create_chat.vue';
import create_db from '@/components/dashboard/create_db.vue';
import { reactive } from 'vue';
// 路由
import { useRouter } from 'vue-router';
const router = useRouter();

  let menuItems = [
  { index: '/dashboard/arrangement', label: '日程安排' },
  { index: '/dashboard/analyze', label: '分析影像' },
  { index: '/dashboard/manage', label: '任务列表' },
  { index: '/dashboard/task', label: '病历管理' },
  { index: '/dashboard/arrangement', label: '日程安排' },
  { index: '/dashboard/analyze', label: '分析影像' },
  { index: '/dashboard/manage', label: '任务列表' },
  { index: '/dashboard/task', label: '病历管理' }
];

</script>

<style scoped>
/* Container styles */
.container {
  display: flex;
  width: 100%;
  height: 100vh;
  background: rgb(251, 251, 251);
}

/* Left Container */
.left_container {
  position: fixed;
  display: flex;
  flex-direction: column; /* 垂直排列 */
  align-items: center;
  box-sizing: border-box;
  padding: 20px 10px;
  width: 15%;
  height: 100vh;
  background-color: #ffffff;
  z-index: 1;
  left: 20px;
  top: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.logo {
  width: 100%;
  padding-bottom: 40px;
  height: 7%; /* 设置 logo 的高度 */
}

.chat {
  width: 100%;
  margin-bottom: 20px; /* 控制 chat 与 db 的间距 */
  height: 40%;
}

.db {
  width: 100%;
}

/* Scrollbar Styles for chat and db */
.chat .scrollbar {
  width: 100%;
  height: 90%; /* 确保滚动条的高度 */
}

.db .scrollbar {
  width: 100%;
  height: 50%;
}


/* Right Container */
.right_container {
  margin-left: 260px; /* 留出 left_container 的宽度 */
  width: calc(100% - 260px);
  display: flex;
  flex-direction: column;
  height: 100vh;
}

/* Topbar */
.topbar {
  width: 100%; /* 确保 topbar 和 right_container 宽度一致 */
  height: 60px; /* 设置 topbar 的高度与 logo 一致 */
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  display: flex;
  justify-content: space-between;
  align-items: center;
}

/* Main Content */
.main {
  flex-grow: 1;
  padding: 20px;
  background: rgb(250, 250, 250);
  overflow: auto;
}
</style>