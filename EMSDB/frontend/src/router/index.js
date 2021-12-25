import {createRouter, createWebHistory} from 'vue-router'
import Home from '../views/Home.vue';
import Student from "../views/Student";
import Teacher from "../views/Teacher";
import Admin from "../views/Admin";

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
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router
