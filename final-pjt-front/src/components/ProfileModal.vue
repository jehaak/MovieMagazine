<template>
  <div :id="id" class="w3-modal" style="display: none">
    <div class="w3-modal-content w3-animate-top w3-card-4" style="width=5rem">
      <!-- 헤더 -->
      <header class="w3-container w3-dark-grey"> 
        <span @click="modalClose(id)" id="myBtn"
        class="w3-button w3-display-topright">&times;</span>
        <h2>{{movie.title}}</h2>
      </header>
      <br>
      <!-- 바디 -->
      <div class="w3-container">
        <div class="w3-justify w3-container w3-row-padding">
          <div class="w3-center w3-col l4 m6" style="padding-bottom: 1.5rem">
            <img :src="movieURL()" class="w3-image w3-right w3-hide-small w3-greyscale">
          </div>
          <br>
          <div class="w3-col l8 m6">
            <p><strong>popularity: {{movie.popularity}}</strong></p>
            <p>{{movie.overview}}</p>
            <!-- 좋아요, 봤어요 -->
            <p v-if="movie['like']==='true'" class="w3-left"><button class="w3-button w3-white w3-border" style="width: 120px;" @click="[likeClick($event), likeAxios(movie['local_id'])]">✓ Liked</button></p>
            <p v-if="movie['like']==='false'" class="w3-left"><button class="w3-button w3-white w3-border" style="width: 120px;" @click="[likeClick($event), likeAxios(movie['local_id'])]"><i class="fa fa-thumbs-up"></i> Like</button></p>
            <p v-if="movie['watched']==='true'" class="w3-left"><button class="w3-button w3-white w3-border" style="width: 120px;" @click="[watchedClick($event), watchedAxios(movie['local_id'])]">✓ Watched</button></p>
            <p v-if="movie['watched']==='false'" class="w3-left"><button class="w3-button w3-white w3-border" style="width: 120px;" @click="[watchedClick($event), watchedAxios(movie['local_id'])]"><i class="fa fa-video-camera"></i> Watch</button></p>
          </div>
        </div>
      </div>
      <!-- 푸터 -->
      <footer class="w3-container w3-dark-grey">
        <p>recommended by {{ name }}</p>
      </footer>
    </div>
  </div>
</template>

<script>
  import drf from '@/api/drf'
  import { mapActions } from 'vuex'

  export default {
    name: 'ProfileModal',
    props: { id: Number, name: String, movie: Object },
    methods: {
      ...mapActions([
        'fetchMovieLike',
        'fetchMovieWatched'
        ]),

      modalClose(id) {
        var inst = document.getElementById(id);
        inst.style = "display: none;"
      },

      movieURL(){
        const img = drf.url.img() + this.movie.poster_url
        if ( this.movie.poster_url ){ return img}
        else { return drf.url.noPhoto() }
      },

      // like 함수
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
      // watch 함수
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
    // created(){
    //   console.log('무비')
    //   console.log(this.movie)
    // }
  }
</script>

<style>

</style>