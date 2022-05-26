  <template>
  <div>
    <!-- <account-error-list v-if="authError"></account-error-list> -->

    <nav class="w3-bar w3-black w3-hide-small">
      <ul>
          <router-link :to="{ name: 'home' }" 
           class="w3-bar-item w3-button">Home</router-link>

          <!-- <router-link :to="{ name: 'login' }" v-if="!isLoggedIn"
           class="w3-bar-item w3-button">Login</router-link> -->

          <!-- <router-link :to="{ name: 'signup' }" v-if="!isLoggedIn" 
           class="w3-bar-item w3-button">Signup</router-link> -->
          
          <!-- 모달 로그인 버튼 -->
            <button v-if="!isLoggedIn"
            onclick="document.getElementById('loginbtn').style.display='block'" 
            class="w3-bar-item w3-button">
            Login
            </button>

          <!-- 모달 사인업 버튼 -->
            <button v-if="!isLoggedIn"
            onclick="document.getElementById('signupbtn').style.display='block'" 
            class="w3-bar-item w3-button">
            Signup
            </button>

          <router-link :to="{ name: 'userProfile', params: { username } }" v-if="isLoggedIn" 
           class="w3-bar-item w3-button">{{ currentUser.user_data.username }}'s page</router-link>

          <router-link :to="{ name: 'logout' }" v-if="isLoggedIn" 
           class="w3-bar-item w3-button">Logout</router-link>
        
        <!-- search input 만들어 -->
        <p class="w3-bar-item w3-right">
          <input @keyup.enter="search" @input="recomends" type="text" style="height: 25px; width: 220px">
          <!-- <i class="fa fa-search w3-button w3-righ" @click="search"></i> -->
          <router-link :key="$route.fullPath" :to="{ name: 'searchResult', params: { keyword } }"><i class="fa fa-search w3-button w3-righ"></i></router-link>
        </p>
      </ul>
    </nav>
    <!-- 자동완성 창 -->
    <div class="auto-parent">
      <a v-if="auto" class="auto w3-bar-item w3-white">
        <div 
          v-for="(reco, index) in recomend" 
          :key="index"
          class="auto-child"
        >
          <div @click="recosearch">{{reco}}</div>
        </div>
      </a>
    </div>

<!-- 로그아웃 모달 -->
      <div id="logout" class="w3-modal margin: 500px">
      <div class="w3-modal-content w3-animate-top" style="max-width:400px">
        <div class="w3-container w3-padding w3-black">
          <h4 class="w3-gray" style="display: inline; margin-left: 5px; margin-right: 10px; margin-top: 15px; border-radius: 4px; border: solid 2px grey; padding-right: 5px; padding-left: 5px;">Logout</h4>
          <span onclick="document.getElementById('logout').style.display='none'" 
          class="w3-button w3-display-topright">&times;</span>
        </div>
        <div class="w3-container w3-center w3-white">
          <div class="w3-container w3-center" style="margin: 10px">
            <br>
               <p><b>See you again!</b></p>     
          </div>
          <button class="w3-button w3-block w3-gray" style="width:70%; display: inline-block;" onclick="document.getElementById('logout').style.display='none'"><b>OK</b></button> 
          <br>
         <br>
        </div>
        </div>
      </div>
<!-- 로그아웃 모달 -->



  <!-- 로그인 모달 -->
      <div id="loginbtn" class="w3-modal margin: 500px">
      <div class="w3-modal-content" style="max-width:600px">
        <div class="w3-container w3-padding w3-black">
          <h4 class="w3-gray" style="display: inline; margin-left: 5px; margin-right: 10px; border-radius: 4px; border: solid 2px grey; padding-right: 5px; padding-left: 5px;">Login</h4>
          <h4 style="display: inline; padding-right: 5px; padding-left: 5px;"><button 
            onclick="document.getElementById('signupbtn').style.display='block'" 
            class="w3-black">
            <span onclick="document.getElementById('loginbtn').style.display='none'" >
            Signup
            </span>
            </button>
          </h4>
          <span onclick="document.getElementById('loginbtn').style.display='none'" 
          class="w3-button w3-display-topright">&times;</span>
        </div>
        <div class="w3-container w3-center w3-white">
          <br>
         <p><b>Find Your Movie</b></p>
          <form class="w3-container w3-center" @submit.prevent="login(credentials)">
            <div class="w3-container w3-center" style="margin: 10px">
              <input placeholder="username" style="width:70%; display: inline-block;" class="w3-input w3-border" v-model="credentials.username" type="text" id="username" required />
            </div>
            <div class="w3-container w3-center" style="margin: 10px">
              <input placeholder="password" style="width:70%; display: inline-block;" class="w3-input w3-border" v-model="credentials.password" type="password" id="password" required />
            </div>
            <br>
            <button class="w3-button w3-block w3-gray" style="width:70%; display: inline-block;" onclick="document.getElementById('loginbtn').style.display='none'"><b>Login</b></button>
          </form> 
          <br>
         <br>
        </div>
      </div>
      </div>
  <!-- 로그인 모달 끝 -->



<!-- 싸인업 모달 -->
      <div id="signupbtn" class="w3-modal margin: 500px">
      <div class="w3-modal-content" style="max-width:600px">
        <div class="w3-container w3-padding w3-black">
            <h4 style="display: inline; margin-right: 10px; padding-right: 5px; padding-left: 5px;"><button 
            onclick="document.getElementById('loginbtn').style.display='block'" 
            class="w3-black">
            <span onclick="document.getElementById('signupbtn').style.display='none'" >
            Login
            </span>
            </button>
          </h4>
          <h4 class="w3-gray" style="display: inline; border-radius: 4px; border: solid 2px grey; padding-right: 5px; padding-left: 5px;" >Signup</h4>
          <span onclick="document.getElementById('signupbtn').style.display='none'" 
          class="w3-button w3-display-topright">&times;</span>
        </div>
        <div class="w3-container w3-center w3-white">
          <br>
         <p><b>Find Your Movie</b></p>
          <form class="w3-container w3-center" @submit.prevent="signup(credentials)">
            <div class="w3-container w3-center" style="margin: 10px">
              <input placeholder="username" style="width:70%; display: inline-block;" class="w3-input w3-border" v-model="credentials.username" type="text" id="username" required />
            </div>
            <div class="w3-container w3-center" style="margin: 10px">
              <input placeholder="password" style="width:70%; display: inline-block;" class="w3-input w3-border" v-model="credentials.password1" type="password" id="password1" required />
            </div>
            <div class="w3-container w3-center" style="margin: 10px">
              <input placeholder="password check" style="width:70%; display: inline-block;" class="w3-input w3-border" v-model="credentials.password2" type="password" id="password2" required />
            </div>
            <br>
            <button class="w3-button w3-block w3-gray" style="width:70%; display: inline-block;" onclick="document.getElementById('signupbtn').style.display='none'"><b>Signup</b></button>
          </form> 
          <br>
         <br>
        </div>
      </div>
      </div>
<!-- 싸인업 모달 끝 -->



  </div>
</template>

<script>
  // import AccountErrorList from '@/components/AccountErrorList.vue'
  import { mapGetters, mapActions } from 'vuex'
  import router from '@/router'
  import axios from 'axios'
  import drf from '@/api/drf'

  export default {
    name: 'NavBar',
    components: {
      // AccountErrorList,
    },
    data() {
      return {
        keyword: '',
        recomend: [],
        auto: false,

        credentials: {
        username: '',
        password: '',
        password1: '',
        password2: '',
        }
      }
    },
    computed: {
      ...mapGetters(['isLoggedIn', 'currentUser', 'authHeader']),
      username() {
        return this.currentUser.username ? this.currentUser.username : 'guest'
      },
    },
    methods: {
      ...mapActions(['login', 'signup']),
      search() { router.push({ name: 'searchResult', params: { keyword: this.keyword } }) },
      recosearch(event) {
        router.push({ name: 'searchResult', key:"$route.fullPath", params: {  keyword: event.target.innerText } }) 
        },
      recomends(event) {
        this.keyword = event.target.value
        this.auto = false
        if (this.isLoggedIn){
          axios({
            url: drf.searche.search() + 'auto/',
            method: 'post',
            data: {keyword: this.keyword},
            headers: this.authHeader
          })
            .then(res => {
              this.recomend = res.data
            })
            .then(res => {
              console.log(res)
              this.auto = true
            })
            }
        else {
          axios({
            url: drf.searche.search() + 'auto/',
            method: 'post',
            data: {keyword: this.keyword},
          })
            .then(res => {
              this.recomend = res.data
            })
            .then(res => {
              console.log(res)
              this.auto = true
          })
        }
      }}}

</script>

<style>
  .w3-bar.w3-black.w3-hide-small .w3-bar-item.w3-button {
    display: inline-block;
    height: 40px;
  } 
  .w3-bar.w3-black.w3-hide-small .w3-bar-item.w3-right {
    height: 40px;
    padding-top: 6px;
    padding-right: 5px;
    margin: 0 0;
  }
  .w3-bar.w3-black.w3-hide-small .w3-bar-item.w3-right > i {
    position: relative;
    top: -2px;
  }
  .w3-bar.w3-black.w3-hide-small .fa {
    /* height: 30px; */
    margin: 0;
    /* padding-top: 6px; 
    margin: 0 0; */
  }
  .auto-parent {
    position: absolute; 
    top: 45px; right:20px; 
    height: 50px; width: 50px;
  }
  .auto {
    position: absolute; 
    top: -16px; left: -201px;
  }
  .auto > .auto-child:nth-child(1) {
    padding-top: 3px;
  }
  .auto-child {
    padding-left: 4px;
    padding-top: 1px;
    width: 220px;
  }
</style>