<router-link :to="{ name: 'directorProfile', params: {localId: directorInfo.id} }">
      <img :src="imgURL" :alt="directorInfo.name">
      <p>{{ directorInfo.name }}</p>
      감독에 대한 나의 레벨
      <p>{{ directorLevel }}</p>
      <!-- 추천 -->
      <!-- <movie-card :movie="recomendMovie"></movie-card> -->
 <router-link :to="{ name: 'directorProfile', params: {localId: directorInfo.id} }">
   </router-link>  