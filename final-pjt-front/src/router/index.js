import Vue from 'vue'
import VueRouter from 'vue-router'

// import { UserService } from './../service/user.service';
// import store from './../store';

import HomeView from '../views/HomeView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'
import ActorProfileView from '@/views/ActorProfileView.vue'
import DirectorProfileView from '@/views/DirectorProfileView.vue'
import SearchResultView from '@/views/SearchResultView.vue'
import DirectorSearchResultView from '@/views/DirectorSearchResultView.vue'
import ActorSearchResultView from '@/views/ActorSearchResultView.vue'
import MovieSearchResultView from '@/views/MovieSearchResultView.vue'

import ToHomeIntersection from '@/intersection/ToHomeIntersection.vue'

import LoginView from '@/views/LoginView.vue'
import LogoutView from '@/views/LogoutView.vue'
import SignupView from '@/views/SignupView.vue'
import UserProfileView from '@/views/UserProfileView.vue'
import NotFound404 from '../views/NotFound404.vue'
// import { component } from 'vue/types/umd'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/detail/movie/:localId',
    name: 'movieDetail',
    component: MovieDetailView
  },
  {
    path: '/profile/actor/:localId',
    name: 'actorProfile',
    component: ActorProfileView
  },
  {
    path: '/profile/director/:localId',
    name: 'directorProfile',
    component: DirectorProfileView
  },
  {
    path: '/search/result/:keyword',
    name: 'searchResult',
    component: SearchResultView
  },
  {
    path: '/search/director/:keyword',
    name: 'directorSearchResult',
    component: DirectorSearchResultView
  },
  {
    path: '/search/actor/:keyword',
    name: 'actorSearchResult',
    component: ActorSearchResultView
  },
  {
    path: '/search/movie/:keyword',
    name: 'movieSearchResult',
    component: MovieSearchResultView
  },
  // ====================================
  // intersection
  // ====================================
  {
    path: '/toHomeInter/:keyword',
    name: 'toHomeInter',
    component: ToHomeIntersection
  },
  // ===================================
  // accounts
  // ===================================
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/logout',
    name: 'logout',
    component: LogoutView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView
  },
  {
    path: '/profile',
    name: 'userProfile',
    component: UserProfileView,
  },
  // =================================
  // 404 페이지
  // =================================
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '*',
    redirect: '/404'
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

/*
Navigation Guard 설정
  (이전 페이지에서 있던 에러 메시지 삭제)

  로그인(Authentication)이 필요 없는 route 이름들 저장(/login, /signup)

  0. router 에서 이동 감지

  1. 현재 이동하고자 하는 페이지가 로그인이 필요한지 확인
  
  2. 로그인이 필요한 페이지인데 로그인이 되어있지 않다면
    로그인 페이지(/login)로 이동

  3. 로그인이 되어 있다면
    원래 이동할 곳으로 이동
  
  4. 로그인이 되어있는데 /login, /signup 페이지로 이동한다면
    메인 페이지(/)로 이동
    

*/

const originalPush = VueRouter.prototype.push;
VueRouter.prototype.push = function push(location) {
	return originalPush.call(this, location).catch(err => {
		if (err.name !== 'NavigationDuplicated') throw err;
	});
};

export default router
