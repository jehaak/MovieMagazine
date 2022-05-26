<template>
  <h1>잠시만 기다려주세요</h1>
</template>

<script>
import {mapActions} from 'vuex'

export default {
  name: 'SearchResultInter',
  methods: {
    ...mapActions([
      'fetchSearchResult',
      ]),
  },
  created() {
    this.fetchSearchResult(this.$route.params.keyword)
      // .then(() => {router.push({ name: 'movieDetail', params: {localId: this.$route.params.localId} })})
  },
  // beforeMount() {router.push({ name: 'test', params: {localId: this.$route.params.localId} })}
}
</script>

<style>

</style>