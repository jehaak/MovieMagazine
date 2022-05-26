<template>
  <div>
    <!-- 장르 선택 -->
    <!-- <fieldset>
        <legend>장르를 선택하세요:</legend>
        <genre-choice
          v-for="genre in genres"
          :key="genre"
          :genre="genre"
        >
          <input type="checkbox" :id="genre" :name="genre"
          checked>
          <label :for="genre">{{ genre }}</label>    
        </genre-choice>
    </fieldset> -->


  <div class="w3-container w3-padding-32" id="projects">
    <h3 class="w3-border-bottom w3-border-light-grey w3-padding-16">Watched Movies</h3>
  </div>
  <div class="w3-row w3-padding w3-border">
  <div class="w3-grid-container">
        <search-movie-card
          class="w3-grid-item w3-col 13 m3 w3-margin-bottom"
          v-for="movie in movieSearchResult"
          :key="movie.id" 
          :movie="movie" :like="movie.like" :watched="movie.watched"
        ></search-movie-card>
  </div>
  </div>

  </div>
</template>

<script>
import SearchMovieCard from '@/components/SearchMovieCard'
// import GenreChoice from '@/components/GenreChoice.vue'

import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'MovieSearchResult',
  data() {
    return {
      UrlKeyword: this.$route.params.keyword,
      // showingMovies: [],
      // genres:  ['액션', '모험', '애니메이션', '코미디', '범죄', '다큐멘터리', '드라마', '가족', '판타지', '역사', '공포', '음악', '미스터리', '로맨스', 'SF', '스릴러', 'TV 영화', '전쟁', '서부']
    }
  },
  components: {
    SearchMovieCard, 
    // GenreChoice,
  },
  computed: {
    ...mapGetters([
      'keyword', 
      'movieSearchResult', 
      'choicedGenres'
    ]),
    // showingMovies() {
    //   return this.movieSearchResult.filter(
    //     movie => this.choicedGenres.includes(movie.genre)
    //   )
    // },
  },
  methods: {
    ...mapActions(['fetchSearchResult']),
    setSearchResult() {
      if (this.keyword !== this.UrlKeyword) {
        this.fetchSearchResult(this.UrlKeyword)
      }
    },
  },
  created() {
    this.setSearchResult()
  },
}
// 주는 데이터
// 검색어

// 받는 데이터
// 액터 리스트[{액터카드데이터}]
</script>

<style>

</style>