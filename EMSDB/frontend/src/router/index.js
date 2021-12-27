import {createRouter, createWebHistory} from 'vue-router'
import Login from '../views/Login.vue';
import Student_Home from "../views/Student_Home";
import Teacher_Home from "../views/Teacher_Home"
import Admin_Home from "../views/Admin_Home";
import PasswordChange from "../views/PasswordChange";
import test from "../views/test";
import PersonalInfo from "../views/PersonalInfo";
import ExemptionApply from "../views/Exemption_Apply";
import ExamDelay_Apply from "../views/ExamDelay_Apply";

const routes = [
    {
        path: '/',
        name: 'login',
        component: Login
    },
    {
      path: '/test',
      name: 'test',
      component: test
    },
    {
        path: '/student',
        name: 'studentHome',
        component: Student_Home
    },
    {
        path: '/teacher',
        name: 'teacherHome',
        component: Teacher_Home
    },
    {
        path: '/admin',
        name: 'adminHome',
        component: Admin_Home
    },
    {
        path: '/passwordChange',
        name: 'passwordChange',
        component: PasswordChange
    },
    {
        path: '/personalInfo',
        name: 'personalInfo',
        component: PersonalInfo
    },
    {
        path: '/exemptionApply',
        name: 'exemptionApply',
        component: ExemptionApply
    },
    {
        path: '/examDelay_Apply',
        name: 'examDelay_Apply',
        component: ExamDelay_Apply
    }

]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router
