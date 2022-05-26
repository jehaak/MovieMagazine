<template>

<!-- Page content -->
<!-- <div class="w3-content w3-padding" style="max-width:1564px"> -->
<div>
  <!-- 1번 감독 모달 -->
    <div id="id01" class="w3-modal">
      <div class="w3-modal-content w3-animate-top w3-card-4" style="width=5rem">
        <header class="w3-container w3-dark-grey" style="50px"> 
          <span onclick="document.getElementById('id01').style.display='none'" 
          class="w3-button w3-display-topright">&times;</span>
          <h2>{{firstDirectorRecomend.title}}</h2>
        </header>
        <br>
        <div class="w3-container">
          <div class="w3-justify w3-container">
            <div class="w3-center">
            <home-movie-card 
            :movie="firstDirectorRecomend" :like="firstDirectorRecomend.like" :watched="firstDirectorRecomend.watched"
            ></home-movie-card>
            </div>
            <br>
            <p><strong>popularity: {{firstDirectorRecomend.popularity}}</strong></p>
            <p>{{firstDirectorRecomend.overview}}</p>
            <!-- 좋아요, 봤어요 -->
            <p 
              v-if="firstDirectorRecomend.like==='true'" 
              class="w3-left">
              <button 
                class="w3-button w3-white w3-border" 
                style="width: 120px;" 
                @click="[
                  likeClick($event), 
                  likeAxios(firstDirectorRecomend.local_id)
                  ]">
                  ✓ Liked
              </button>
            </p>
            <p v-if="firstDirectorRecomend.like==='false'" class="w3-left"><button class="w3-button w3-white w3-border" style="width: 120px;" @click="[likeClick($event), likeAxios(firstDirectorRecomend.local_id)]"><i class="fa fa-thumbs-up"></i> Like</button></p>
            <p v-if="firstDirectorRecomend.watched==='true'" class="w3-left"><button class="w3-button w3-white w3-border" style="width: 120px;" @click="[watchedClick($event), watchedAxios(firstDirectorRecomend.local_id)]">✓ Watched</button></p>
            <p v-if="firstDirectorRecomend.watched==='false'" class="w3-left"><button class="w3-button w3-white w3-border" style="width: 120px;" @click="[watchedClick($event), watchedAxios(firstDirectorRecomend.local_id)]"><i class="fa fa-video-camera"></i> Watch</button></p>
          </div>
        </div>
        <footer class="w3-container w3-dark-grey">
          <p>MOVIE MAGAGIN</p>
        </footer>
      </div>
    </div>
<!-- 1번감독 모달 끝 -->


    <!-- 2번 감독 모달 -->
    <div id="id02" class="w3-modal">
      <div class="w3-modal-content w3-animate-top w3-card-4" style="width=5rem">
        <header class="w3-container w3-dark-grey"> 
          <span onclick="document.getElementById('id02').style.display='none'" 
          class="w3-button w3-display-topright">&times;</span>
          <h2>{{secondDirectorRecomend.title}}</h2>
        </header>
        <br>
        <div class="w3-container">
          <div class="w3-justify w3-container">
            <div class="w3-center">
            <home-movie-card 
            :movie="secondDirectorRecomend" :like="secondDirectorRecomend.like" :watched="secondDirectorRecomend.watched"
            ></home-movie-card>
            </div>
            <br>
            <p><strong>popularity: {{secondDirectorRecomend.popularity}}</strong></p>
            <p>{{secondDirectorRecomend.overview}}</p>
            <!-- 좋아요, 봤어요 -->
            <p v-if="secondDirectorRecomend.like==='true'" class="w3-left"><button class="w3-button w3-white w3-border" style="width: 120px;" @click="[likeClick($event), likeAxios(secondDirectorRecomend.local_id)]">✓ Liked</button></p>
            <p v-if="secondDirectorRecomend.like==='false'" class="w3-left"><button class="w3-button w3-white w3-border" style="width: 120px;" @click="[likeClick($event), likeAxios(secondDirectorRecomend.local_id)]"><i class="fa fa-thumbs-up"></i> Like</button></p>
            <p v-if="secondDirectorRecomend.watched==='true'" class="w3-left"><button class="w3-button w3-white w3-border" style="width: 120px;" @click="[watchedClick($event), watchedAxios(secondDirectorRecomend.local_id)]">✓ Watched</button></p>
            <p v-if="secondDirectorRecomend.watched==='false'" class="w3-left"><button class="w3-button w3-white w3-border" style="width: 120px;" @click="[watchedClick($event), watchedAxios(secondDirectorRecomend.local_id)]"><i class="fa fa-video-camera"></i> Watch</button></p>
          </div>
        </div>
        <footer class="w3-container w3-dark-grey">
          <p>MOVIE MAGAGIN</p>
        </footer>
      </div>
    </div>
<!-- 2번감독 끝 -->

    <!-- 3번 감독 모달 -->
    <div id="id03" class="w3-modal">
      <div class="w3-modal-content w3-animate-top w3-card-4" style="width=5rem">
        <header class="w3-container w3-dark-grey"> 
          <span onclick="document.getElementById('id03').style.display='none'" 
          class="w3-button w3-display-topright">&times;</span>
          <h2>{{thirdDirectorRecomend.title}}</h2>
        </header>
        <br>
        <div class="w3-container">
          <div class="w3-justify w3-container">
            <div class="w3-center">
            <home-movie-card 
            :movie="thirdDirectorRecomend" :like="thirdDirectorRecomend.like" :watched="thirdDirectorRecomend.watched"
            ></home-movie-card>
            </div>
            <br>
            <p><strong>popularity: {{thirdDirectorRecomend.popularity}}</strong></p>
            <p>{{thirdDirectorRecomend.overview}}</p>
            <!-- 좋아요, 봤어요 -->
            <p v-if="thirdDirectorRecomend.like==='true'" class="w3-left"><button class="w3-button w3-white w3-border" style="width: 120px;" @click="[likeClick($event), likeAxios(thirdDirectorRecomend.local_id)]">✓ Liked</button></p>
            <p v-if="thirdDirectorRecomend.like==='false'" class="w3-left"><button class="w3-button w3-white w3-border" style="width: 120px;" @click="[likeClick($event), likeAxios(thirdDirectorRecomend.local_id)]"><i class="fa fa-thumbs-up"></i> Like</button></p>
            <p v-if="thirdDirectorRecomend.watched==='true'" class="w3-left"><button class="w3-button w3-white w3-border" style="width: 120px;" @click="[watchedClick($event), watchedAxios(thirdDirectorRecomend.local_id)]">✓ Watched</button></p>
            <p v-if="thirdDirectorRecomend.watched==='false'" class="w3-left"><button class="w3-button w3-white w3-border" style="width: 120px;" @click="[watchedClick($event), watchedAxios(thirdDirectorRecomend.local_id)]"><i class="fa fa-video-camera"></i> Watch</button></p>
          </div>
        </div>
        <footer class="w3-container w3-dark-grey">
          <p>MOVIE MAGAGIN</p>
        </footer>
      </div>
    </div>
    <!-- 3번 감독 모달 끝-->

    <!-- 1번 배우 모달 -->
    <div id="id04" class="w3-modal">
      <div class="w3-modal-content w3-animate-top w3-card-4" style="width=5rem">
        <header class="w3-container w3-dark-grey"> 
          <span onclick="document.getElementById('id04').style.display='none'" 
          class="w3-button w3-display-topright">&times;</span>
          <h2>{{firstActorRecomend.title}}</h2>
        </header>
        <br>
        <div class="w3-container">
          <div class="w3-justify w3-container">
            <div class="w3-center">
            <home-movie-card 
            :movie="firstActorRecomend" :like="firstActorRecomend.like" :watched="firstActorRecomend.watched"
            ></home-movie-card>
            </div>
            <br>
            <p><strong>popularity: {{firstActorRecomend.popularity}}</strong></p>
            <p>{{firstActorRecomend.overview}}</p>
            <!-- 좋아요, 봤어요 -->
            <p v-if="firstActorRecomend.like==='true'" class="w3-left"><button class="w3-button w3-white w3-border" style="width: 120px;" @click="[likeClick($event), likeAxios(firstActorRecomend.local_id)]">✓ Liked</button></p>
            <p v-if="firstActorRecomend.like==='false'" class="w3-left"><button class="w3-button w3-white w3-border" style="width: 120px;" @click="[likeClick($event), likeAxios(firstActorRecomend.local_id)]"><i class="fa fa-thumbs-up"></i> Like</button></p>
            <p v-if="firstActorRecomend.watched==='true'" class="w3-left"><button class="w3-button w3-white w3-border" style="width: 120px;" @click="[watchedClick($event), watchedAxios(firstActorRecomend.local_id)]">✓ Watched</button></p>
            <p v-if="firstActorRecomend.watched==='false'" class="w3-left"><button class="w3-button w3-white w3-border" style="width: 120px;" @click="[watchedClick($event), watchedAxios(firstActorRecomend.local_id)]"><i class="fa fa-video-camera"></i> Watch</button></p>
          </div>
        </div>
        <footer class="w3-container w3-dark-grey">
          <p>MOVIE MAGAGIN</p>
        </footer>
      </div>
    </div>
    <!-- 1번배우 모달 끝 -->

    <!-- 2번 배우 모달 -->
    <div id="id05" class="w3-modal">
      <div class="w3-modal-content w3-animate-top w3-card-4" style="width=5rem;">
        <header class="w3-container w3-dark-grey"> 
          <span onclick="document.getElementById('id05').style.display='none'" 
          class="w3-button w3-display-topright">&times;</span>
          <h2>{{secondActorRecomend.title}}</h2>
        </header>
        <br>
        <div class="w3-container">
          <div class="w3-justify w3-container">
            <div class="w3-center">
            <home-movie-card 
            :movie="secondActorRecomend" :like="secondActorRecomend.like" :watched="secondActorRecomend.watched"
            ></home-movie-card>
            </div>
            <br>
            <p><strong>popularity: {{secondActorRecomend.popularity}}</strong></p>
            <p>{{secondActorRecomend.overview}}</p>
            <!-- 좋아요, 봤어요 -->
            <p v-if="secondActorRecomend.like==='true'" class="w3-left"><button class="w3-button w3-white w3-border" style="width: 120px;" @click="[likeClick($event), likeAxios(secondActorRecomend.local_id)]">✓ Liked</button></p>
            <p v-if="secondActorRecomend.like==='false'" class="w3-left"><button class="w3-button w3-white w3-border" style="width: 120px;" @click="[likeClick($event), likeAxios(secondActorRecomend.local_id)]"><i class="fa fa-thumbs-up"></i> Like</button></p>
            <p v-if="secondActorRecomend.watched==='true'" class="w3-left"><button class="w3-button w3-white w3-border" style="width: 120px;" @click="[watchedClick($event), watchedAxios(secondActorRecomend.local_id)]">✓ Watched</button></p>
            <p v-if="secondActorRecomend.watched==='false'" class="w3-left"><button class="w3-button w3-white w3-border" style="width: 120px;" @click="[watchedClick($event), watchedAxios(secondActorRecomend.local_id)]"><i class="fa fa-video-camera"></i> Watch</button></p>
          </div>
        </div>
        <footer class="w3-container w3-dark-grey">
          <p>MOVIE MAGAGIN</p>
        </footer>
      </div>
    </div>
    <!-- 2번 배우 모달 끝 -->

    <!-- 3번 배우 모달 -->
    <div id="id06" class="w3-modal">
      <div class="w3-modal-content w3-animate-top w3-card-4" style="width=5rem">
        <header class="w3-container w3-dark-grey"> 
          <span onclick="document.getElementById('id06').style.display='none'" 
          class="w3-button w3-display-topright">&times;</span>
          <h2>{{thirdActorRecomend.title}}</h2>
        </header>
        <br>
        <div class="w3-container">
          <div class="w3-justify w3-container">
            <div class="w3-center">
            <home-movie-card 
            :movie="thirdActorRecomend" :like="thirdActorRecomend.like" :watched="thirdActorRecomend.watched"
            ></home-movie-card>
            </div>
            <br>
            <p><strong>popularity: {{thirdActorRecomend.popularity}}</strong></p>
            <p>{{thirdActorRecomend.overview}}</p>
            <!-- 좋아요, 봤어요 -->
            <p v-if="thirdActorRecomend.like==='true'" class="w3-left"><button class="w3-button w3-white w3-border" style="width: 120px;" @click="[likeClick($event), likeAxios(thirdActorRecomend.local_id)]">✓ Liked</button></p>
            <p v-if="thirdActorRecomend.like==='false'" class="w3-left"><button class="w3-button w3-white w3-border" style="width: 120px;" @click="[likeClick($event), likeAxios(thirdActorRecomend.local_id)]"><i class="fa fa-thumbs-up"></i> Like</button></p>
            <p v-if="thirdActorRecomend.watched==='true'" class="w3-left"><button class="w3-button w3-white w3-border" style="width: 120px;" @click="[watchedClick($event), watchedAxios(thirdActorRecomend.local_id)]">✓ Watched</button></p>
            <p v-if="thirdActorRecomend.watched==='false'" class="w3-left"><button class="w3-button w3-white w3-border" style="width: 120px;" @click="[watchedClick($event), watchedAxios(thirdActorRecomend.local_id)]"><i class="fa fa-video-camera"></i> Watch</button></p>
          </div>
        </div>
        <footer class="w3-container w3-dark-grey">
          <p>MOVIE MAGAGIN</p>
        </footer>
      </div>
    </div>
    <!-- 3번 배우 모달 끝 -->


  <header class="w3-border w3-container w3-center w3-padding-48 w3-white">
    <h1 class="w3-xxxlarge"><b>{{userNameUpper}}'s Page</b></h1>
    <h6>expressly designed for <span class="w3-tag">{{user_data.username}}</span></h6>
  </header>


  <div class="w3-row w3-padding w3-border">
  <div class="w3-container w3-padding-32" id="about">
    <h3 class="w3-border-bottom w3-border-light-grey w3-padding-16">About</h3>
    <p>How much do you know about your taste in films? Might you say there is no such thing like tate for you; "I just watch any genre, any movie available. I am willing to explore a wide veriety of uncharted territory." That is a respectable stance. Yet, your watch history reads a different line.
      Just as your website watch history or search history, the list of movies you have savered unveil your cinema preferance. This project is expressly designed to select a handful of perfect films only for you, based on which directors' works you like and which actors were featerd in them.
      Each director has his own style in filming and actors in expressing the scripts. Be gentle in emotional scene? Get every last drop of sweat to revive the reality? Or talk right at you about the crookied society that makes no sense whatsoever? This page will quench that unknown thirst hidden in mind.
    </p>
  </div>

<!-- 감독 추천 -->
  <h3 class="w3-border-bottom w3-border-light-grey w3-padding-16">Your Favorit Directors</h3>
  <div class="w3-row-padding w3-grayscale w3-border">

    <!-- 1번 감독 -->
    <div class="w3-col l3 m6 w3-margin-bottom">
      <router-link :to="{ name: 'directorProfile', params: {localId: first_director_info.id} }">
        <img :src="first_director_url" alt="John" style="width:212.49px;height:318.72px;object-fit:cover;">
        <h3>{{first_director_info.name}}</h3> <span><i class="fa fa-heart" :style="first_director_color"></i>  My Director Level: {{first_director_level}}%</span>
      </router-link>
      <p><button 
            onclick="document.getElementById('id01').style.display='block'" 
            class="w3-button w3-light-grey w3-block ">
            Movie Recommend    
      </button></p>
    </div>


    <!-- 2번 감독 -->
    <div class="w3-col l3 m6 w3-margin-bottom">
      <router-link :to="{ name: 'directorProfile', params: {localId: second_director_info.id} }">
        <img :src="second_director_url" alt="John" style="width:212.49px;height:318.72px;object-fit:cover;">
        <h3>{{second_director_info.name}}</h3> <span><i class="fa fa-heart" :style="second_director_color"></i>  My Director Level: {{second_director_level}}%</span>
      </router-link>
      <!-- <p class="w3-opacity">CEO & Founder</p> -->
      <!-- <p>Phasellus eget enim eu lectus faucibus vestibulum. Suspendisse sodales pellentesque elementum.</p> -->
      <p><button 
            onclick="document.getElementById('id02').style.display='block'" 
            class="w3-button w3-light-grey w3-block ">
            Movie Recommend    
      </button></p>
    </div>


    <!-- 3번 감독 -->
    <div class="w3-col l3 m6 w3-margin-bottom">
      <router-link :to="{ name: 'directorProfile', params: {localId: third_director_info.id} }">
      <img :src="third_director_url" alt="John" style="width:212.49px;height:318.72px;object-fit:cover;">
      <h3>{{ third_director_info.name }}</h3> <span><i class="fa fa-heart" :style="third_director_color"></i>  My Director Level: {{third_director_level}}%</span>
      </router-link>
      <!-- <p class="w3-opacity">CEO & Founder</p> -->
      <!-- <p>Phasellus eget enim eu lectus faucibus vestibulum. Suspendisse sodales pellentesque elementum.</p> -->
      <p><button 
            onclick="document.getElementById('id03').style.display='block'" 
            class="w3-button w3-light-grey w3-block ">
        Movie Recommend    
      </button></p>
    </div>


  </div>

<!-- 배우 추천 -->
  <h3 class="w3-border-bottom w3-border-light-grey w3-padding-16">Your Favorit Actors</h3>
  <div class="w3-row-padding w3-grayscale w3-border">

    <!-- 1번 배우 -->
    <div class="w3-col l3 m6 w3-margin-bottom">
      <router-link :to="{ name: 'actorProfile', params: {localId: first_actor_info.id} }">
      <img :src="first_actor_url" alt="John" style="width:212.49px;height:318.72px;object-fit:cover;">
      <h3>{{first_actor_info.name}}</h3> <span><i class="fa fa-heart" :style="first_actor_color"></i>  My Actor Level: {{first_actor_level}}%</span>
      </router-link>
      <!-- <p class="w3-opacity">CEO & Founder</p> -->
      <!-- <p>Phasellus eget enim eu lectus faucibus vestibulum. Suspendisse sodales pellentesque elementum.</p> -->
      <p><button 
            onclick="document.getElementById('id04').style.display='block'" 
            class="w3-button w3-light-grey w3-block ">
        Movie Recommend    
      </button></p>
    </div>


    <!-- 2번 배우 -->
    <div class="w3-col l3 m6 w3-margin-bottom">
      <router-link :to="{ name: 'actorProfile', params: {localId: second_actor_info.id} }">
      <img :src="second_actor_url" alt="John" style="width:212.49px;height:318.72px;object-fit:cover;">
      <h3>{{second_actor_info.name}}</h3> <span><i class="fa fa-heart" :style="second_actor_color"></i>  My Actor Level: {{second_actor_level}}%</span>
      </router-link>
      <!-- <p class="w3-opacity">CEO & Founder</p> -->
      <!-- <p>Phasellus eget enim eu lectus faucibus vestibulum. Suspendisse sodales pellentesque elementum.</p> -->
      <p><button 
            onclick="document.getElementById('id05').style.display='block'" 
            class="w3-button w3-light-grey w3-block ">
        Movie Recommend    
      </button></p>
    </div>

    <!-- 3번 배우 -->
    <div class="w3-col l3 m6 w3-margin-bottom">
      <router-link :to="{ name: 'actorProfile', params: {localId: third_actor_info.id} }">
      <img :src="third_actor_url" alt="John" style="width:212.49px;height:318.72px;object-fit:cover;">
      <h3>{{ third_actor_info.name }}</h3> <span><i class="fa fa-heart fa-solid" :style="third_actor_color"></i>  My Actor Level: {{third_actor_level}}%</span>
      </router-link>
      <!-- <p class="w3-opacity">CEO & Founder</p> -->
      <!-- <p>Phasellus eget enim eu lectus faucibus vestibulum. Suspendisse sodales pellentesque elementum.</p> -->
      <p><button 
            onclick="document.getElementById('id06').style.display='block'" 
            class="w3-button w3-light-grey w3-block ">
        Movie Recommend    
      </button></p>
    </div>


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
<p></p>
</div>
</div>
</template>

<script>
  // import MovieCard from '@/components/MovieCard'
  // import ActorCard from '@/components/ActorCard'
  // import DirectorCard from '@/components/DirectorCard'
  import HomeMovieCard from '@/components/HomeMovieCard.vue'
  import UserMovieCard from '@/components/UserMovieCard.vue'
  import { mapGetters, mapActions } from 'vuex'

  import axios from 'axios'
  import drf from '@/api/drf'
  import router from '@/router'
  // import VueHorizontal from 'vue-horizontal'
  

  export default {
  name: 'UserProfileView',
  components: {
    UserMovieCard, HomeMovieCard,
    // MovieCard, ActorCard, DirectorCard, VueHorizontal,
  },
  data () {
    return {
      load: false,
      userNameUpper: '',
      byDirectorRecomend: [],
      byActorRecomend: [],
      user_watched: [],
      user_data: {},

      // 배우정보
      first_actor_info: [],
      second_actor_info: [],
      third_actor_info: [],
      first_actor_level: 0,
      second_actor_level: 0,
      third_actor_level: 0,
      first_actor_color: '',
      second_actor_color: 0,
      third_actor_color: 0,
      firstActorRecomend: {},
      first_actor_url: '',
      secondActorRecomend: {},
      second_actor_url: '',
      thirdActorRecomend: {},
      third_actor_url: '',
      first_act_mov_url: '',
      second_act_mov_url: '',
      third_act_mov_url: '',

      // 감독정보
      first_director_info: [],
      second_director_info: [],
      third_director_info: [],
      first_director_level: 0,
      second_director_level: 0,
      third_director_level: 0,
      first_director_color: 0,
      second_director_color: 0,
      third_director_color: 0,
      firstDirectorRecomend: {},
      first_director_url: '',
      secondDirectorRecomend: {},
      second_director_url: '',
      thirdDirectorRecomend: {},
      third_director_url: '',
      first_dir_mov_url: '',
      second_dir_mov_url: '',
      third_dir_mov_url: '',
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
      // 'fetchUserProfile',
      'removeToken',
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
    if (this.isLoggedIn) {
      axios({
        url: drf.user.userProfile(), 
        method: 'get',
        headers: this.authHeader
      })
        .then(res => {
          const color = ["color: #D3D3D3;", "color: #A9A9A9", "color: #787878;", "color: #484848;", "color: #000000;", "color: #000000;"]
          console.log(res.data)

          this.firstDirectorRecomend = res.data.by_director_recomend.first_director
          this.secondDirectorRecomend = res.data.by_director_recomend.second_director
          this.thirdDirectorRecomend = res.data.by_director_recomend.third_director         
          this.byDirectorRecomend.push(res.data.by_director_recomend.first_director)
          this.byDirectorRecomend.push(res.data.by_director_recomend.second_director)
          this.byDirectorRecomend.push(res.data.by_director_recomend.third_director)

          this.firstActorRecomend = res.data.by_actor_recomend.first_actor
          this.secondActorRecomend = res.data.by_actor_recomend.second_actor
          this.thirdActorRecomend = res.data.by_actor_recomend.third_actor

          // this.byActorRecomend.push(res.data.by_actor_recomend.first_actor)
          // this.byActorRecomend.push(res.data.by_actor_recomend.second_actor)
          // this.byActorRecomend.push(res.data.by_actor_recomend.third_actor)
          this.user_watched = res.data.user_watched
          this.user_data = res.data.user_data
          this.userNameUpper = res.data.user_data.username.charAt(0).toUpperCase() + res.data.user_data.username.slice(1)

          // 감독정보 할당
          this.first_director_info = res.data.by_director_recomend.first_director_info
          this.second_director_info = res.data.by_director_recomend.second_director_info
          this.third_director_info = res.data.by_director_recomend.third_director_info

          this.first_director_level = parseInt(res.data.by_director_recomend.first_director_level)
          this.second_director_level = parseInt(res.data.by_director_recomend.second_director_level)
          this.third_director_level = parseInt(res.data.by_director_recomend.third_director_level)

          this.first_director_color = color[parseInt(this.first_director_level/20)]
          this.second_director_color = color[parseInt(this.second_director_level/20)]
          this.third_director_color = color[parseInt(this.third_director_level/20)]

          // 배우정보 할당
          this.first_actor_info = res.data.by_actor_recomend.first_actor_info
          this.second_actor_info = res.data.by_actor_recomend.second_actor_info
          this.third_actor_info = res.data.by_actor_recomend.third_actor_info

          this.first_actor_level = parseInt(res.data.by_actor_recomend.first_actor_level)
          this.second_actor_level = parseInt(res.data.by_actor_recomend.second_actor_level)
          this.third_actor_level = parseInt(res.data.by_actor_recomend.third_actor_level)

          // if (res.data.by_actor_recomend.first_actor_level <= 20) {this.first_actor_color = color[0]}
          // else if (res.data.by_actor_recomend.first_actor_level <= 20) {this.first_actor_color = color[0]}
          this.first_actor_color = color[parseInt(this.first_actor_level/20)]
          this.second_actor_color = color[parseInt(this.second_actor_level/20)]
          this.third_actor_color = color[parseInt(this.third_actor_level/20)]

          // 배우 이미지 할당
          if ( this.first_actor_info === 'no_actor' ){ this.first_actor_url = drf.url.noPhoto() }
          else if ( !this.first_actor_info.profile_url ){ this.first_actor_url = drf.url.noPhoto() }
          else { this.first_actor_url = drf.url.img() + this.first_actor_info.profile_url }          
          if ( this.second_actor_info === 'no_actor' ){ this.second_actor_url = drf.url.noPhoto() }
          else if ( !this.second_actor_info.profile_url ){ this.second_actor_url = drf.url.noPhoto() }
          else { this.second_actor_url = drf.url.img() + this.second_actor_info.profile_url }
          if ( this.third_actor_info === 'no_actor' ){ this.third_actor_url = drf.url.noPhoto() }
          else if ( !this.third_actor_info.profile_url ){ this.third_actor_url = drf.url.noPhoto() }
          else { this.third_actor_url = drf.url.img() + this.third_actor_info.profile_url }



          // 감독 이미지 할당
          if ( this.first_director_info === 'no_actor' ){ this.first_director_url = drf.url.noPhoto() }
          if ( !this.first_director_info.profile_url ){ this.first_director_url = drf.url.noPhoto() }
          else { this.first_director_url = drf.url.img() + this.first_director_info.profile_url }          
          if ( this.second_director_info === 'no_actor' ){ this.second_director_url = drf.url.noPhoto() }
          else if ( !this.second_director_info.profile_url ){ this.second_director_url = drf.url.noPhoto() }
          else { this.second_director_url = drf.url.img() + this.second_director_info.profile_url }
          if ( this.third_director_info === 'no_actor' ){ this.third_director_url = drf.url.noPhoto() }
          else if ( !this.third_director_info.profile_url ){ this.third_director_url = drf.url.noPhoto() }
          else { this.third_director_url = drf.url.img() + this.third_director_info.profile_url }

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
  //   // this.setUserProfileData()
  },
  // mounted() {
  //   this.setUserProfileData()
  // }
}
</script>

<style></style>