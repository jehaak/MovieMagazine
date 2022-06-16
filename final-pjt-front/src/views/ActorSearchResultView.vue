<template>
  <div>



  <div class="w3-container w3-padding-32" id="projects">
    <h3 class="w3-border-bottom w3-border-light-grey w3-padding-16">Actor Result</h3>
  </div>
  <div class="w3-row w3-padding w3-border">
  <div class="w3-grid-container">
    <actor-card 
      v-for="actor in actorSearchResult" 
      :key="actor.local_id" 
      :actor="actor"
    ></actor-card>
  </div>
  </div>


<!-- 
    <actor-card 
      v-for="actor in actorSearchResult" 
      :key="actor.local_id" 
      :actor="actor"
    ></actor-card> -->
  </div>
</template>

<script>
import ActorCard from '@/cards/ActorCard'

import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'ActorSearchResult',
  data() {
    return {
      UrlKeyword: this.$route.params.keyword,
    }
  },
  components: {
    ActorCard,
  },
  computed: {
    ...mapGetters([
      'keyword', 'actorSearchResult',
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