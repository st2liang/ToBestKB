<template>
  <div>
    <div class="knowledge-base">
      <div class="title">
      <span class="name">默认知识库 </span>
      <span class="changeKDBName" @click="editName">修改名称</span>
      </div>
      <!-- 文件列表 -->
      <div class="file-list">
        <div class="file-list-title">
          <span>文件列表</span>
        </div>
        <ul>
          <li v-for="(file, index) in files" :key="index">
            <span class="filename">{{ file.name }}</span>
            <div class="operations">
            <input type="checkbox" v-model="file.selected">
            <span @click="deleteFile(index)" class="dfb"><el-icon><Delete /></el-icon></span>
            </div>
          </li>
        </ul>


        <!-- 文件查询 -->
        <div class="file-search">
          <input type="text" v-model="searchQuery" placeholder="查询文件">
          <span @click="searchFiles"><el-icon><Search /></el-icon></span>
        </div>
      </div>


      <!-- 文件上传 -->
      <div class="file-upload">
        <label for="file-input" class="drop-area">
          拖拽文件至此 或点击上传文件
        </label>
        <input id="file-input" type="file" multiple @change="handleFileUpload" style="display:none;">
      </div>

      <!-- 操作按钮 -->
      <div class="action-buttons">
        <div class="upbuttons">
          <button @click="confirmUpload" class="confirm-btn">确认上传</button>
        </div>
        <div class="downbuttons">
        <button @click="saveAndReturn" class="save-btn">保存并返回</button>
        <button @click="deleteKnowledgeBase" class="delete-btn">删除知识库</button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.knowledge-base {
  font-family: Arial, sans-serif;
  background-color: #fff;
  width: 40%;
  padding-bottom: 50px;
  margin: 0 auto;
  padding-top: 50px;
  box-shadow: 20px 20px 10px rgba(50, 50, 50, 0.1); /* 添加阴影 */
}

.knowledge-base .title{
  width: 50%;
  margin: 0 auto 30px auto;
  text-align: center;

}

.knowledge-base .title .name{
  font-weight: bold;
  font-size: large;
  margin-right: 30px;
}

.knowledge-base .title .changeKDBName{
  color: #bbb;
}
.file-list {
  margin: 0 auto;
  margin-bottom: 20px;
  padding: 10px;
  border-radius: 8px;
  background-color: rgb(254, 247, 255);
  width: 50%;
}
.file-list .operations{
  display: inline;
  float: right;
}

.file-list .file-list-title{
  width: 4em;
  margin: 0 auto;
  color: rgba(72,66,82,0.77);
}

.file-list ul {
  list-style: none;
  padding: 0;
}

.file-list li {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}

.file-search {
  margin-bottom: 20px;
  display: flex;
  width: 80%;
  margin: 0 auto;
}

.file-search input {
  flex-grow: 1;
  padding: 5px;
  border-radius: 8px;
  border: 1px solid #ccc;
  margin-right: 10px;
}

.file-upload {
  margin-bottom: 20px;
  text-align: center;
}

.dfb{
  width: 40px;
  height: 40px;
  text-align: center;
  padding: 0;
  cursor: pointer;
}

.drop-area {
  display: inline-block;
  padding: 20px;
  border: 2px dashed #ccc;
  border-radius: 8px;
  background-color: rgb(254, 247, 255);
  cursor: pointer;
}

.action-buttons {
  /*display: flex;*/
  justify-content: space-around;
}



button {
  padding: 10px 20px;
  border-radius: 20px;
  border: none;
  cursor: pointer;
  color: white;
}

.upbuttons{
  position: relative;
  height: 40px;
  width: 100px;
  margin: 0 auto;
}

.confirm-btn {
  position: absolute;
  background-color: #d7b3fb;
  box-shadow: 0px 10px 10px rgba(215, 179, 251, 0.5); /* 添加阴影 */
}

.downbuttons{
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
  height: 40px;
  width: 80%;
  margin: 30px auto;
}


.save-btn {
  background-color: #87e1fc;
  margin-left: 0%;
  margin-right: 15%;
  box-shadow: 0px 10px 10px rgba(96, 183, 211, 0.5); /* 添加阴影 */
}

.delete-btn {
  background-color: rgb(247, 72, 72);
  margin-right: 5%;
  box-shadow: 0px 10px 10px rgba(212, 59, 59, 0.5); /* 添加阴影 */
}
</style>

<script>
export default {
  name: 'ImageAnalysis',
  data() {
    return {
      files: [
        {name: 'test1.txt', selected: true},
        {name: 'test2.txt', selected: true},
        {name: 'text3.md', selected: false},
        {name: 'test4.pdf', selected: false},
        {name: 'test5.txt', selected: true},
        {name: 'text6.txt', selected: true},
      ],
      searchQuery: '',
      uploadedFiles: []
    };
  },
  methods: {
    editName() {
      // 修改名称的逻辑
      alert('名称修改功能未实现');
    },
    deleteFile(index) {
      this.files.splice(index, 1);
    },
    searchFiles() {
      alert('搜索文件功能未实现');
    },
    handleFileUpload(event) {
      const selectedFiles = event.target.files;
      for (let i = 0; i < selectedFiles.length; i++) {
        this.uploadedFiles.push(selectedFiles[i]);
      }
    },
    confirmUpload() {
      if (this.uploadedFiles.length > 0) {
        alert('文件已上传');
        this.files.push(...this.uploadedFiles.map(file => ({name: file.name, selected: false})));
        this.uploadedFiles = [];
      } else {
        alert('没有选择文件');
      }
    },
    saveAndReturn() {
      alert('保存并返回');
    },
    deleteKnowledgeBase() {
      alert('知识库已删除');
    }
  }
};
</script>

