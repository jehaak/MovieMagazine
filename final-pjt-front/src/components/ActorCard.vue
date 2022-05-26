// 받는
// URL, 이름
// 좋아요 여부
// 나의 액터 레벨

<template>
    <!-- <div class="w3-white w3-margin" style="width: 18rem;">
    <router-link :to="{ name: 'actorProfile', params: {localId: actor.id} }">
        <img
          class="card-img" 
          :src="imgURL" 
          :alt="actor.name" 
          style="width:100%">
        <div class="w3-container w3-black">
          <h4>{{ actor.name }}</h4>
        </div>
      </router-link>
    </div> -->


    <router-link :to="{ name: 'actorProfile', params: {localId: actor.id} }">
      <div class="card" style="width: 18rem;">
        <img class="card-img-top card-img w3-grayscale" :src="imgURL" alt="Card image cap">
        <div class="card-body">
          <h5 class="card-title">{{ actor.name }}</h5>
        </div>
      </div>
    </router-link>
</template>

<script>
import drf from '@/api/drf'

export default {
  name: 'ActorCard',
  props: {
    actor: Object,
  },
  // data() {
  //   return {
  //     imageURL: '',
  //   }
  // },
  computed: {
    // ...mapGetters([]),
    IMG() {return "@/assets/images/noimage.png"},
    imgURL() {
      // return drf.url.img() + this.actor.profile_url
      const img = drf.url.img() + this.actor.profile_url
      if ( this.actor.profile_url ){ return img}
      else { return drf.url.noPhoto() }
    }
  },
  methods: {
    // ...mapActions(['fetchSearchResult']),
    // setSearchResult() {

    // },
  },
  created() {
    // this.setSearchResult()
  },
}
</script>

<style>
.card-img {
  width: 270px;
  height: 405px;
  object-fit: cover;
}
</style>