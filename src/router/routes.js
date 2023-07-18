import posts from '@/views/posts.vue'
import error from '@/views/error.vue'
import index from '@/views/index.vue'

// student
import student from '@/views/student'
import studentSignup from '@/views/studentSignup'
import studentTests from "@/views/studentTests";
import studentChat from "@/views/studentChat";
import studentProfile from "@/views/studentProfile";
import studentChangeProfile from "@/views/studentChangeProfile";
import studentInters from "@/views/studentInters";


export default [
    {
        path: '/student',
        redirect: '/student/signup',
        component: student,
    },
    {
        path: '/student/signup',
        component: studentSignup
    },
    {
        path: '/student/profile',
        redirect: false,
        component: studentProfile,
    },
    {
        path: '/student/profile/edit',
        component:  studentChangeProfile,
    },
    {
        path: '/student/chat',
        component: studentChat,
    },
    {
        path: '/student/inters',
        component: studentInters,
    },
    {
        path: '/student/tests',
        component: studentTests,
    },
    {
        path: '/posts',
        name: 'posts',
        component: posts
    },
    {
        path: '/',
        name: 'index',
        component: index,
        redirect: '/student/signup',
    },
    {
        path: '/:pathMatch(.*)*',
        name: 'error',
        component: error
    }
]
