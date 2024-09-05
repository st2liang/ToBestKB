import axios from 'axios';

let axiosInstance = axios.create({
  baseURL: '/', // 替换根api
  timeout: 5000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// 添加请求拦截器
axiosInstance.interceptors.request.use(config => {
  // 在发送请求之前做些什么
  return config;
}, error => {
  // 对请求错误做些什么
  return Promise.reject(error);
});

// 添加响应拦截器
axiosInstance.interceptors.response.use(response => {
  // 对响应数据做点什么
  return response;
}, error => {
  // 对响应错误做点什么
  // 添加响应拦截器
axiosInstance.interceptors.response.use(response => {
  // 对响应数据做点什么
  return response;
}, error => {
  // 对响应错误做点什么
  if (error.response.status === 400) {
    console.log(JSON.stringify(error.response.data));
  } else if (error.response.status === 401) {
    console.log(JSON.stringify(error.response.data));
  } else {
    console.log('Error: ' + JSON.stringify(error.response.data));
  }
  return Promise.reject(error);
});
  return Promise.reject(error);
});

export default axiosInstance;