import  request from "@/utils/request";
import type { LoginParams,LogResponse } from "./type";
//统一管理
enum API{
    LOGIN_URL = '/doctors/login/',
    LOGOUT_URL = '/doctors/logout/',
    REGIST_URL = '/doctors/register/',
    GET_DOCTOR_LIST_URL = '/doctors/',
    GET_DOCTOR_INFO_URL ='/doctors/{id}/profile/',
    CHANGE_DOCTOR_INFO_URL ='/doctors/{id}/',
}

//暴露请求函数
//登录接口方法
export const reqlogin = (data:LoginParams) => {
    return request.post<any,LogResponse>(API.LOGIN_URL,data)
}
//登出接口方法
export const reqlogout = (data:LogResponse) => {
    return request.post(API.LOGOUT_URL,data)
}
//注册接口方法
export const reqregist = (data:any) => {
    return request.post(API.REGIST_URL,data)
}
//获取医生列表接口方法
export const reqgetDoctorList = () => {
    return request.get(API.GET_DOCTOR_LIST_URL)
}
//获取医生信息接口方法
export const reqgetDoctorInfo = (id:string) => {
    return request.get(API.GET_DOCTOR_INFO_URL.replace('{id}',id))
}
//修改医生信息接口方法
export const reqchangeDoctorInfo = (id:string,data:any) => {
    return request.put(API.CHANGE_DOCTOR_INFO_URL.replace('{id}',id),data)
}