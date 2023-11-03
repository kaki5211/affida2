
<script setup>




// ■Component


// ■■■■■■ import > Packages ■■■■■■
import { computed } from 'vue';
// import { onMounted } from 'vue';
import { watch } from 'vue';
import { ref } from 'vue';
// import { reactive } from 'vue';
import { useStore } from 'vuex';
import { useRoute } from 'vue-router';



// ■■■■■■ import > Others ■■■■■■
// import { Icon } from '@iconify/vue';




// ■■■■■■ import > Components ■■■■■■
import Btn_1 from '../components/_Btn_1_mottomiru.vue';
import Text_1 from '../components/_Text_1.vue';
// import HelloWorld from './components/HelloWorld.vue'
// import Meta from './components/Meta.vue';
// import ToolBar from './components/ToolBar.vue';
// import Topimage from './components/Topimage.vue';
// import Footer from './components/Footer.vue';
// import Breadcrumbs from './components/Breadcrumbs.vue';






// ■■■■■■ VueStore ■■■■■■
const store = useStore();
const VIDEOS = computed(() => { return store.getters.GET_VIDEOS; });
const PERFORMER_LIST = computed(() => { return store.getters.GET_PERFORMER_LIST; });
const TAG_LIST = computed(() => { return store.getters.GET_TAG_LIST; });
// const MAKER_LIST = computed(() => { return store.getters.GET_MAKER_LIST; });
// const LABEL_LIST = computed(() => { return store.getters.GET_LABEL_LIST; });
// const SERIES_LIST = computed(() => { return store.getters.GET_SERIES_LIST; });
// const KYOUNUKI_LIST = computed(() => { return store.getters.GET_KYOUNUKI_LIST; });
const VIDEOS_LOADED = computed(() => { return store.getters.GET_VIDEOS_LOADED; });
// const URL_LIST = computed(() => { return store.getters.GET_URL_LIST; });
// const URL_PARAM = computed(() => { return store.getters.GET_URL_PARAM; });
// const URL_JUDGE_PARAM = computed(() => { return store.getters.GET_URL_JUDGE_PARAM; });
// const SUBCONTENTS = computed(() => { return store.getters.GET_SUBCONTENTS; });
// const SUBCONTENTS_ALL = computed(() => { return store.getters.GET_SUBCONTENTS_ALL; });
const DEBUG = computed(() => { return store.getters.GET_DEBUG; });
const ARTICLE_LIST = computed(() => { return store.getters.GET_ARTICLE_LIST; });


// let slicedKYOUNUKI_LIST = ref("");
// if (KYOUNUKI_LIST.length > 2) {
//   slicedKYOUNUKI_LIST = KYOUNUKI_LIST.slice(0, 2);
// } else {
//   slicedKYOUNUKI_LIST = KYOUNUKI_LIST;
// }

// store.dispatch('FETCH_GET_BREADCRUMBS')



// ■■■■■■ VueRouter ■■■■■■
const route = useRoute();

const slicedVideos = ref([{performers:[], tags: [], images: []}]);
watch(VIDEOS, (newVal, oldVal) => {
  try {
    if (newVal) {
      slicedVideos.value = newVal.slice(0, 4);
    }
  } catch (error) {
    console.error("An error occurred in the watcher callback:", error);
  }})
if (VIDEOS.value) {
  slicedVideos.value = VIDEOS.value.slice(0,4)
}


// console.log("DEBUG", DEBUG.value)
// store.dispatch('FETCH_GET_BREADCRUMBS')
// console.log("route.path ", route.path )



const text1 = ref("アカウント");
const text2 = ref("記事１");
const text3 = ref("記事２");

if (DEBUG.value == true) {
  text1.value = "アカウント";
  text2.value = "記事１";
  text3.value = "記事２";

}



// ■ARTICLE_LIST　＞　ARTICLE_LIST_DUP
let ARTICLE_LIST_DUP = ref()
watch(ARTICLE_LIST, (newVal, oldVal) => {
  if (newVal) {
    const uniqueTitles = [...new Set(newVal.map(item => item.title))];
    ARTICLE_LIST_DUP.value = uniqueTitles.map(title => {
      return newVal.find(item => item.title === title);
    });
    // SUBCONTENTS_ALL.value = ARTICLE_LIST_DUP.value;

  //  SUBCONTENTS_CLASS_MAJOR.value = [...new Set(newVal.map(item => item.classmajor))];
  //  SUBCONTENTS_CLASS_MEDIUM.value = [...new Set(newVal.map(item => item.classmedium))];
  //  SUBCONTENTS_CLASS_MINOR.value = [...new Set(newVal.map(item => item.classminor))];
  }
})
if (ARTICLE_LIST.value) {
    const uniqueTitles = [...new Set(ARTICLE_LIST.value.map(item => item.title))];
    ARTICLE_LIST_DUP.value = uniqueTitles.map(title => {
      return ARTICLE_LIST.value.find(item => item.title === title);
    });
    // SUBCONTENTS_ALL.value = ARTICLE_LIST_DUP.value;
  }





const path_ = route
console.log("path_", path_)
console.log("route.path", route.path);






</script>

<script>
import { defineComponent } from 'vue'
import GlobalStyles from '../components/_GlobalStyles.vue';


export default defineComponent({
  name: 'App',
  components: {
    GlobalStyles,
		// Icon,
    Text_1,
    // VideoPlayer,
  },
  data () {
    return {
      media: [false,false,false,false,false,false,false,false,false,false],
      model: [0,0,0,0,0,0,0,0,0,0],
      currentImageIndex: 0,
      startX: 0,
      startIndex: 0,
      currentX: 0,
      search_view_performer: true,
      search_view_tag: true,

      playerOptions: {
        autoplay: false, // 自動再生
        controls: true, // コントロール表示
        sources: [
          {
            src: 'http://www.youtube.com/embed/cvj3-MZO9T', // 動画のURL
            // type: 'video/mp4', // 動画の形式
          },
        ],
      },
      items: [
        {
          src: 'https://cdn.vuetifyjs.com/images/carousel/squirrel.jpg',
        },
        {
          src: 'https://cdn.vuetifyjs.com/images/carousel/sky.jpg',
        },
        {
          src: 'https://cdn.vuetifyjs.com/images/carousel/bird.jpg',
        },
        {
          src: 'https://cdn.vuetifyjs.com/images/carousel/planet.jpg',
        },
      ],
      cards: [
      { title: '【〇〇まとめ】厳選〇〇', src: 'https://cdn.vuetifyjs.com/images/cards/house.jpg', flex: 12 },
      { title: '【雑記】〇〇について', src: 'https://cdn.vuetifyjs.com/images/cards/road.jpg', flex: 12 },
      { title: '【〇〇まとめ】厳選〇〇', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 12 },
      { title: '【雑記】〇〇について', src: 'https://cdn.vuetifyjs.com/images/cards/house.jpg', flex: 12 },
    ],
    tab: null,

    }    
  },
  methods: {
  parseJson(value) {
    if (value.length != 0) {
    return JSON.parse(value.replace(/'/g, '"'));
  }
  },
  playVideo() {
      const videoPlayer = this.$refs.videoPlayer;
      videoPlayer.play();
  },

  handleTouchStart(event, i, Index) {
    this.startX = event.touches[0].clientX;
    this.startIndex = this.model[i];
  },
  toggleMedia(index) {
    this.media.splice(index, 1, !this.media[index]); // spliceメソッドを使って要素を置換する
  },
  // handleTouchMove(event, i, images) {
  //   const touch = event.touches[0];
  //   const distance = touch.clientX - this.startX;
  //   let changeindex = 0;
  //   changeindex = parseInt(distance / 100, 10);

  //   this.model[i] = (this.startIndex + changeindex + (images * 50)) % images
  //   console.log(this.model[i])
  // },

  // handleTouchMove2(event) {
  //     const touch = event.touches[0];
  //     const distance = touch.clientX - this.startX;

  //     // スワイプ距離とナビゲーションの座標を比較し、一致する座標を見つける
  //     const matchIndex = Math.round(distance / NAVIGATION_WIDTH); // ナビゲーションの幅に合わせて調整

  //     // 一致した座標に対応するインデックスを計算し、表示画像を更新する
  //     this.model = matchIndex;
  //   },  
}

});



</script>









<template>

  <v-app id="#my-scroll-target">


    <!-- <v-main v-if="isUrlListDataLoaded" class="my-bg-color-white"> -->
    <v-main v-if="VIDEOS_LOADED" class="my-bg-color-white">
      <!-- <dev>{{ VIDEOS }}</dev> -->
      <!-- <dev>{{ URL_LIST }}</dev>
      <dev>{{ currentPath }}</dev>
      <dev>{{ pathList }}</dev> -->

      







      this.$router.currentRoute.pat:{{this.$router.currentRoute.path}}






    <v-row justify="space-around" aria-disabled no-gutters>
    <Text_1 :text_1="text3 || 'ブログ記事'" />
      <v-col cols="11" class="mx-auto">
        <v-row dense class="my-bg-color-white" >
          <v-col
            v-for="card in ARTICLE_LIST_DUP"
            :key="card.title"
            cols="12"
            class="my-bg-color-white my-5 pb-0"
          >
          <v-hover>
            <template v-slot:default="{ isHovering, props }">
              <v-card
                v-bind="props"
                :elevation="isHovering ? 16 : 2"
                class="pb-0"
                rounded="lg"
                :to="{ name: 'Article', params: { param: card.classmajor, param2: card.classmedium, param3: card.classminor, param4: card.number} }"
              >
                <p class="pl-5 my-font-size-20 my-fit-contents my-text-size-30 mt-0 my-bg-color my-text-color-white">
                  2022-04-02
                </p>
              <v-img
                src="https://cdn.vuetifyjs.com/images/carousel/sky.jpg"
                class="align-end"
                gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
                height="200px"
                cover
              >
                <!-- <v-row v-if="ii==0" no-gutters> -->
                <v-row no-gutters>
                  <!-- v-for="(item,i) in VIDEO.performers" -->
                  <!-- :key="i" -->
                  <v-col cols="12" class="d-flex">
                  <!-- :prepend-icon="i === 0 ? 'mdi-account-circle' : ''" -->
                    <v-btn 
                      rounded="0"
                      class="my-fit-contents my-text-size-30  ms-auto me-0"
                      style="position: absolute; top: 5px; right: 10px;"
                    >
                      <!-- {{ card.classminor }} -->
                      タグ
                    </v-btn>
                  </v-col>
                </v-row>
                <v-card-title class="text-white text-h3" style="white-space: pre-wrap;" v-text="card.title">
                </v-card-title>
                </v-img>
              </v-card>
            </template>
            </v-hover>
          </v-col>
        </v-row>
        <Btn_1 text="もっとみる" href="Articles"/>
      </v-col>
    </v-row>







      <v-row no-gutters class="my-bg-color-white">
        <Text_1 :text_1="text2 || 'aaaa'" />
        <v-col cols="12" class="mx-auto px-10">


          <!-- 動画 -->
          <v-card v-if="slicedVideos" class="my-15">
            <v-toolbar
                flat
                dark
                class="my-bg-color"
              >
                <v-toolbar-title class="my-text-color-white font-weight-medium my-text-size-40">動画</v-toolbar-title>
              </v-toolbar>
              <v-row no-gutters>
                <v-col cols="6" class="mx-auto px-6 py-15 pb-5"
                  v-for="(VIDEO,i) in slicedVideos"
                  :key="i"
                  :src="VIDEO"
                >
                  <v-carousel
                  class="my-carousel"
                  v-if="media[i]==false"
                   :show-arrows="false"
                   :cycle="false"
                   v-model="model[i]"
                    @touchstart="handleTouchStart($event, i, model[i])"
                  >
                  <!-- @touchmove="handleTouchMove($event, i, parseJson(VIDEO.images).length)" -->

                    <v-carousel-item
                      v-for="(item,ii) in parseJson(VIDEO.images)"
                      :key="ii"
                      cover
                      aspect-ratio="" :src="item" alt="Image" @click="model[i] = (model[i] + 1 ) % parseJson(VIDEO.images).length"
                      class="d-flex justify-end"
                    >
                    <v-row v-if="ii==0" no-gutters>
                      <v-col cols="12" class="d-flex"
                      v-for="(item,i) in VIDEO.performers"
                          :key="i"
                      >
                        <v-btn 
                          rounded="0"
                          class="my-fit-contents my-text-size-30  ms-auto me-0"
                          :prepend-icon="i === 0 ? 'mdi-account-circle' : ''"
                          >
                          {{item.name}}
                        </v-btn>
                      </v-col>
                    </v-row>
                    <v-row v-if="ii==1" no-gutters>
                      <v-col cols="12" class="d-flex"
                      v-for="(item,i) in VIDEO.tags"
                          :key="i"
                      >
                        <v-btn 
                          rounded="0"
                          class="my-fit-contents my-text-size-30  ms-auto me-0 "
                          style="white-space: nowrap; overflow-x: auto"
                          :prepend-icon="i === 0 ? 'mdi-tag-text-outline' : ''"
                          >
                          {{item.name}}
                        </v-btn>
                      </v-col>
                    </v-row>

                    <!-- <v-img aspect-ratio="0.73" :src="item" alt="Image" @click="model[i] = (model[i] + 1 ) % parseJson(VIDEO.images).length"></v-img> -->

                  </v-carousel-item>
                  </v-carousel>
                  <v-row no-gutters v-if="media[i]==true">
                    <v-col cols="12" aspect-ratio="0.73" class="mx-auto px-0 my-auto">

                        <video controls class="w-100 my-auto px-0 my-auto" playsinline autoplay muted>
                          <source src="https://liginc.co.jp/wp-content/uploads/2020/05/D0002060347_00000_V_000.mp4?_=1" type="video/mp4">
                          Your browser does not support the video tag.
                        </video>
                    </v-col>
                        <v-col cols="12" class="d-flex pb-0 w-100">
                          <v-btn class="me-0 ms-auto my-font-size-20 my-fit-contents my-text-size-40 w-100" append-icon="mdi-play-circle-outline" @click="toggleMedia(i)">
                            閉じる
                          </v-btn> 
                        </v-col>
                  </v-row>


                  

                  <v-row no-gutters v-if="media[i]==false">
                    <v-col class="d-flex pb-0 w-100">
                      <v-btn class="me-0 ms-auto my-font-size-20 my-fit-contents my-text-size-40 w-100" append-icon="mdi-play-circle-outline" @click="toggleMedia(i)">
                        再生
                      </v-btn> 
                    </v-col>
                  </v-row>

                  <p
                    class="my-text-size-50 font-weight-midium pt-2"
                    style="white-space: nowrap; overflow-x: auto"
                  >
                    {{VIDEO.title}}
                  </p>


                </v-col>
              </v-row>
            </v-card>












        <Btn_1 text="もっとみる" href="Videos" />


      </v-col>
    </v-row>



    

    



<v-row no-gutters>
  <Text_1 text_1="ランキング(準備中...)" />
  <v-col cols="12" class="mx-auto px-5 pb-10 mb-10">
    <v-card class=""
      disabled
    >
      
        <v-tabs
          v-model="tab"
          color="var(--my-color-white)"
          align-tabs="center"
          class="my-bg-color mb-10"
        >
        
          <v-tab :value="1" class="text-h3 font-weight-bold">月間</v-tab>
          <v-tab value="98" disabled class="text-h3 font-weight-bold">/</v-tab>

          <v-tab :value="2" class="text-h3 font-weight-bold">週間</v-tab>
          <v-tab value="99" disabled class="text-h3 font-weight-bold">/</v-tab>

          <v-tab :value="3" class="text-h3 font-weight-bold">今日</v-tab>
        </v-tabs>
        <v-window v-model="tab" class="pt-10 ">
          <v-window-item
            v-for="n in 3"
            :key="n"
            :value="n"
          >
            <v-container fluid>
              <v-row>
                <v-col
                  v-for="i in 6"
                  :key="i"
                  cols="4"
                  md="4"
                >
                <div class="d-flex">
                <p class="mx-auto my-text-size-50 pa-5 pb-2">{{ i }}</p>
                </div>
                  <v-img
                    class="pa-8"
                    src="https://picsum.photos/200/300"
                    :lazy-src="`https://picsum.photos/10/6?image=${i * n * 5 + 10}`"
                    aspect-ratio="0.73"
                  ></v-img>
                  <p class="mx-auto my-text-size-50 pa-7">TITLE</p>
                </v-col>
              </v-row>
            </v-container>
          </v-window-item>
        </v-window>
      </v-card>
    </v-col>
  </v-row>
  <!-- <Btn_1 text="もっとみる" href="" /> -->


  <!-- :src="`https://picsum.photos/500/300?image=${i * n * 5 + 10}`" -->






  <v-row no-gutters>
  <Text_1 text_1="アカウント・タグ 一覧" />
    <v-col cols="11" class="mx-auto px-5">






                    <!-- アカウント -->
                    <v-card height="" class="my-bg-color-white mb-5">
                  <v-row no-gutters>
                      <v-col cols="12" class="border">
                          <v-btn large outlined tile block class="my-text-color my-text-size-40 font-weight-medium rounded-tl-lg"
                          height="50px" @click="search_view_performer=!search_view_performer"><v-icon>mdi-account-circle</v-icon>アカウント</v-btn>
                            <v-row v-if="search_view_performer" no-gutters class="my-auto">
                              <v-col cols="12" class="border px-2 py-5 pb-10">
                                <v-chip-group
                                  v-model="PERFORMER_LIST"
                                  column
                                  multiple
                                  color="text-deep-purple-accent-4"
                                >
                                    <v-chip
                                    v-for="item in PERFORMER_LIST"
                                    :key="item.id"
                                    label
                                    outline
                                    :value="item.name"
                                    color="red"
                                    :to="{ name: 'Videos', query: { 'searchrequest': JSON.stringify([{'performers':item.name}])}}"


                                    class="custom-chip-style mx-0 mb-1 mt-0 elevation-1"

                                  >

                                      {{ item.name }}
                                    </v-chip>
                                  </v-chip-group>
                                  <!-- {{searchparams.performers}} -->

                                  
                              </v-col>
                              
                            </v-row>
                        </v-col>
                      </v-row>
                    </v-card>




                    <!-- タグ -->
                    <v-card height="" class="my-bg-color-white" elevation=0>
                      <v-row no-gutters>
                        <v-col cols="12" class="border">
                          <v-btn large outlined tile block class="my-text-color my-text-size-40 font-weight-medium rounded-tl-lg"
                          height="50px" @click="search_view_tag=!search_view_tag"><v-icon>mdi-tag-text-outline</v-icon>タグ</v-btn>
                            <v-row v-if="search_view_tag" no-gutters class="my-auto">
                              <v-col cols="12" class="border px-2 py-5 pb-10">
                                  <v-chip-group
                                    v-model="TAG_LIST"
                                    column
                                    multiple

                                  >
                                      <v-chip
                                      v-for="item in TAG_LIST"
                                      :key="item.id"
                                      label
                                      outline
                                      :value="item.name"
                                      color="red"
                                      :to="{ name: 'Videos', query: { 'searchrequest': JSON.stringify([{'tags':item.name}])}}"
                                      class="custom-chip-style mx-0 mb-1 mt-0 elevation-1"

                                    >
                                      {{ item.name }}
                                    </v-chip>
                                  </v-chip-group>
                                  <!-- {{searchparams.tags}} -->

                                  <div class="d-flex py-3">
                                  </div>
                              </v-col>
                            </v-row>
                        </v-col>
                      </v-row>
                    </v-card>

      
<!-- 
      <v-card height="" class="my-bg-color-white mt-15" elevation=0>
        <v-row no-gutters>
          <v-col cols="12" class="border">
              <v-btn large outlined tile block disabled class="my-text-color my-text-size-40 font-weight-medium rounded-tl-lg" height="200px" href=""><v-icon>mdi-magnify</v-icon>詳細検索（準備中...）</v-btn>
          </v-col>
        </v-row>
      </v-card> -->


    </v-col>
  </v-row>

  <v-col cols="12" class="my-15"></v-col>










  

















































  <!-- <v-container>
    <Text_1 text_1="SNS" />
    <v-row class="text-center mt-10 mx-auto"> 
        <v-col cols="5" class="mx-auto">
          <a href="">
            <v-icon class="my-3" contain size="200px" color="#1DA1F2">mdi-twitter</v-icon>
          </a>
        </v-col>
        <v-col cols="5" class="mx-auto">
          <a href="">
            <v-icon class="my-3" contain size="200px"><Icon icon="skill-icons:instagram" /></v-icon>
          </a>
        </v-col>

      </v-row>
      <v-row class="text-center">


      <v-col cols="5" class="mb-4 mx-auto">
        <a class="text-h3 font-weight-bold mb-3">
          Twitter
        </a>

      </v-col>
      <v-col cols="5" class="mb-4 mx-auto">
        <h1 class="text-h3 font-weight-bold mb-3">
          Instagram
        </h1>

      </v-col>

    </v-row>
  </v-container> -->











    </v-main>








    <div v-else>
        データを読み込んでいます...
    </div>







  </v-app>
</template>



<style>


</style>
