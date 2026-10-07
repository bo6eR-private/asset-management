import 'bootstrap/dist/js/bootstrap.bundle.min.js'
import '../css/style.css'
import { defineRoutes, startRouter } from './router.js'
import { dashboardPage } from './pages/dashboard.js'
import { assetsPage, assetPage, assetCreatePage, assetEditPage } from './pages/assets.js'
import { employeesPage, employeeCreatePage } from './pages/employees.js'
import { issuesPage, issueCreatePage, returnCreatePage } from './pages/issues.js'
import { reportsPage } from './pages/reports.js'

defineRoutes({
  dashboard: {
    path: '/',
    title: 'Учёт материальных ценностей',
    nav: 'dashboard',
    render: dashboardPage,
  },
  assets: {
    path: '/assets',
    title: 'Имущество',
    nav: 'assets',
    render: assetsPage,
  },
  asset: {
    path: '/assets/view',
    title: 'Карточка имущества — Учёт имущества',
    nav: 'assets',
    render: assetPage,
  },
  assetCreate: {
    path: '/assets/create',
    title: 'Добавление имущества — Учёт имущества',
    nav: 'assets',
    render: assetCreatePage,
  },
  assetEdit: {
    path: '/assets/edit',
    title: 'Изменение имущества — Учёт имущества',
    nav: 'assets',
    render: assetEditPage,
  },
  employees: {
    path: '/employees',
    title: 'Сотрудники — Учёт имущества',
    nav: 'employees',
    render: employeesPage,
  },
  employeeCreate: {
    path: '/employees/create',
    title: 'Добавление сотрудника — Учёт имущества',
    nav: 'employees',
    render: employeeCreatePage,
  },
  issues: {
    path: '/issues',
    title: 'Выдачи — Учёт имущества',
    nav: 'issues',
    render: issuesPage,
  },
  issueCreate: {
    path: '/issues/create',
    title: 'Оформление выдачи — Учёт имущества',
    nav: 'issues',
    render: issueCreatePage,
  },
  returnCreate: {
    path: '/issues/return',
    title: 'Оформление возврата — Учёт имущества',
    nav: 'issues',
    render: returnCreatePage,
  },
  reports: {
    path: '/reports',
    title: 'Отчёты — Учёт имущества',
    nav: 'reports',
    render: reportsPage,
  },
})

startRouter()
