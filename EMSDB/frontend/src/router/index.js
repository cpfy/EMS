import {createRouter, createWebHistory} from 'vue-router'
import Login from '../views/Login.vue';
import Student_Home from "../views/student/Student_Home";
import Teacher_Home from "../views/teacher/Teacher_Home"
import Admin_Home from "../views/Admin_Home";
import PasswordChange from "../views/PasswordChange";
import test from "../views/test";
import PersonalInfo from "../views/PersonalInfo";
import ExemptionApply from "../views/student/Exemption_Apply";
import ExamDelay_Apply from "../views/student/ExamDelay_Apply";
import ScoreRevise_Apply from "../views/teacher/ScoreRevise_Apply";
import Leave_Apply from "../views/teacher/Leave_Apply";
import OtherApply from "../views/Other_Apply";
import Notice_Send from "../views/Notice_Send";
import Student_SysNotice from "../views/student/Student_SysNotice";
import Student_CourseSelect from "../views/student/Student_CourseSelect";
import Student_courseDrop from "../views/student/Student_CourseDrop";
import Student_Schedule from "../views/student/Student_Schedule";
import Student_ScheduleRecommend from "../views/student/Student_ScheduleRecommend";
import Teacher_Schedule from "../views/teacher/Teacher_Schedule";
import Student_ExamSchedule from "../views/student/Student_ExamSchedule";
import EmptyRoom from "../views/EmptyRoom";
import CourseEvaluate from "../views/student/CourseEvaluate";

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
    }, {
        path: '/teacher/scoreRevise_Apply',
        name: 'scoreRevise_Apply',
        component: ScoreRevise_Apply
    },
    {
        path: '/teacher/leave_Apply',
        name: 'leave_Apply',
        component: Leave_Apply
    },
    {
        path: '/other_Apply',
        name: 'other_Apply',
        component: OtherApply
    },
    {
        path: '/admin/notice_Send',
        name: 'notice_Send',
        component: Notice_Send
    },
    {
        path: '/student/sysNotice',
        name: 'student_SysNotice',
        component: Student_SysNotice
    },
    {
        path: '/student/courseSelect',
        name: 'student_CourseSelect',
        component: Student_CourseSelect
    },
    {
        path: '/student/courseDrop',
        name: 'student_CourseDrop',
        component: Student_courseDrop
    },
    {
        path: '/student/schedule',
        name: 'student_Schedule',
        component: Student_Schedule
    },
    {
        path: '/student/scheduleRecommend',
        name: 'student_ScheduleRecommend',
        component: Student_ScheduleRecommend
    },
    {
        path: '/teacher/schedule',
        name: 'teacher_Schedule',
        component: Teacher_Schedule
    },
    {
        path: '/student/examSchedule',
        name: 'student_ExamSchedule',
        component: Student_ExamSchedule
    },
    {
        path: '/emptyRoom',
        name: 'emptyRoom',
        component: EmptyRoom
    }, {
        path: '/student/courseEvaluate',
        name: 'student_courseEvaluate' ,
        component: CourseEvaluate
    }

]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router
