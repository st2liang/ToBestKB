<template>
  <div class="common-layout">
    <el-container>
      <el-header class="header">
        <div class="demo-date-picker">
          <div class="block header-content">
            <span class="demonstration">新增日程安排</span>
            <el-date-picker
              v-model="valueforPick"
              type="date"
              placeholder="选择日期"
              value-format="YYYY-MM-DD"
              :disabled-date="disabledDate"
              :shortcuts="shortcuts"
            />
            <el-input class="header-content" v-model="misson" style="width: 240px" placeholder="请输入相关事宜" />
            <el-button class="header-content" plain @click="setMisson">确定</el-button>
            
          </div>
        </div>
      </el-header>
      <el-main>
        <el-calendar>
          <template #date-cell="{ data, date }">
            <p :class="data.isSelected ? 'is-selected' : ''">
              {{ data.day.split("-").slice(2).join("-") }}
              <div
                v-for="(item, index) in missonList"
                :key="index"
              >
              <p class="missonInCalender" v-if="(item.date).indexOf(data.day)!=-1">{{ item.content }}</p>
              </div>
            </p>
          </template>
        </el-calendar>
      </el-main>
    </el-container>
  </div>
</template>

<script setup lang="ts">
import { reactive, ref } from "vue";
const value = ref(new Date());
const valueforPick = ref("");
const misson = ref("");
const shortcuts = [
  {
    text: "Today",
    value: new Date(),
  },
  {
    text: "Yesterday",
    value: () => {
      const date = new Date();
      date.setTime(date.getTime() - 3600 * 1000 * 24);
      return date;
    },
  },
  {
    text: "A week ago",
    value: () => {
      const date = new Date();
      date.setTime(date.getTime() - 3600 * 1000 * 24 * 7);
      return date;
    },
  },
];

const disabledDate = (time: Date) => {
  return time.getTime() > Date.now();
};

const missonList=reactive([
    {
        date:"2024-03-01",
        content:"test"
    }
]);
const setMisson = () => {
    const dateforPickValue = valueforPick.value.toString();
  const daymissionValue = misson.value;

  let found = false;

  for (let i = 0; i < missonList.length; i++) {
    if (missonList[i].date === dateforPickValue) {
      missonList[i].content = daymissionValue;
      found = true;
      break;
    }
  }

  if (!found) {
    missonList.push({
      date: dateforPickValue,
      content: daymissionValue
    });
  }

  console.log(missonList);

};
</script>

<style>
.demo-date-picker {
  display: flex;
  width: 100%;
  padding: 0;
  flex-wrap: wrap;
}

.demo-date-picker .block {
  padding: 30px 0;
  text-align: center;
  border-right: solid 1px var(--el-border-color);
  flex: 1;
}

.demo-date-picker .block:last-child {
  border-right: none;
}

.demo-date-picker .demonstration {
  color: var(--el-text-color-secondary);
  font-size: 14px;
  margin-bottom: 20px;
  margin-right: 20px;
}

.header {
  margin-bottom: 50px;
}

.header-content {
  margin: 10px;
}

.missonInCalender{
    box-shadow: 3px;
    background-color:skyblue;
    border-radius: 3px;

}
</style>
