<template>
  <div>
    <director-card 
      v-for="director in directorSearchResult" 
      :key="director.local_id" 
      :director="director"
    ></director-card>
  </div>
</template>

<script>
import DirectorCard from '@/components/DirectorCard'

import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'DirectorSearchResult',
  data() {
    return {
      UrlKeyword: this.$route.params.keyword,
    }
  },
  components: {
    DirectorCard,
  },
  computed: {
    ...mapGetters([
      'keyword', 'directorSearchResult',
    ]),
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