const HOST = 'http://localhost:8000/'
const NO_PHOTO = 'https://i.pinimg.com/564x/85/6b/3f/856b3fb181ccecff71c06e9ce666a3ff.jpg'
const TMDB = 'https://image.tmdb.org/t/p/original'

const MOVIES = 'movies/'
const USER = 'user/'
// const BOARD = 'board/'
// const RECOMEND = 'recomend/'
const SEARCH = 'search/'
const ACCOUNTS = 'accounts/'

export default {
  url: {
    noPhoto: () => NO_PHOTO,
    img: () => TMDB,
  },
  user: {
    currentUserInfo: () => HOST + USER + 'user-info/',
    userProfile: () => HOST + USER + 'user-info/',
    userLike: () => HOST + MOVIES + 'like/',
    userWatched: () => HOST + MOVIES + 'watched/',
  },
  movies: {
    // /articles/
    home: () => HOST + MOVIES,
    actor: () => HOST + MOVIES + 'actor/',
    director: () => HOST + MOVIES + 'director/',
    detail: () => HOST + MOVIES + 'detail/',
  //   // /articles/1/
  //   article: articlePk => HOST + ARTICLES + `${articlePk}/`,
  //   likeArticle: articlePk => HOST + ARTICLES + `${articlePk}/` + 'like/',
  //   comments: articlePk => HOST + ARTICLES + `${articlePk}/` + COMMENTS,
  //   comment: (articlePk, commentPk) =>
  //     HOST + ARTICLES + `${articlePk}/` + COMMENTS + `${commentPk}/`,
  },
  searche: {
    search: () => HOST + SEARCH,
  },
  accounts: {
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    // Token 으로 현재 user 판단
    // username으로 프로필 제공
    profile: username => HOST + ACCOUNTS + 'profile/' + username,
    currentUserInfo: () => HOST + USER + 'user-info/',
    

  },
}
