
const routes = [
  {
    path: '/',
    component: () => import('layouts/LoginLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Login.vue') }
    ]
  },
  {
    path: '/dietasapp',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/MainPage.vue') }
    ]
  },
  {
    path: '/menu',
    component: () => import('layouts/MenuLayout.vue'),
    children: [
      { path: '', component: () => import('pages/MenuPage.vue') }
    ]
  },
  {
    path: '/realizadas',
    component: () => import('layouts/RealizadasLayout.vue'),
    children: [
      { path: '', component: () => import('pages/RealizadasPage.vue') }
    ]
  },
  {
    path: '/registrar',
    component: () => import('layouts/RegisterLayout.vue'),
    children: [
      { path: '', component: () => import('pages/RegisterPage.vue') }
    ]
  },
  {
    path: '/chat',
    component: () => import('layouts/ChatLayout.vue'),
    children: [
      { path: '', component: () => import('pages/ChatPage.vue') }
    ]
  },
  {
    path: '/opciones',
    component: () => import('layouts/OpcionesLayout.vue'),
    children: [
      { path: '', component: () => import('pages/OpcionesPage.vue') }
    ]
  },
  {
    path: '/datos',
    component: () => import('layouts/DatosLayout.vue'),
    children: [
      { path: '', component: () => import('pages/DatosPage.vue') }
    ]
  }, 
  {
    path: '/reportes',
    component: () => import('layouts/ReportesLayout.vue'),
    children: [
      { path: '', component: () => import('pages/ReportesPage.vue') }
    ]
  },
  // Always leave this as last one,
  // but you can also remove it
  {
    path: '*',
    component: () => import('pages/Error404.vue')
  }
]

export default routes
