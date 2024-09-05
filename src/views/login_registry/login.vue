<template>
  <div class="container">
    <div class="login_container">
      <div class="login_section">
        <img class="logo" src="/src/assets/logo/logo.png">
        <div class="login">
          <div class="title">
            <h1>登录</h1>
            <h4>还没有账号？</h4>
            <router-link to="/registry" class="registry">立即注册</router-link>
          </div>
          <div class="form">
              <el-input type="text" 
                placeholder="请输入用户名" id="username" v-model="username" prefix-icon="UserFilled"></el-input>
              <el-input type="password" placeholder="请输入密码" id="password" v-model="password" prefix-icon="Lock" show-password></el-input>
              <el-button type="primary" class="loginbtn" @click="handleSubmit">登录</el-button>
          </div>
        </div>
      </div>
      <img class="show" src="/src/assets/login_registry/show.png">
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

import { UserFilled, Lock } from '@element-plus/icons-vue';
import axios from 'axios';

export default {
  setup() {
    const username = ref("");
    const password = ref("");
    const router = useRouter();

    const handleSubmit = async () => {
      console.log("In handleSubmit!")
      try {
        const response = await axios.post("https://api.chattree.cc/mock/41/login", {
          username: username.value,
          password: password.value,
        });
        if (response.data.code==200) {
          alert("登录成功！");
          router.push('/dashboard/person');
        } else {
          alert("登录失败，请检查用户名和密码。");
        }
        console.log(response);
      } catch (error) {
        console.error(error);
      }
    };

    return {
      username,
      password,
      handleSubmit,
    };
  },
}
</script>

<style scoped>
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  padding: 20px;
}

.login_container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
}

.login_section {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 50%; /* 占用50%的宽度 */
}

.logo {
  width: 150px; /* 根据需要
  调整logo大小 */
  margin-bottom: 200px;
  margin-right:200px;
}

.login {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 300px;
}

.show {
  width: 50%; /* 占用50%的宽度 */
  height: auto;
}

.title {
  text-align: left;
  margin-bottom: 20px;
  width: 100%;
}

.form {
  width: 100%;
}

.el-input,
.el-button {
  width: 100%;
  margin-bottom: 20px;
}
</style>