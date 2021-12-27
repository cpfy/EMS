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
import ScoreRevise_Apply from "../views/ScoreRevise_Apply";
import Leave_Apply from "../views/Leave_Apply";

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
        path: '/student/exemptionApply',
        name: 'exemptionApply',
        component: ExemptionApply
    },
    {
        path: '/student/examDelay_Apply',
        name: 'examDelay_Apply',
        component: ExamDelay_Apply
    },{
        path: '/teacher/scoreRevise_Apply',
        name: 'scoreRevise_Apply',
        component: ScoreRevise_Apply
    },
    {
        path: '/teacher/leave_Apply',
        name: 'leave_Apply',
        component: Leave_Apply
    }


]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router
