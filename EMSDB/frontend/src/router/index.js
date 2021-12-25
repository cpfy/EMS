import {createRouter, createWebHistory} from 'vue-router'
import Home from '../views/Home.vue';
import Student from "../components/Student_Nav";
import Teacher from "../components/Teacher_Nav";
import Admin from "../components/Admin_Nav";
import Student_Home from "../views/Student_Home";
import Teacher_Home from "../views/Teacher_Home"
import Admin_Home from "../views/Admin_Home";

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/student',
        name: 'Student',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: Student
    },
    {
        path: '/teacher',
        name: 'Teacher',
        component: Teacher
    },
    {
        path: '/admin',
        name: 'Admin',
        component: Admin
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
