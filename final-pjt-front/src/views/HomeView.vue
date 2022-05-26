<template>
  <div>
  <!-- Header -->
  <header class="w3-border w3-container w3-center w3-padding-48 w3-white">
    <h1 class="w3-xxxlarge"><b>MOVIE MAGAGINE</b></h1>
    <h6>Welcome to the site of <span class="w3-tag">Movie Recomend</span></h6>
  </header>

  <!-- Image header -->
  <header class="w3-display-container w3-wide" id="home">
    <img class="w3-image" src="@/assets/images/head.jpg" alt="headimage" width="1600" height="500">
    <div v-if="isLoggedIn">
      <div class="w3-display-left w3-padding-large">
        <br>
        <h1 class="w3-text-white">{{ currentUser.user_data.username }}'s style</h1>
        <h1 class="w3-jumbo w3-text-white w3-hide-small"><b>MOVIE </b></h1>
        <router-link :to="{ name: 'userProfile', params: { username } }">
        <h6><button class="w3-button w3-white w3-padding-large w3-large w3-opacity w3-hover-opacity-off" onclick="document.getElementById('subscribe').style.display='block'">Your Page</button></h6>
        </router-link>
      </div>
    </div>
    <div v-else>
      <div class="w3-display-left w3-padding-large">
        <br>
        <h1 class="w3-text-white">Find your</h1>
        <h1 class="w3-jumbo w3-text-white w3-hide-small"><b>MOVIE</b></h1>
        <h6><button class="w3-button w3-white w3-padding-large w3-large w3-opacity w3-hover-opacity-off" onclick="document.getElementById('loginbtn').style.display='block'">Login</button></h6>
      </div>
    </div>
  </header>


  <h1>Home</h1>

  <!-- 몸통 시작 -->
  <div v-if="load">
  <!-- Grid -->
  <div class="w3-row w3-padding w3-border">

    <!-- Blog entries -->
    <div class="w3-col l8 s12">
    
    <!-- 감독기반 추천영화 시작 -->
    <header class="w3-container w3-border w3-center w3-margin w3-padding-48 w3-white">
        <h1 class="w3-xxxlarge"><b>By Director Recomend</b></h1>
    </header>
      <div v-for="movie in byDirectorRecomend" :key="movie.id">
      <!-- 추천영화 있을때만 -->
      <div v-if="movie.movieInfo !== 'no_movie'">

      <!-- 추천영화 하나 -->
      <div class="w3-container w3-white w3-margin w3-padding-large">
        <div class="w3-center">
          <h3><b>{{movie.movieInfo.title}}</b></h3>
          <h5>{{movie.movieInfo.genre}}<span class="w3-opacity"></span></h5>
        </div>

        <div class="w3-justify w3-container">
          <div class="w3-center">
          <home-movie-card 
          :movie="movie.movieInfo" :like="movie.movieInfo.like" :watched="movie.movieInfo.watched"
          ></home-movie-card>
          </div>
          <br>
          <p><strong>popularity: {{movie.movieInfo.popularity}}</strong></p>
          <p>{{movie.movieInfo.overview}}</p>
          <!-- 좋아요, 봤어요 -->
          <p v-if="movie.movieInfo.like==='true'" class="w3-left"><button class="w3-button w3-white w3-border" style="width: 120px; margin: 2px;" @click="[likeClick($event), likeAxios(movie.movieInfo.local_id)]">✓ Liked</button></p>
          <p v-if="movie.movieInfo.like==='false'" class="w3-left"><button class="w3-button w3-white w3-border" style="width: 120px; margin: 2px;" @click="[likeClick($event), likeAxios(movie.movieInfo.local_id)]"><i class="fa fa-thumbs-up"></i> Like</button></p>
          <p v-if="movie.movieInfo.watched==='true'" class="w3-left"><button class="w3-button w3-white w3-border" style="width: 120px; margin: 2px" @click="[watchedClick($event), watchedAxios(movie.movieInfo.local_id)]">✓ Watched</button></p>
          <p v-if="movie.movieInfo.watched==='false'" class="w3-left"><button class="w3-button w3-white w3-border" style="width: 120px; margin: 2px" @click="[watchedClick($event), watchedAxios(movie.movieInfo.local_id)]"><i class="fa fa-video-camera"></i> Watch</button></p>
          <p class="w3-right"><button style="height:43px; width: 100px;" class="w3-button w3-black w3-border" @click="myFunction(movie.director.id)" id="myBtn">Director</button></p>
          <p class="w3-clear"></p>
          <div class="w3-row w3-margin-bottom" :id=movie.director.id style="display:none">
            <hr>
              <!-- <div class="w3-col l2 m3"> -->
              <p><b>Your Director</b></p>
              <!-- </div> -->
              <!--  style="width:90px;" -->
              <div style="width: 10; height: 12;">
              <home-director-card
              :director="movie.director"
              ></home-director-card>
              </div>
              <div class="w3-col l10 m9">
                <h4>{{ movie.director.name }}  </h4>
              <span span class="w3-opacity w3-medium">Popularity: {{movie.director.popularity}}</span>              </div>
          </div>
        </div>
      </div>
      <hr>
      </div>
      </div>
      <!-- 감독기반 추천영화 끝 -->

      <hr>

      <!-- 배우기반 추천영화 시작 -->
      <header class="w3-container w3-border w3-center w3-margin w3-padding-48 w3-white">
        <h1 class="w3-xxxlarge"><b>By Actor Recomend</b></h1>
      </header>
      <div v-for="movie in byActorRecomend" :key="movie.id">
      <!-- 추천영화 있을때만 -->
      <div v-if="movie.movieInfo !== 'no_movie'">

      <!-- 추천영화 하나 -->
      <div class="w3-container w3-white w3-margin w3-padding-large">
        <div class="w3-center">
          <h3><b>{{movie.movieInfo.title}}</b></h3>
          <h5>{{movie.movieInfo.genre}}<span class="w3-opacity"></span></h5>
        </div>

        <div class="w3-justify w3-container">
          <div class="w3-center">
          <home-movie-card 
          :movie="movie.movieInfo" :like="movie.movieInfo.like" :watched="movie.movieInfo.watched"
          ></home-movie-card>
          </div>
          <br>
          <p><strong>popularity: {{movie.movieInfo.popularity}}</strong></p>
          <p>{{movie.movieInfo.overview}}</p>
          <!-- 좋아요, 봤어요 -->
          <p v-if="movie.movieInfo.like==='true'" class="w3-left"><button class="w3-button w3-white w3-border" style="width: 120px; margin: 2px;" @click="[likeClick($event), likeAxios(movie.movieInfo.local_id)]">✓ Liked</button></p>
          <p v-if="movie.movieInfo.like==='false'" class="w3-left"><button class="w3-button w3-white w3-border" style="width: 120px; margin: 2px;" @click="[likeClick($event), likeAxios(movie.movieInfo.local_id)]"><i class="fa fa-thumbs-up"></i> Like</button></p>
          <p v-if="movie.movieInfo.watched==='true'" class="w3-left"><button class="w3-button w3-white w3-border" style="width: 120px; margin: 2px;" @click="[watchedClick($event), watchedAxios(movie.movieInfo.local_id)]">✓ Watched</button></p>
          <p v-if="movie.movieInfo.watched==='false'" class="w3-left"><button class="w3-button w3-white w3-border" style="width: 120px; margin: 2px;" @click="[watchedClick($event), watchedAxios(movie.movieInfo.local_id)]"><i class="fa fa-video-camera"></i> Watch</button></p>
         
          <p class="w3-right"><button style=" height:43px; width: 100px;" class="w3-button w3-black w3-border" @click="myFunction(movie.actor.id)" id="myBtn">Actor</button></p>
          <p class="w3-clear"></p>
          <div class="w3-row w3-margin-bottom" :id=movie.actor.id style="display:none">
            <hr>
              <!-- <div class="w3-col l2 m3"> -->
                <p><b>Your Actor</b></p>
              <!-- </div> -->
              <!--  style="width:90px;" -->
              <div style="width: 10; height: 12;">
              <!-- <div>{{ movie.actor.name }}</div> -->
              <home-actor-card
              :actor="movie.actor"
              ></home-actor-card>
              </div>
              <div class="w3-col l10 m9">
                <h4>{{ movie.actor.name }}</h4>
                 <span class="w3-opacity w3-medium">Popularity: {{movie.actor.popularity}}</span>
              </div>
          </div>
        </div>
      </div>
      <hr>
      </div>
      </div>
      <!-- 배우기반 추천영화 끝 -->
      
    <!-- END BLOG ENTRIES -->
    </div>

    <!-- About/Information menu -->
    <div class="w3-col l4">
      <!-- About Card -->
      <div class="w3-white w3-margin">
        <!-- <img :src=imgURL(hotMovies.poster_url) style="width:100%" class="w3-grayscale"> -->
        <div class="w3-container w3-black" >
          <h4>Today's Hot Movie</h4>
        </div>
        <div class="container w3-border" v-if="hotMovies!=='no_movie'">
        <br>
         <home-movie-card
        :movie="hotMovies"
        ></home-movie-card>
        <br>
        <div style="margin: 10px;"><b><i class="fa fa-thumbs-up"></i> In Today: {{hotMovies_cnt}} </b></div>
        <div style="margin: 10px;"><b> Popularity: {{ hotMovies.popularity }}</b></div>
        <hr>
      </div>
      </div>
      <hr>

      <!-- Posts -->
      <!-- <div v-for=""> -->
      <div class="w3-white w3-margin">
        <!-- <img :src=imgURL(hotMovies.poster_url) style="width:100%" class="w3-grayscale"> -->
        <div class="w3-container w3-black">
          <h4>Recent Movie</h4>
        </div>
        <div class="w3-border container" style="margin:0 auto;" v-for="movie in recentMovies" :key="movie.id">
          <br>
          <span class="w3-medium text-center"><b>Release_Date: {{ movie.release_date }}</b></span>
          <hr>
          <home-movie-card
          :movie="movie"
          ></home-movie-card>
          <hr>
        </div>
      </div>

    <!-- END About/Intro Menu -->
    </div>
    </div>
    </div>
    </div>
  <!-- END GRID -->
      <!-- 최신영화 -->

      <!-- 핫무비 -->

      <!-- 감독기반추천 --> 

      <!-- 배우추천 -->
</template>

<script>
// import MovieCard from '@/components/MovieCard'
import HomeMovieCard from '@/components/HomeMovieCard'
import HomeDirectorCard from '@/components/HomeDirectorCard.vue'
import HomeActorCard from '@/components/HomeActorCard.vue'
import { mapActions, mapGetters } from 'vuex'
// import VueHorizontal from 'vue-horizontal'
import axios from 'axios'
import drf from '@/api/drf'

export default {
  name: 'HomeView',
  components: {
    HomeMovieCard, HomeDirectorCard, HomeActorCard, 
  },
  data () {
    return {
      load: false,
      recentMovies: 0, 
      hotMovies: 0,
      hotMovies_cnt: -1,
      byActorRecomend: [],
      byDirectorRecomend: [],

      firstActorLevel: 0,
      secondActorLevel: 0,
      thirdActorLevel: 0,

      firstDirectorInfo: 0,
      secondDirectorInfo: 0,
      thirdDirectorInfo: 0,

      credentials: {
        username: '',
        password: '',
      }
    }
  },
  computed: {
    ...mapGetters([
      'authHeader', 'isLoggedIn', 'currentUser',
      ]),
    hotImgURL() {
      // return drf.url.img() + this.actor.profile_url
      const img = drf.url.img() + this.hotMovies.poster_url
      if ( this.hotMovies.poster_url ){ return img}
      else { return drf.url.noPhoto() }
    }
  },
  methods: {
    ...mapActions([
      'fetchHomeView', 
      'setHotMovie',
      'fetchSearchResult',
      'fetchMovieLike',
      'fetchMovieWatched',
      'login',
    ]),
      myFunction(id) {
      var x = document.getElementById(id);
      if (x.className.indexOf("w3-show") == -1) {
        x.className += " w3-show";
      } else { 
        x.className = x.className.replace(" w3-show", "");
      }
      //   event.target.className += " w3-show";
      // } else { 
      //   event.target.className = event.target.className.replace(" w3-show", "");
      // }
    },
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
      axios({
        url: drf.movies.home(),
          method: 'get',
          headers: this.authHeader
        })
          .then(res => {
            console.log(res.data)
            this.recentMovies = res.data.recent_movie
            this.hotMovies = res.data.hot_movie[0]
            if (res.data.hot_movie.length == 2) {
              this.hotMovies_cnt = res.data.hot_movie[1]
            }
            console.log(this.hotMovies_cnt)
            
            console.log('핫')
            console.log(this.hotMovies)
            // console.log(res.data.by_director_recomend.first_director)
            const temp1 = {}
            temp1.movieInfo = res.data.by_director_recomend.first_director
            temp1.director = res.data.by_director_recomend.first_director_info
            this.byDirectorRecomend.push(temp1)

            const temp2 = {}
            temp2.movieInfo = res.data.by_director_recomend.second_director
            temp2.director = res.data.by_director_recomend.second_director_info
            this.byDirectorRecomend.push(temp2)

            const temp3 = {}
            temp3.movieInfo = res.data.by_director_recomend.third_director
            temp3.director = res.data.by_director_recomend.third_director_info
            this.byDirectorRecomend.push(temp3)

            const atemp1 = {}
            atemp1.movieInfo = res.data.by_actor_recomend.first_actor
            atemp1.actor = res.data.by_actor_recomend.first_actor_info
            this.byActorRecomend.push(atemp1)

            const atemp2 = {}
            atemp2.movieInfo = res.data.by_actor_recomend.second_actor
            atemp2.actor = res.data.by_actor_recomend.second_actor_info
            this.byActorRecomend.push(atemp2)

            const atemp3 = {}
            atemp3.movieInfo = res.data.by_actor_recomend.third_actor
            atemp3.actor = res.data.by_actor_recomend.third_actor_info
            this.byActorRecomend.push(atemp3)

            console.log(this.byActorRecomend)

            this.firstActorLevel = res.data.first_director_level
            this.secondActorLevel = res.data.second_director_level
            this.thirdActorLevel = res.data.third_director_level

            // if (this.like === 'true') {
            //   this.like_state = 'true'
            // }
            // else {
            //   this.like_state = 'false'
            // }
            // if (this.watched === 'true') {
            //   this.watched_state = 'true'
            // }
            // else {
            //   this.watched_state = 'false'
            // }

            this.load = true
          })
    } else {
      axios({
        url: drf.movies.home(),
          method: 'get',
        })
          .then(res => {
            console.log(res.data)
            this.recentMovies = res.data.recent_movie
            // this.hotMovies = res.data.hot_movie[0]
            this.hotMovies = res.data.hot_movie[0]
            if (res.data.hot_movie.length == 2) {
              this.hotMovies_cnt = res.data.hot_movie[1]
            }
            // console.log('핫')
            // console.log(this.hotMovies)
            // console.log(res.data.by_director_recomend.first_director)
            // this.byDirectorRecomend.push(res.data.by_director_recomend.first_director)
            // this.byDirectorRecomend.push(res.data.by_director_recomend.second_director)
            // this.byDirectorRecomend.push(res.data.by_director_recomend.third_director)

            // this.byActorRecomend.push(res.data.by_actor_recomend.first_actor)
            // this.byActorRecomend.push(res.data.by_actor_recomend.second_actor)
            // this.byActorRecomend.push(res.data.by_actor_recomend.third_actor)
            
            // this.firstActorLevel = res.data.first_director_level
            // this.secondActorLevel = res.data.second_director_level
            // this.thirdActorLevel = res.data.third_director_level

            // this.firstDirectorInfo = res.data.first_director_info
            // this.secondDirectorInfo = res.data.second_director_info
            // this.thirdDirectorInfo = res.data.third_director_info

            this.load = true
          })      
    }

  },
  mounted() {
    }
}
</script>

<style>

</style>