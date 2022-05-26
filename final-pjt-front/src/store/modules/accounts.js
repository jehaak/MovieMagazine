
import router from '@/router'
import axios from 'axios'
import drf from '@/api/drf'


export default {
  // namespaced: true,

  // state는 직접 접근하지 않겠다!
  state: {
    token: localStorage.getItem('token') || '' ,
    currentUser: {},
    profile: {},
    authError: null,
    liked: false,
    wathed: false,
  },
  // 모든 state는 getters 를 통해서 접근하겠다.
  getters: {
    isLoggedIn: state => !!state.token,
    currentUser: state => state.currentUser,
    profile: state => state.profile,
    authError: state => state.authError,
    authHeader: state => ({ Authorization: `Token ${state.token}`}),
    liked: state => state.liked,
    watched: state => state.watched,
  },

  mutations: {
    SET_TOKEN: (state, token) => state.token = token,
    SET_CURRENT_USER: (state, user) => state.currentUser = user,
    SET_PROFILE: (state, profile) => state.profile = profile,
    SET_AUTH_ERROR: (state, error) => state.authError = error,
    SET_LIKED: (state, bool) => state.liked = bool,
    SET_WATCHED: (state, bool) => state.watched = bool,
  },

  actions: {
    saveToken({ commit }, token) {
      commit('SET_TOKEN', token)
      localStorage.setItem('token', token)
    },

    removeToken({ commit }) {
      commit('SET_TOKEN', '')
      localStorage.setItem('token', '')
    },

    login({ commit, dispatch }, credentials) {
      axios({
        url: drf.accounts.login(),
        method: 'post',
        data: credentials
      })
        .then(res => {
          const token = res.data.key
          dispatch('saveToken', token)
          dispatch('fetchCurrentUser', true)
          // alert('성공적으로 로그인')
          // router.push({ name: 'home' })
        })
        // .then(function() {router.push({ name: 'home' })})
        .catch(err => {
          console.error(err.response.data)
          commit('SET_AUTH_ERROR', err.response.data)
        })
        // .finally(function() {router.push({ name: 'home' })})
    },

    signup({ commit, dispatch }, credentials) {
      axios({
        url: drf.accounts.signup(),
        method: 'post',
        data: credentials
      })
        .then(res => {
          const token = res.data.key
          dispatch('saveToken', token)
          dispatch('fetchCurrentUser', true)
        })
        .catch(err => {
          console.error(err.response.data)
          commit('SET_AUTH_ERROR', err.response.data)
        })
        // .finally(function() {router.push({ name: 'home' })})
    },

    logout({ getters, dispatch }) {
      axios({
        url: drf.accounts.logout(),
        method: 'post',
        // data: {},
        headers: getters.authHeader,
      })
        .then(() => {
          dispatch('removeToken')
          document.getElementById('logout').style.display='block'
          router.push({ name: 'home' })
        })
        .error(err => {
          console.error(err.response)
        })
    },

    fetchCurrentUser({ commit, getters, dispatch }, goHome) {
      if (getters.isLoggedIn) {
        axios({
          url: drf.user.currentUserInfo(), 
          method: 'get',
          headers: getters.authHeader
        })
          .then(res => {
            console.log('되니?')
            commit('SET_CURRENT_USER', res.data)
            console.log('커런트유저 업뎃!')
            // router.push({ name: 'home' })
          })
          .then(res => {
            res
            console.log('기다려')
          })
          .catch(err => {
            if (err.response.status === 401) {
              dispatch('removeToken')
              router.push({ name: 'login' })
            }
          })
          .finally(function() {
            if(goHome){
              router.push({ name: 'toHomeInter' })
            }
          })
      }
    },

    // fetchUserProfile({ commit, getters, dispatch }) {
    fetchUserProfile({ commit }, res) {
      commit('SET_PROFILE', res)
      // if (getters.isLoggedIn) {
      //   axios({
      //     url: drf.user.userProfile(), 
      //     method: 'get',
      //     headers: getters.authHeader
      //   })
      //     .then(res => {
      //       commit('SET_PROFILE', res.data)
      //     })
      //     .catch(err => {
      //       if (err.response.status === 401) {
      //         dispatch('removeToken')
      //         router.push({ name: 'login' })
      //       }
      //     })
      //     // .finally(function() {
      //     //     router.push({ name: 'userProfile' })
      //     // })
      // }
    },

    fetchMovieLike({ commit, getters, dispatch }, id) {
      if (getters.isLoggedIn) {
        axios({
          url: drf.user.userLike() + String(id) + '/', 
          method: 'post',
          headers: getters.authHeader
        })
          .then(res => {
            console.log('라이크 보내기 성공')
            console.log(res.data)
            commit('SET_LIKED', res.data)
            dispatch('fetchCurrentUser', false)
            // dispatch('fetchHomeView')
          })
          .catch(err => {
            console.log('에러라도 띄워줘ㅜ')
            console.error(err)
            if (err.response.status === 401) {
              dispatch('removeToken')
              router.push({ name: 'login' })
            }
          })
      }
    },

    fetchMovieWatched({ commit, getters, dispatch }, id) {
      if (getters.isLoggedIn) {
        axios({
          url: drf.user.userWatched() + String(id) + '/', 
          method: 'post',
          headers: getters.authHeader
        })
          .then(res => {
            console.log(`봤어요 성공${res.data}`)
            commit('SET_WATCHED', res.data)
            dispatch('fetchCurrentUser', false)
            // dispatch('fetchHomeView')
          })
          .catch(err => {
            if (err.response.status === 401) {
              dispatch('removeToken')
              router.push({ name: 'login' })
            }
          })
      }
    },

    // fetchProfile({ commit, getters }, { username }) {
    //   /*
    //   GET: profile URL로 요청보내기
    //     성공하면
    //       state.profile에 저장
    //   */
    //   axios({
    //     url: drf.accounts.profile(username),
    //     method: 'get',
    //     headers: getters.authHeader,
    //   })
    //     .then(res => {
    //       commit('SET_PROFILE', res.data)
    //     })
    // },
  },
}
