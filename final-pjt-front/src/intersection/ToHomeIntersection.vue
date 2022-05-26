<template>
  <h1>Please Wait For A Second</h1>
</template>

<script>
// import {mapActions} from 'vuex'
import router from '@/router'

export default {
  name: 'ToHomeInter',
  methods: {
    // ...mapActions([
    //   'fetchHomeView',
    //   ]),
  },
  created() {
    router.push({ name: 'home' })
          // .then(() => {router.push({ name: 'movieDetail', params: {localId: this.$route.params.localId} })})
  },
  // beforeMount() {router.push({ name: 'test', params: {localId: this.$route.params.localId} })}
}
</script>

<style>

</style>