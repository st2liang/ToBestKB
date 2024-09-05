<template>
  <div class="top-bar">
    <h1 class="text">至善助手</h1>
    <profilePhoto/>
  </div>
</template>

<script lang="ts" setup>
  import profilePhoto from './profile photo.vue'; // 确保路径正确
</script>

<style scoped>
.top-bar {
  position: fixed;
  top: 10px;
  left: 20%; /* 与左侧导航栏对齐 */
  width: 80%; /* 剩余宽度填充 */
  padding: 10px 20px;
  box-sizing: border-box;
  
  z-index: 1000;
  display: flex;
  justify-content: space-between; /* 左右元素分散对齐 */
  align-items: center; /* 垂直居中对齐 */
  height: 40px;
}

.text {
  margin: 0;
  line-height: 1;
}

.profilePhoto {
  display: flex;
  align-items: center;
  margin-right: 100px;
}
</style>