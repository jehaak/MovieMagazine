<template>
  <h1>잠시만 기다려주세요</h1>
</template>

<script>
import {mapActions} from 'vuex'


export default {
  name: 'ActorProfileInter',
  methods: {
    ...mapActions([
      'fetchActorProfileView',
      ]),
  },
  created() {
    console.log(`인터미션 성공, id=${this.$route.params.localId}`)
    this.fetchActorProfileView(this.$route.params.localId)
      // .then(() => {router.push({ name: 'movieDetail', params: {localId: this.$route.params.localId} })})
  },
  // beforeMount() {router.push({ name: 'test', params: {localId: this.$route.params.localId} })}
}
</script>

<style>

</style>