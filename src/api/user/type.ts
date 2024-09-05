//登录接口需要携带参数ts类型
export interface LoginParams {
    name: string,
    password: string
}

//登录/登出接口返回数据ts类型
export interface LogResponse {
    data: any
    token: string,
    code: number
}

//服务器返回用户信息相关数据类型
export interface UserInfo {
    
}