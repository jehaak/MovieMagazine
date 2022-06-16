<template>
<div>
  <div v-if="load">
    <!-- <p class="go-back">
      <button @click="$router.go(-2)">뒤로가기</button>
    </p> -->
  <!-- 감독 헤더 -->
  <header class="w3-border w3-container w3-center w3-padding-48 w3-white">
    <h1 class="w3-xxxlarge"><b>Director's Detail</b></h1>
    <h6>Welcome to <span class="w3-tag">{{directorInfo.name}}'s page</span></h6>
  </header>

  <!-- 감독 설명 -->
  <div class="w3-row w3-padding w3-border">
  <div style="padding-top:64px;">
    <div class="w3-row-padding">
      <div class="w3-col l8 m6">
        <h1 class="w3-jumbo"><b>{{directorInfo.name}}</b></h1>
        <h1 class="w3-xxxlarge w3-text-grey"><b>Your level: <i class="fa fa-heart" :style="directorColor"></i><span style="font-size: 1rem;"> {{directorLevel}}%</span></b></h1>
        <!-- <p><span class="w3-xlarge">Director's popularity is {{directorInfo.popularity}}</span></p> -->
        <p><span class="w3-xlarge">Director's popularity is {{directorInfo.popularity}}.</span> However, once you start to appreciate {{directorInfo.name}}'s effort to understand human life and lay out the thoughts via form of video spanning a couple of hours, you would definately be more into {{directorInfo.name}}. Find more about the director, by scrolling through the filmography of {{directorInfo.name}} for the film just apt for your vibe.
          It is always fun to explore foreign fields to meet the life friend of yours. This director's might be it!</p>
        <!-- 연출작 -->
        <!-- <vue-horizontal>
          <profile-movie-card
            v-for="movie in directedMovie" 
            :key="movie.id" 
            :movie="movie"
          ></profile-movie-card>
        </vue-horizontal> -->
        <!-- <h4 style="position:absolute; top:820px; left:250px; margin-left:20px; margin-top:0;">directed</h4> -->
      </div>
      <div class="w3-col l4 m6 w3-grayscale">
        <!-- 감독 얼굴 -->
        <img :src="imgURL" class="w3-image w3-right w3-hide-small" width="335" height="471">
        <!-- 감독 추천작 버튼 -->
        <b><button
            v-if="isLoggedIn" 
            onclick="document.getElementById('directorRecom').style.display='block'" 
            class="w3-button w3-light-grey w3-block "> 
            Director's Movie Recommend
        </button></b>
        <!-- <div class="w3-center w3-hide-large w3-hide-medium">
          <button class="w3-button w3-block w3-padding-large" onclick="document.getElementById('download').style.display='block'">
            <i class="fa fa-download"></i> Download Application
          </button>
          <img src="/w3images/img_app.jpg" class="w3-image w3-margin-top w3-grayscale" width="335" height="471">
        </div> -->
      </div>
    </div>
  </div>

  <!-- 감독 추천작 -->
  <div id="directorRecom" class="w3-modal">
    <div class="w3-modal-content w3-animate-top w3-card-4" style="max-width:400px">
      <header class="w3-container w3-black"> 
        <span onclick="document.getElementById('directorRecom').style.display='none'" 
        class="w3-button w3-display-topright">&times;</span>
        <h6>{{recomendMovie.title}}</h6>
      </header>
      <div class="w3-container">
        <div class="w3-justify w3-container">
          <div class="w3-center">
            <img :src="movieURL" class="w3-image w3-right w3-hide-small">
          </div>
          <p style="font-size:5px"><strong>popularity: {{recomendMovie.popularity}}</strong></p>
          <p style="font-size:13px">{{recomendMovie.overview}}</p>
          <!-- 좋아요, 봤어요 -->
          <p v-if="recomendMovie.like==='true'" class="w3-left"><button class="w3-button w3-white w3-border" style="width: 120px;" @click="[likeClick($event), likeAxios(recomendMovie.local_id)]">✓ Liked</button></p>
          <p v-if="recomendMovie.like==='false'" class="w3-left"><button class="w3-button w3-white w3-border" style="width: 120px;" @click="[likeClick($event), likeAxios(recomendMovie.local_id)]"><i class="fa fa-thumbs-up"></i> Like</button></p>
          <p v-if="recomendMovie.watched==='true'" class="w3-left"><button class="w3-button w3-white w3-border" style="width: 120px;" @click="[watchedClick($event), watchedAxios(recomendMovie.local_id)]">✓ Watched</button></p>
          <p v-if="recomendMovie.watched==='false'" class="w3-left"><button class="w3-button w3-white w3-border" style="width: 120px;" @click="[watchedClick($event), watchedAxios(recomendMovie.local_id)]"><i class="fa fa-video-camera"></i> Watch</button></p>
        </div>
      </div>
      <footer class="w3-container w3-black">
        <p>Recommended by {{directorInfo.name}}</p>
      </footer>
    </div>
  </div>

<hr class="w3-border">

<!-- 연출작 -->
        <h4 style="margin-left:20px; margin-top:0;">directed</h4>
        <vue-horizontal>
          <profile-movie-card
            v-for="movie in directedMovie" 
            :key="movie.id" 
            :movie="movie"
          ></profile-movie-card>
        </vue-horizontal>


  </div>
</div>
</div>
</template>

<script>
  import ProfileMovieCard from '@/cards/ProfileMovieCard.vue'
  // import HomeMovieCard from '@/components/HomeMovieCard.vue'
  import VueHorizontal from 'vue-horizontal'
  import drf from '@/api/drf'
  import axios from 'axios'

  import { mapGetters } from 'vuex'

  export default {
  name: 'DirectorProfileView',
  components: {
    ProfileMovieCard, VueHorizontal, 
    // HomeMovieCard
  },
  data () {
    return {
      load: false,

      directorId: this.$route.params.localId,
      directorLevel: null,
      recomendMovie: [],
      directorInfo: [],
      directorColor: '',
      directedMovie: [],
    }
  },
  computed: {
    ...mapGetters([
      // 'actorprofile',
      'isLoggedIn',
      'authHeader',
      ]),
    imgURL() {
      // console.log('액터디테일')
      // console.log(this.actorprofile)
      const img = drf.url.img() + this.directorInfo.profile_url
      if ( this.directorInfo.profile_url ){ return img}
      else { return drf.url.noPhoto() }
      // return drf.url.img() + this.directorInfo.profile_url
    },
    movieURL() {
      // console.log('액터디테일')
      // console.log(this.actorprofile)
      const img = drf.url.img() + this.recomendMovie.poster_url
      if ( this.recomendMovie.poster_url ){ return img}
      else { return drf.url.noPhoto() }
      // return drf.url.img() + this.directorInfo.profile_url
    }
  },
  methods: {
  //   // ...mapActions([
  //   //   'fetchActorProfileView',
  //   //   ]),
  //     setActorProfileData() {
  //     if (this.isLoggedIn) {
  //       // 로그인시에만 레벨정보, 추천영화 정보 보여줌
  //       this.actorLevel = this.actorprofile.actor_level
  //       if (this.actorprofile.recomend_movie !== "no_movie") {
  //         this.recomendMovie = this.actorprofile.recomend_movie
  //       }
  //     }
  //     this.actorInfo = this.actorprofile.actor_info
  //     this.castedMovie = this.actorprofile.casted_movies
  //   },
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
    if (this.isLoggedIn){
      // 로그인시 토큰 같이
      axios({
        url: drf.movies.director() + String(this.$route.params.localId),
        // url: drf.movies.actor(),
        method: 'get',
        headers: this.authHeader
      })
        .then(res => {
          const color = ["color: #D3D3D3;", "color: #A9A9A9", "color: #787878;", "color: #484848;", "color: #000000;", "color: #000000;"]
          // console.log('액터 ㅍㄿ')
          // console.log(res.data)
          this.directorLevel = parseInt(res.data.director_level)
          this.recomendMovie = res.data.recomend_movie
          this.directorInfo = res.data.director_info
          this.directorColor = color[parseInt(this.directorLevel/20)]
          this.directedMovie = res.data.directed_movies
          // commit('SET_ACTORPROFILE_VIEW', res.data)
          this.load = true
        })
        .catch(err => {
          console.error(err.response.data)
        })
    } else {
      // 비로그인시 토큰x
      axios({
        url: drf.movies.director() + String(this.$route.params.localId),
        method: 'get',
      })
      .then(res => {
          // console.log('액터 ㅍㄿ')
          // console.log(res.data)        
          // this.directorLevel = res.data.director_level
          // this.recomendMovie = res.data.recomend_movie
          this.directorInfo = res.data.director_info
          this.directedMovie = res.data.directed_movies
          // commit('SET_ACTORPROFILE_VIEW', res.data)
          this.load = true
      })
      .catch(err => {
        console.error(err.response.data)
      })
      // .finally(()=>{ router.push({name: 'actorProfile', params: {localId: id}}) })
    }
    // this.fetchActorProfileView(this.$route.params.localId)
    // this.setActorProfileData()
  },
}
</script>

<style></style>

