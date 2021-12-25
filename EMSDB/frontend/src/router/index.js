import {createRouter, createWebHistory} from 'vue-router'
import Login from '../views/Login.vue';
import Student_Home from "../views/Student_Home";
import Teacher_Home from "../views/Teacher_Home"
import Admin_Home from "../views/Admin_Home";

const routes = [
    {
        path: '/',
        name: 'login',
        component: Login
    },

    {
        path: '/studentHome',
        name: 'studentHome',
        component: Student_Home
    },
    {
        path: '/teacherHome',
        name: 'teacherHome',
        component: Teacher_Home
    },
    {
        path: '/adminHome',
        name: 'adminHome',
        component: Admin_Home
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router
