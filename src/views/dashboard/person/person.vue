<template>
  <div class="doctor-profile">
    <el-card class="doctor-card" shadow="hover">
      <!-- 医生个人信息内容 -->
      <div class="doctor-header">
        <img 
        src="/src/assets/doctor/photo.jpg" class="doctor-avatar" alt="Doctor Avatar" 
        />
        <h2>{{ doctor.name }}</h2>
        <p>{{ doctor.department }}</p>
      </div>
      <div v-if="editing">
        <div class="doctor-info">
          <h3>个人信息</h3>
          <p><strong>性别：</strong><el-input v-model="editedDoctor.gender" /></p>
          <p><strong>年龄：</strong><el-input v-model.number="editedDoctor.age" /></p>
        </div>
        <div class="doctor-contact">
          <h3>联系方式</h3>
          <p><strong>电话：</strong><el-input v-model="editedDoctor.phone" /></p>
          <p><strong>Email:</strong><el-input v-model="editedDoctor.email" /></p>
        </div>
        <div class="doctor-bio">
          <h3>医生简介</h3>
          <p><el-input type="textarea" v-model="editedDoctor.bio" /></p>
        </div>
        <el-button @click="saveInfo">保存</el-button>
      </div>
      
      <div v-else>
        <div class="doctor-info">
          <h3>个人信息</h3>
          <p><strong>性别：</strong>{{ doctor.gender }}</p>
          <p><strong>年龄：</strong>{{ doctor.age }}</p>
        </div>
        <div class="doctor-contact">
          <h3>联系方式</h3>
          <p><strong>电话：</strong>{{ doctor.phone }}</p>
          <p><strong>Email:</strong>{{ doctor.email }}</p>
        </div>
        <div class="doctor-bio">
          <h3>医生简介</h3>
          <p>{{ doctor.bio }}</p>
        </div>
        <el-button @click="editInfo">修改信息</el-button>
      </div>
      
    </el-card>
  </div>
</template>

<script>
export default {
  data() {
    return {
      doctor: {
        name: '医生姓名',
        department: '心脏科',
        avatar: '医生头像地址',
        gender: '男',
        age: 40,
        phone: '123-456-7890',
        email: 'doctor@example.com',
        bio: '医生的简介内容，包括教育背景、专业经验等。'
      },
      editing: false,
      editedDoctor: {}
    };
  },
  methods: {
    editInfo() {
      this.editing = true;
      this.editedDoctor = { ...this.doctor }; // 创建一个副本以在编辑时使用
    },
    saveInfo() {
      this.doctor = { ...this.editedDoctor }; // 更新医生信息为编辑后的信息
      this.editing = false; // 退出编辑状态
    }
  }
};
</script>

<style>
.doctor-profile {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.doctor-card {
  width: 400px;
  padding: 20px;
  text-align: center;
}

.doctor-avatar {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  margin-bottom: 10px;
}

.doctor-header {
  margin-bottom: 20px;
  text-align: center;
}

.doctor-info, .doctor-contact, .doctor-bio {
  margin-bottom: 15px;
}
</style>
