<template> 
    <el-button plain @click="dialogFormVisible = true" class="new">
      +新对话
    </el-button>
  
    <el-dialog v-model="dialogFormVisible" title="新建一个对话" width="500">
      <el-form :model="form">
        <el-form-item label="对话名称" :label-width="formLabelWidth">
          <el-input v-model="form.name" autocomplete="off" />
        </el-form-item>
        <el-form-item label="知识库" :label-width="formLabelWidth">
          <el-select v-model="form.region" placeholder="请选择要绑定的知识库">
            <el-option label="Zone No.1" value="shanghai" />
            <el-option label="Zone No.2" value="beijing" />
          </el-select>
        </el-form-item>
      </el-form>
      <template #footer>
        <div class="dialog-footer">
          <el-button @click="dialogFormVisible = false">取消</el-button>
          <el-button type="primary" @click="dialogFormVisible = false">
            确认
          </el-button>
        </div>
      </template>
    </el-dialog>
  </template>
  
  <script lang="ts" setup>
  import { reactive, ref } from 'vue'
  
  const dialogFormVisible = ref(false)
  const formLabelWidth = '140px'
  
  const form = reactive({
    name: '',
    region: '',
    date1: '',
    date2: '',
    delivery: false,
    type: [],
    resource: '',
    desc: '',
  })
  
  </script>
  
  <style scoped>
  .new {
    width: 100%;
    color:white;
    background-color: #2666FE;
  }

  </style>