<template>
  <el-table :data="tableData" style="width: 100%">
    <el-table-column fixed prop="id" label="ID" width="100" />
    <el-table-column prop="name" label="姓名" width="120" />
    <el-table-column prop="sex" label="性别" width="120" />
    <el-table-column prop="age" label="年龄" width="120" />
    <el-table-column prop="phone" label="手机号" width="120" />
    <el-table-column prop="description" label="描述" width="600" />
    <el-table-column fixed="right" label="Operations" width="120">
      <template #default="{ row }">
        <el-button link type="primary" size="small" @click="openDialog(row)"
          >编辑</el-button
        >
      </template>
    </el-table-column>
  </el-table>

  <el-dialog v-model="dialogFormVisible" title="编辑病人信息" width="500">
    <el-form ref="form" :model="formData" label-width="80px" class="demo-form">
      <el-form-item label="ID">
        <el-input v-model="formData.id" disabled></el-input>
      </el-form-item>
      <el-form-item label="姓名" prop="name">
        <el-input v-model="formData.name"></el-input>
      </el-form-item>
      <el-form-item label="性别" prop="sex">
        <el-select v-model="formData.sex" placeholder="请选择">
          <el-option label="男" value="male"></el-option>
          <el-option label="女" value="female"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="年龄" prop="age">
        <el-input v-model="formData.age"></el-input>
      </el-form-item>
      <el-form-item label="手机号" prop="phone">
        <el-input v-model="formData.phone"></el-input>
      </el-form-item>
      <el-form-item label="描述" prop="description">
        <el-input v-model="formData.description" type="textarea"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm">提交</el-button>
        <el-button @click="resetForm">重置</el-button>
      </el-form-item>
    </el-form>
  </el-dialog>
</template>

<script setup lang="ts">
import { ref, reactive, onMounted } from "vue";
import axios from "axios";

const dialogFormVisible = ref(false);

const baseURL = "http://localhost:8000"; // 假设后端服务器在本地的 8000 端口上

const axiosInstance = axios.create({
  baseURL: baseURL,
});

onMounted(() => {
  fetchPatients();
});

// 定义表格数据和表单数据

const formData = reactive({
  id: "",
  name: "",
  sex: "",
  age: "",
  phone: "",
  description: "",
});

interface TableRow {
  id: string;
  name: string;
  sex: string;
  age: string;
  phone: string;
  description: string;
}

const tableData: TableRow[] = reactive([]);

const openDialog = (row: TableRow) => {
  formData.id = row.id;
  formData.name = row.name;
  formData.sex = row.sex;
  formData.age = row.age;
  formData.phone = row.phone;
  formData.description = row.description;
  dialogFormVisible.value = true;
};

const resetForm = () => {
  // Reset form logic
  formData.id = "";
  formData.name = "";
  formData.sex = "";
  formData.age = "";
  formData.phone = "";
  formData.description = "";
};

// 提交表单并更新病人信息
const submitForm = () => {
  // 获取token
  const token = localStorage.getItem("token");

  // 设置请求头，将token添加到Authorization头部
  const config = {
    headers: {
      Authorization: `Token ${token}`,
    },
  };

  // 发送请求保存表单数据，使用config配置
  axiosInstance
    .put(`/patients/${formData.id}/`, formData, config)
    .then((response) => {
      console.log("Form submitted:", response.data);
      dialogFormVisible.value = false;
      // 更新表格数据等操作
      fetchPatients();
    })
    .catch((error) => {
      console.error("Error submitting form:", error);
      // 处理错误情况
    });
};

// 获取病人列表数据
const fetchPatients = () => {
  // 获取token
  const token = localStorage.getItem("token");
  console.log(token);

  // 设置请求头，将token添加到Authorization头部
  const config = {
    headers: {
      Authorization: `Token ${token}`,
    },
  };

  // 发送请求获取病人列表数据，使用config配置
  axiosInstance
    .get("/patients/", config)
    .then((response) => {
      console.log("test");
      console.log("--------------------------------------------");
      console.log(response);
      console.log("--------------------------------------------");
      console.log(response.data.results[0]);
      console.log("--------------------------------------------");
      tableData.push(response.data.results[0]);
      console.log(tableData.values);
      // 清空tableData数组
      tableData.splice(0);

      // 将新数据添加到tableData数组中
      for (let patient of response.data.results) {
        tableData.push(patient);
      }
    })
    .catch((error) => {
      console.error("Error fetching patients:", error);
      // 处理错误情况
    });
};

// const tableData: TableRow[] = reactive([
//   {
//     ID: "1001",
//     name: "张三",
//     sex: "男",
//     age: 55,
//     phone: "13812345678",
//     description: "患者心脏病史，曾有一次心肌梗死，需注意冠脉堵塞情况。",
//   },
//   {
//     ID: "1002",
//     name: "李四",
//     sex: "女",
//     age: 60,
//     phone: "13987654321",
//     description: "患者冠脉支架植入史，心脏功能良好，无异常体征。",
//   },
//   {
//     ID: "1003",
//     name: "王五",
//     sex: "男",
//     age: 50,
//     phone: "13655557777",
//     description: "患者近期出现心绞痛症状，需要进一步检查冠脉情况。",
//   },
//   {
//     ID: "1004",
//     name: "赵六",
//     sex: "男",
//     age: 65,
//     phone: "13544448888",
//     description: "患者有高血压和冠心病病史，需定期监测心脏功能。",
//   },
//   {
//     ID: "1005",
//     name: "小七",
//     sex: "女",
//     age: 45,
//     phone: "13799998888",
//     description: "患者冠脉狭窄，需要安排冠脉扩张手术。",
//   },
//   {
//     ID: "1006",
//     name: "钱八",
//     sex: "男",
//     age: 58,
//     phone: "13333335555",
//     description: "患者心电图异常，需要进一步检查心脏功能。",
//   },
//   {
//     ID: "1007",
//     name: "孙九",
//     sex: "女",
//     age: 62,
//     phone: "13222226666",
//     description: "患者有糖尿病合并心血管疾病，需控制血糖并定期随访。",
//   },
//   {
//     ID: "1008",
//     name: "周十",
//     sex: "男",
//     age: 70,
//     phone: "13111117777",
//     description: "患者心脏衰竭，需长期服药控制病情。",
//   },
// ]);
</script>
