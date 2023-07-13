import { createRouter, createWebHashHistory } from 'vue-router';
import inthead from "./components/inthead.vue";
import intup from "./components/intup.vue";
import info from "./components/info.vue"
export default createRouter( {
    history: createWebHashHistory(),
    routes: [
        { path: '/one', component: inthead},
        { path: '/two', component: intup},
        { path: '/info', component: info}
    ]
})