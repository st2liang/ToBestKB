import  request from "@/utils/request";
//统一管理
enum API{
    GET_PATIENTS_LIST_URL = '/patients/',
    CREAT_PATIENT_URL ='/patients/',
    GET_PATIENT_INFO_URL ='/patients/{id}',
    CHANGE_PATIENT_INFO_URL ='/patients/{id}/',
}

//暴露请求函数
//获取患者列表接口方法
export const getPatientsList = () => {
    return request.get(API.GET_PATIENTS_LIST_URL)
}
//创建患者接口方法
export const createPatient = (data:any) => {
    return request.post(API.CREAT_PATIENT_URL,data)
}
//获取患者信息接口方法
export const getPatientInfo = (id:string) => {
    return request.get(API.GET_PATIENT_INFO_URL.replace('{id}',id))
}
//修改患者信息接口方法
export const changePatientInfo = (id:string,data:any) => {
    return request.put(API.CHANGE_PATIENT_INFO_URL.replace('{id}',id),data)
}