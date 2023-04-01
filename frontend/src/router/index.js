import { createRouter, createWebHashHistory } from 'vue-router'
import StudentTable from '../components/StudentTable.vue'
import SubjectTable from '../components/SubjectTable.vue'

const routes = [
  {
    path: '/',
    name: 'students',
    component: StudentTable,
  },
  {
    path: '/edit/:id',
    name: 'edit',
    component: () => import(/* webpackChunkName: "edit" */ '../components/StudentForm.vue')
  },
  {
    path: '/add',
    name: 'add',
    component: () => import(/* webpackChunkName: "add" */ '../components/StudentForm.vue')
  },
  {
    path: '/subjects',
    name: 'subjects',
    component: SubjectTable
  },
  {
    path: '/subjects/edit/:id',
    name: 'editSubject',
    component: () => import(/* webpackChunkName: "edit" */ '../components/SubjectForm.vue')
  },
  {
    path: '/subjects/add',
    name: 'addSubject',
    component: () => import(/* webpackChunkName: "add" */ '../components/SubjectForm.vue')
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
