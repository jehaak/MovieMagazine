<template>
<!-- Page content -->
<!-- <div class="w3-content w3-padding" style="max-width:1564px"> -->
<div>  
  <!-- 1번 감독 모달 -->
    <profile-modal
      v-for="(movie, idx) in directorRecommend" 
      :key="idx" 
      :id="directorInfo[idx]['id']"
      :name="directorInfo[idx]['name']"
      :movie="movie"
    ></profile-modal>
<!-- 1번감독 모달 끝 -->


    <!-- 1번 배우 모달 -->
    <profile-modal
      v-for="(movie, idx) in actorRecommend" 
      :key="idx" 
      :id="actorInfo[idx]['id']"
      :name="actorInfo[idx]['name']"
      :movie="movie"
    ></profile-modal>
    <!-- 1번배우 모달 끝 -->


  <header class="w3-border w3-container w3-center w3-padding-48 w3-white">
    <h1 class="w3-xxxlarge"><b>{{userNameUpper}}'s Page</b></h1>
    <h6>expressly designed for <span class="w3-tag">{{user_data.username}}</span></h6>
  </header>


  <div class="w3-row w3-padding w3-border">

    <div class="w3-container w3-padding-32" id="about">
      <h3 class="w3-border-bottom w3-border-light-grey w3-padding-16">About</h3>
      <p>How much do you know about your taste in films? Might you say there is no such thing like "movie taste" to you; "I just watch any genre, any movie available. I am willing to explore a wide veriety of uncharted territory." That is a respectable stance. Yet, your watch history reads a different line.
        Just as your website watch history or search history, the list of movies you have savered unveil your cinema preferance. This project is expressly designed to select a handful of perfect films only for you, based on which directors' works you like and which actors were featerd in them.
        Each director has his own style in filming and actors in expressing the scripts. Be gentle in emotional scene? Get every last drop of sweat to revive the reality? Or talk right at you about the crookied society that makes no sense whatsoever? This page will quench that unknown thirst hidden in mind.
      </p>
    </div>

  <!-- 감독 추천 -->
    <h3 class="w3-border-bottom w3-border-light-grey w3-padding-16">Your Favorit Directors</h3>
    <div class="w3-row-padding w3-grayscale w3-border">

      <!-- 감독 카드 -->
      <director-profile-card
        v-for="(director, idx) in directorInfo" 
        :key="idx" 
        class="w3-col l3 m6 w3-margin-bottom"
        :director="director">
      </director-profile-card>

    </div>

  <!-- 배우 추천 -->
    <h3 class="w3-border-bottom w3-border-light-grey w3-padding-16">Your Favorit Actors</h3>
    <div class="w3-row-padding w3-grayscale w3-border">

      <!-- 배우 카드 -->
      <actor-profile-card
        v-for="(actor, idx) in actorInfo" 
        :key="idx" 
        class="w3-col l3 m6 w3-margin-bottom"
        :actor="actor">
      </actor-profile-card>

    </div>


    <!-- 본 영화 목록 -->
    <div class="w3-container w3-padding-32" id="projects">
      <h3 class="w3-border-bottom w3-border-light-grey w3-padding-16">Watched Movies</h3>
    </div>
    <div class="w3-row w3-padding w3-border">
      <div class="w3-grid-container">
        <user-movie-card
          class="w3-grid-item w3-col 13 m3 w3-margin-bottom"
          v-for="movie in user_watched"
          :key="movie.id" 
          :movie="movie" :like="movie.like" :watched="movie.watched"
        ></user-movie-card>
      </div>
    </div>


    <div class="w3-container">
      <img src="@/assets/images/head.jpg" class="w3-image" style="width:100%">
    </div>

    
    <br>
    Lv.0%~20%<i class="fa fa-heart" style="color: #D3D3D3;"></i>
    &nbsp;&nbsp;Lv.20%~40%<i class="fa fa-heart" style="color: #A9A9A9;"></i>
    &nbsp;&nbsp;Lv.40%~60%<i class="fa fa-heart" style="color: #787878;"></i>
    &nbsp;&nbsp;Lv.60%~80%<i class="fa fa-heart" style="color: #484848;"></i>
    &nbsp;&nbsp;Lv.80%~100%<i class="fa fa-heart" style="color: #000000;"></i>
  </div>

</div>
</template>

<script>
  import UserMovieCard from '@/cards/UserMovieCard.vue'
  import ProfileModal from '@/components/ProfileModal.vue'
  import ActorProfileCard from '@/cards/ActorProfileCard.vue'
  import DirectorProfileCard from '@/cards/DirectorProfileCard.vue'
  import { mapGetters, mapActions } from 'vuex'



  import axios from 'axios'
  import drf from '@/api/drf'
  import router from '@/router'
  

  export default {
  name: 'UserProfileView',
  components: { 
    UserMovieCard, 
    ProfileModal, 
    ActorProfileCard,
    DirectorProfileCard, 
  },
  data () {
    return {
      load: false,
      // 유저 정보
      userNameUpper: '',
      user_watched: [],
      user_data: {},
      // 배우정보
      actorInfo: [],
      actorRecommend: [],
      // 감독정보
      directorInfo: [],
      directorRecommend: [],
    }
  },
  computed: {
    ...mapGetters([
      'isLoggedIn',
      'authHeader'
      // 'profile',
      ]),
  },
  methods: {
    ...mapActions([
      'removeToken',
      'fetchMovieLike',
      'fetchMovieWatched'
      ]),
    // like
    likeClick(event) {
    console.log(event.target.innerHTML)
    if (event.target.innerHTML === '<i class="fa fa-thumbs-up"></i> Like') {
      event.target.innerHTML = '✓ Liked'
    }
    else {
      event.target.innerHTML = '<i class="fa fa-thumbs-up"></i> Like'
    }
    },
    likeAxios(id) {
    this.fetchMovieLike(id)
    },
    // watched
    watchedClick(event) { 
    console.log(event.target.value)
    if (event.target.innerHTML === '<i class="fa fa-video-camera"></i> Watch') {
      event.target.innerHTML = '✓ Watched'
    }
    else {
      event.target.innerHTML = '<i class="fa fa-video-camera"></i> Watch'
    }
    },
    watchedAxios(id) {
    this.fetchMovieWatched(id)
    },
  },
  created() {
    if (this.isLoggedIn) {
      axios({
        url: drf.user.userProfile(), 
        method: 'get',
        headers: this.authHeader
      })
        .then(res => {
          // 유저 정보
          this.user_watched = res.data.user_watched
          this.user_data = res.data.user_data
          this.userNameUpper = res.data.user_data.username.charAt(0).toUpperCase() + res.data.user_data.username.slice(1)

          // 감독정보 할당
          this.directorInfo.push(res.data.by_director_recomend.first_director_info)
          this.directorInfo.push(res.data.by_director_recomend.second_director_info)
          this.directorInfo.push(res.data.by_director_recomend.third_director_info)

          this.directorInfo[0] = {...this.directorInfo[0], 'level': parseInt(res.data.by_director_recomend.first_director_level) }
          this.directorInfo[1] = {...this.directorInfo[1], 'level': parseInt(res.data.by_director_recomend.second_director_level) }
          this.directorInfo[2] = {...this.directorInfo[2], 'level': parseInt(res.data.by_director_recomend.third_director_level) }

          this.directorRecommend.push(res.data.by_director_recomend.first_director)
          this.directorRecommend.push(res.data.by_director_recomend.second_director)
          this.directorRecommend.push(res.data.by_director_recomend.third_director)

          // 배우정보 할당
          this.actorInfo.push(res.data.by_actor_recomend.first_actor_info)
          this.actorInfo.push(res.data.by_actor_recomend.second_actor_info)
          this.actorInfo.push(res.data.by_actor_recomend.third_actor_info)

          this.actorInfo[0] = {...this.actorInfo[0], 'level': parseInt(res.data.by_actor_recomend.first_actor_level) }
          this.actorInfo[1] = {...this.actorInfo[1], 'level': parseInt(res.data.by_actor_recomend.second_actor_level) }
          this.actorInfo[2] = {...this.actorInfo[2], 'level': parseInt(res.data.by_actor_recomend.third_actor_level) }

          this.actorRecommend.push(res.data.by_actor_recomend.first_actor)
          this.actorRecommend.push(res.data.by_actor_recomend.second_actor)
          this.actorRecommend.push(res.data.by_actor_recomend.third_actor)

          this.load = true
          // this.fetchUserProfile(res.data)
        })
        .catch(err => {
          if (err.response.status === 401) {
            this.removeToken()
            router.push({ name: 'login' })
          }
        })
    }
  },
}
</script>

<style></style>