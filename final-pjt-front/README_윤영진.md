# 영화산업진흥위원회 front_end

## 바뀐 것

#### 0519

- Home -> newMovie -> movieCard

#### 0522

- 장고에서
  - search는 post로 바꿈



## Router 모음

##### movies

```javascript
{'/', 'home', HomeView},
{'/detail/movie/:moviePk', 'movieDetail', MovieDetailView},
{'/profile/actor/:localId', 'actorProfile', ActorProfileView},
{'/profile/director/:localId', 'directorProfile', DirectorProfileView},
{'/search/result/:keyword', 'searchResult', SearchResultView},
{'/search/director/:keyword', 'directorSearchResult', DirectorSearchResultView},
{'/search/actor/:keyword', 'actorSearchResult', ActorSearchResultView},
{'/search/movie/:keyword', 'movieSearchResult', MovieSearchResultView},
```

##### accounts

```javascript
  // accounts
{'/login', 'login', LoginView},
{'/logout', 'logout', LogoutView},
{'/signup', 'signup', SignupView},
{'/profile/:username', 'userProfile', UserProfileView},
```

##### 404

```javascript
  // 404 페이지
  {'/404', 'NotFound404', NotFound404},
  {'*', redirect:'/404'},
```



## movies vuex 모음

##### state

```javascript
newMovies: [] //최신 영화 정보
hotMovies: [] //오늘 좋아요 가장 많이 받은 영화 정보
recommendByDirector: [], // 해당 감독에 대한 추천 영화
recommendByActor: [], // 해당 배우에 대한 추천 영화
recommendByUser: [], // 비슷한 유저들 바탕으로 영화 추천
```

##### getters

```javascript
// state에 있는 전부 다
```

##### mutations

```javascript
// SET_어쩌구 (state, state인스턴스이름)
// state 인스턴스 바꾸는 메소드 전부 다
```

##### actions

```javascript
// fetch어쩌구Movies ({commit}, num)
// fetchRecommendBy어쩌구 ({commit}, {user_id, num})
// state 인스턴스 장고에서 받아오는 액션 전부 다
```

오스 헤더 필요한 경우

영화 좋아요/봤어요 누를 때 

추천영화 요청



fetch()

=>컴색어 발송

백에서는 => 패키지로 옵니다!{

perfect: {actor: [{인스턴스1},{인스턴스2}], director: [], movie:[]}

director: [{},{},{}, ...]

actor: [{},{},{}, ...]

movie: [{},{},{}, ...]

}

모든 3000개의 검색 결과가!)



영화 좋아요 봤어요 정보는 로그인, 이나 뭐 뭐 할 때 받는게 아니라 걍 영화 카드 띄울 때 받는걸로!



우선순위 낮음!

'자동완성ㄷㄷㄷ'



이 알고리즘은 시간이 남을 때 구현! + 시간 최적화 구현

검색: 반지의 제왕

배우: 박제왕

감독: 반지하, 의제왕, 강'의'선
