export const constantRoute=[
     // 路由配置
        {//首页
            path:'/',
            redirect:'/dashboard/person',
            name:'defalt'
        },

        {//登录界面
            path:'/login',
            component:()=>import('@/views/login_registry/login.vue'),
            name:'login',//命名路由
        }
        ,{//注册界面
            path:'/registry',
            component:()=>import('@/views/login_registry/registry.vue'),
            name:'registry',//命名路由
        }
        ,{//登陆成功后跳转
            path:'/dashboard',
            component:()=>import('@/layout/index.vue'),
            name:'dashboard',//命名路由
            children: [
                {
                    path:'',
                    redireact:'/dashboard/person'
                },
                {
                    path: 'person',
                    component: () => import('@/views/dashboard/person/person.vue'),
                    name: 'person',
                    default:true,
                },
                {
                    path: 'analyze',
                    component: () => import('@/views/dashboard/analyze/analyze.vue'),
                    name: 'analyze'
                },
                {
                    path: 'manage',
                    component: () => import('@/views/dashboard/manage/manage.vue'),
                    name: 'manage'
                },
                {
                    path: 'task',
                    component: () => import('@/views/dashboard/task/task.vue'),
                    name: 'task'
                },
                {
                    path: 'arrangement',
                    component: () => import('@/views/dashboard/arrangement/arrangement.vue'),
                    name: 'arrangement'
                }
            ]
        }
        ,{//404
            path:'/404',
            component:()=>import('@/views/404/404.vue'),
            name:'404',//命名路由
        }
        ,{
            path:'/:pathMatch(.*)*',
            redirect:'/404',
            name:'any',//命名路由
        }
        
]