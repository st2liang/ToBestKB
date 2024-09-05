import { createRouter ,createWebHistory} from "vue-router";
import { constantRoute } from "./routes";

const router = createRouter({
    history: createWebHistory(),
    routes: constantRoute,
    //页面滚动到顶部
    scrollBehavior(){
        return {top:0,left:0,}
    }
});

export default router;