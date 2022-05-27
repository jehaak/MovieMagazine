<template>
<div>
  <div v-if="load">
    <!-- <p class="go-back">
      <button @click="$router.go(-2)">뒤로가기</button>
    </p> -->

  <header class="w3-border w3-container w3-center w3-padding-48 w3-white">
    <h1 class="w3-xxxlarge"><b>Actor's Detail</b></h1>
    <h6>Welcome to <span class="w3-tag">{{actorInfo.name}}'s page</span></h6>
  </header>


<div class="w3-row w3-padding w3-border">
  <div style="padding-top: 64px">
    <div class="w3-row-padding">
      <div class="w3-col l8 m6">
        <h1 class="w3-jumbo"><b>{{actorInfo.name}}</b></h1>
        <h1 class="w3-xxxlarge w3-text-grey"><b>Your level: <i class="fa fa-heart" :style="actorColor"></i><span style="font-size: 1rem;"> {{actorLevel}}%</span></b></h1>
        <!-- <p><span class="w3-xlarge">Actor's popularity is {{actorInfo.popularity}}</span></p> -->
        <p><span class="w3-xlarge">Actor's popularity is {{actorInfo.popularity}}.</span> However, once you start to appreciate {{actorInfo.name}}'s effort to understand lines and lay out the feelings inside, you would definately be more into {{actorInfo.name}}. Find more about the actor, by scrolling through the filmography of {{actorInfo.name}} for the film just apt for your vibe.
          It is always fun to explore foreign fields to find the life friend of yours. This actor's might be it!</p>

      <!-- 출연작 -->
      <!-- <vue-horizontal>
        <profile-movie-card
          v-for="movie in castedMovie" 
          :key="movie.id" 
          :movie="movie"
        ></profile-movie-card>
      </vue-horizontal>
      <h4 style="position:absolute; top:820px; left:250px; margin-left:20px; margin-top:0;">featured</h4> -->


<!-- 추천 영화 모달 버튼 -->
      </div>
      <div class="w3-col l4 m6 w3-grayscale">
        <img :src="imgURL" class="w3-image w3-right w3-hide-small" width="335" height="471">
        <b><button
            v-if="isLoggedIn"
            onclick="document.getElementById('actorRecom').style.display='block'" 
            class="w3-button w3-light-grey w3-block "> 
            Actor's Movie Recommend
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




      <!-- <p><button 
            onclick="document.getElementById('id05').style.display='block'" 
            class="w3-button w3-light-grey w3-block ">
        Movie Recommend    
      </button></p> -->

    <!-- 추천 영화 모달 -->
    <div id="actorRecom" class="w3-modal">
      <div class="w3-modal-content w3-animate-top w3-card" style="max-width:400px">
        <!-- 헤더 -->
        <header class="w3-container w3-black"> 
          <span onclick="document.getElementById('actorRecom').style.display='none'" 
          class="w3-button w3-display-topright">&times;</span>
          <h6>{{recomendMovie.title}}</h6>
        </header>
        <!-- 카드바디 -->
        <div class="w3-container">
          <div class="w3-justify w3-container">
            <div class="w3-center">
              <img :src="movieURL" class="w3-image w3-right w3-hide-small">
              <p style="font-size:5px"><strong>popularity: {{recomendMovie.popularity}}</strong></p>
              <p style="font-size:13px">{{recomendMovie.overview}}</p>
            <!-- <home-movie-card 
            :movie="recomendMovie" :like="recomendMovie.like" :watched="recomendMovie.watched"
            ></home-movie-card> -->
            </div>
            <!-- 좋아요, 봤어요 -->
            <p v-if="recomendMovie.like==='true'" class="w3-left"><button class="w3-button w3-white w3-border" style="width: 120px;" @click="[likeClick($event), likeAxios(recomendMovie.local_id)]">✓ Liked</button></p>
            <p v-if="recomendMovie.like==='false'" class="w3-left"><button class="w3-button w3-white w3-border" style="width: 120px;" @click="[likeClick($event), likeAxios(recomendMovie.local_id)]"><i class="fa fa-thumbs-up"></i> Like</button></p>
            <p v-if="recomendMovie.watched==='true'" class="w3-left"><button class="w3-button w3-white w3-border" style="width: 120px;" @click="[watchedClick($event), watchedAxios(recomendMovie.local_id)]">✓ Watched</button></p>
            <p v-if="recomendMovie.watched==='false'" class="w3-left"><button class="w3-button w3-white w3-border" style="width: 120px;" @click="[watchedClick($event), watchedAxios(recomendMovie.local_id)]"><i class="fa fa-video-camera"></i> Watch</button></p>
          </div>
        </div>
        <!-- 푸터 -->
        <footer class="w3-container w3-black">
          <p>Recommended by {{actorInfo.name}}</p>
        </footer>
      </div>
    </div>



<hr class="w3-border">
      <!-- 출연작 -->
      <h4 style="margin-left:20px; margin-top:0;">featured</h4>
      <!-- <h4 style="position:absolute; top:820px; left:250px; margin-left:20px; margin-top:0;">featured</h4> -->
      <vue-horizontal>
        <profile-movie-card
          v-for="movie in castedMovie" 
          :key="movie.id" 
          :movie="movie"
        ></profile-movie-card>
      </vue-horizontal>



    </div>


 </div>
  </div>
</template>

<script>
  import ProfileMovieCard from '@/components/ProfileMovieCard.vue'
  // import HomeMovieCard from '@/components/HomeMovieCard.vue'
  import VueHorizontal from 'vue-horizontal'
  import drf from '@/api/drf'
  import axios from 'axios'

  import { mapGetters, mapActions } from 'vuex'

  export default {
  name: 'ActorProfileView',
  components: {
    // HomeMovieCard, 
    VueHorizontal, ProfileMovieCard,
  },
  data () {
    return {
      load: false,
      actorId: 0,
      actorLevel: null,
      recomendMovie: [],
      actorInfo: [],
      actorColor: '',
      castedMovie: [],
    }
  },
  computed: {
    ...mapGetters([
      // 'actorprofile',
      'isLoggedIn',
      'authHeader',
      ]),
    imgURL() {
      const img = drf.url.img() + this.actorInfo.profile_url
      if ( this.actorInfo.profile_url ){ return img}
      else { return drf.url.noPhoto() }
      // return drf.url.img() + this.actorInfo.profile_url
    },
    movieURL(){
      const img = drf.url.img() + this.recomendMovie.poster_url
      if ( this.recomendMovie.poster_url ){ return img}
      else { return drf.url.noPhoto() }
    }
  },
  methods: {
    ...mapActions([
      'fetchMovieLike',
      'fetchMovieWatched'
      ]),
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
        url: drf.movies.actor() + String(this.$route.params.localId),
        // url: drf.movies.actor(),
        method: 'get',
        headers: this.authHeader
      })
        .then(res => {
          const color = ["color: #D3D3D3;", "color: #A9A9A9", "color: #787878;", "color: #484848;", "color: #000000;", "color: #000000;"]
          console.log('액터 받아와')
          console.log(res.data)
          this.actorLevel = parseInt(res.data.actor_level)
          this.recomendMovie = res.data.recomend_movie
          this.actorInfo = res.data.actor_info
          this.actorColor = color[parseInt(this.actorLevel/20)]
          this.castedMovie = res.data.casted_movies
          this.load = true
          console.log(this.recomendMovie)
        })
        .catch(err => {
          console.error(err.response.data)
        })
    } else {
      // 비로그인시 토큰x
      axios({
        url: drf.movies.actor() + String(this.$route.params.localId),
        method: 'get',
      })
      .then(res => {
          // console.log('액터 ㅍㄿ')
          // console.log(res.data)        
          // this.actorLevel = res.data.actor_level
          // this.recomendMovie = res.data.recomend_movie
          this.actorInfo = res.data.actor_info
          this.castedMovie = res.data.casted_movies
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

