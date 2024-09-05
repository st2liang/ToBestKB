import { defineStore } from "pinia";
//引入接口
import { reqlogin } from "@/api/user";
//引入数据类型
import type { LoginParams } from "@/api/user/type";
const useUserStore = defineStore("user", {
    //小仓库
    state: () => {
        return {
            token:localStorage.getItem("TOKEN"),
        }
    },
    //逻辑
    actions: {
        //用户登录方法
        async userlogin(data:LoginParams) {
            const res = await reqlogin(data);
            //登陆成功：200->token
            if(res.code===200){
                //token存储到小仓库
                this.token=res.data.token;
                //持久化存储
                localStorage.setItem('TOKEN',res.data.token);
                return '登录成功';
            }
            //登录失败：
            else{
                return Promise.reject(new Error(res.data.message));
            }
        }
    },
    getters: {
        
    }
})
export default useUserStore;