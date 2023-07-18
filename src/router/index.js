import { createRouter, createWebHistory } from 'vue-router'
import routes from './routes'

const router = createRouter({
  history: createWebHistory(),
  routes
})


router.beforeEach(function (target, current, next) {

  next()
})

export default router
