<script setup lang="ts">


import { useRoute } from 'vue-router';

import { useStore } from 'vuex';
import { computed } from 'vue';
import { ref, onMounted, watch } from 'vue';
import { Icon } from '@iconify/vue';

import Text_1 from '../components/_Text_1.vue';


import Breadcrumbs from '../components/Breadcrumbs.vue';



// import { VideoPlayer } from '@videojs-player/vue'
// import 'video.js/dist/video-js.css'




const route = useRoute();
const store = useStore();

const VIDEOS = computed(() => { return store.getters.GET_VIDEOS; });
const PERFORMER_LIST = computed(() => { return store.getters.GET_PERFORMER_LIST; });
const TAG_LIST = computed(() => { return store.getters.GET_TAG_LIST; });
const KYOUNUKI_LIST = computed(() => { return store.getters.GET_KYOUNUKI_LIST; });
let VIDEOS_LOADED = computed(() => { return store.getters.GET_VIDEOS_LOADED; });
const URL_LIST = computed(() => { return store.getters.GET_URL_LIST; });

const urlPath = window.location.pathname;
const pathList = urlPath.split("/");
const lastpath = pathList[pathList.length - 1];




let SUBCONTENTS = ref(route.path.split("/")[1]+"s")


let SUBCONTENTS_ALL = ref()






if (SUBCONTENTS.value === "performers") {
  SUBCONTENTS_ALL.value = PERFORMER_LIST;
} else if (SUBCONTENTS.value === "tags") {
  SUBCONTENTS_ALL.value = TAG_LIST;
} else if (SUBCONTENTS.value === "videos") {
  SUBCONTENTS_ALL.value = VIDEOS;
}








const productNumbers = computed(() => {
  // URL_LISTの値が変更されたときに処理を実行する
  const newValue = URL_LIST.value;

  // ここでnewValueを使用して必要な処理を実行する
  const productNumbers = newValue.video.map(video => video.productnumber)
  
  return productNumbers;
});


const judgeurl = computed(() => {
  const newValue = productNumbers.value;
  const lastpathin = lastpath;

  // newValueの中にlastpathと一致する要素があるかどうかを判定
  const hasMatch = newValue.includes(lastpathin);
  
  return hasMatch;
});


const VIDEO_DETAIL = computed(() => {
  const newValue = judgeurl.value;
  const newVIDEOS = VIDEOS.value
  const videoMatch = newVIDEOS.filter((video) => video.productnumber === lastpath);
  return videoMatch
});



const iii = ref(0)
</script>


<script lang="ts">
import { defineComponent } from 'vue'
import GlobalStyles from '../components/_GlobalStyles.vue';


export default defineComponent({
  name: 'App',
  components: {
    GlobalStyles,
		Icon,
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
    return JSON.parse(value.replace(/'/g, '"'));
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
}

});



</script>

<template>
  <!-- <v-app id="#my-scroll-target" v-if="judgeurl" class="my-bg-color"> -->

    <v-container fluid>
    <v-row justify="space-around" no-gutters>
      <v-col class="py-1" cols="12">


            <v-row no-gutters class="my-bg-color-white">
        <!-- <Text_1 :text_1="text2 || '今日抜き'" /> -->

        
        <v-col cols="12" class="mx-auto px-10">

          <v-card class="my-15"

          >
          <v-toolbar
                flat
                dark
                class="my-bg-color"
              >
                <!-- <v-toolbar-title class="my-text-color-white font-weight-medium text-center my-text-size-40">{{ KYOUNUKI.post_day}}</v-toolbar-title> -->
              </v-toolbar>
            <!-- <v-card-text tag="h3" class="mt-6 my-underline text-center px-5 my-text-size-40 font-weight-medium">{{ KYOUNUKI.post_day}}</v-card-text> -->

            
              <v-row no-gutters>

                <v-col cols="11" class="mx-auto px-6 py-15 pb-5"
                  v-for="(VIDEO,i) in VIDEO_DETAIL"
                  :key="i"
                  :src="VIDEO"
                >

                  <v-carousel
                  class="my-carousel"
                  v-if="media[(i)+iii*4]==false"
                   :show-arrows="false"
                   :cycle="false"
                   v-model="model[(i)+iii*4]"
                    @touchstart="handleTouchStart($event, (i)+iii*4, model[(i)+iii*4])"



                  >
                  <!-- @touchmove="handleTouchMove($event, i, parseJson(VIDEO.images).length)" -->

                    <v-carousel-item
                      v-for="(item,ii) in parseJson(VIDEO.images)"
                      :key="ii"
                      cover
                      aspect-ratio="1.46" :src="item" alt="Image" @click="model[(i)+iii*4] = (model[(i)+iii*4] + 1 ) % parseJson(VIDEO.images).length"
                      
                      
                      
                    >
                    <!-- <v-row v-if="ii==0" no-gutters>
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
                    </v-row> -->
                    <!-- <v-img aspect-ratio="0.73" :src="item" alt="Image" @click="model[i] = (model[i] + 1 ) % parseJson(VIDEO.images).length"></v-img> -->

                  </v-carousel-item>
                  </v-carousel>
                  <v-row no-gutters v-if="media[(i)+iii*4]==true">
                    <v-col cols="12" aspect-ratio="1.46" class="mx-auto px-0 my-auto">

                        <video controls class="w-100 my-auto px-0 my-auto" playsinline autoplay muted>
                          <source src="https://liginc.co.jp/wp-content/uploads/2020/05/D0002060347_00000_V_000.mp4?_=1" type="video/mp4">
                          Your browser does not support the video tag.
                        </video>
                    </v-col>


                        
                        <v-col cols="12" class="d-flex pb-0 w-100">
                          <v-btn class="me-0 ms-auto my-font-size-20 my-fit-contents my-text-size-40 w-100" append-icon="mdi-play-circle-outline" @click="toggleMedia((i)+iii*4)">
                            閉じる
                          </v-btn> 
                        </v-col>

                  </v-row>


                  <!--
                  <div v-if="media[i]==true" class="video-container">
                    <video ref="videoRef" class="video-player" controls playsinline autoplay muted>
                      <source src="src/assets/mov_hts-samp007.mp4" type="video/mp4">
                      Your browser does not support the video tag.
                    </video>

                    <v-toolbar class="control-bar" absolute bottom>
                      コントロールバーのコンポーネントをここに追加
                      <v-btn icon>
                        <v-icon>mdi-play-pause</v-icon>
                      </v-btn>
                      <v-slider thumb-label="always"></v-slider>
                      追加のコントロールボタンやスライダーなどを配置
                    </v-toolbar>
                  </div>
                  -->


                <!-- <div v-if="media[i]==true" aspect-ratio="0.73" class="mx-auto px-0 my-auto d-flex">
                  <div class="video-wrapper">
                    <video ref="videoPlayer" :class="['video-player', { 'small': isSmall }]" playsinline autoplay muted>
                      <source src="src/assets/mov_hts-samp007.mp4" type="video/mp4">
                      Your browser does not support the video tag.
                    </video>
                    <div class="custom-controls">
                      <div class="progress-bar" @mousedown="startDrag">
                        <div class="progress" :style="{ width: progressWidth }"></div>
                      </div>
                    </div>
                  </div>
                  </div> -->


                  <!-- videoSrc -->
                  

                  <v-row no-gutters v-if="media[(i)+iii*4]==false">
                    <v-col class="d-flex pb-0 w-100">
                      <v-btn class="me-0 ms-auto my-font-size-20 my-fit-contents my-text-size-40 w-100" append-icon="mdi-play-circle-outline" @click="toggleMedia((i)+iii*4)">
                        再生
                      </v-btn> 
                    </v-col>
                  </v-row>

                    <!-- <v-row no-gutters>
                    <v-col class="d-flex mt-1 w-100">
                      <v-btn class="me-0 ms-auto my-font-size-20 my-fit-contents my-text-size-40 w-100" append-icon="mdi-open-in-new">
                        続きを見る
                      </v-btn> 
                    </v-col>
                  </v-row> -->

                  <a :to="{ name: 'Video', param: VIDEO.productnumber}" class="custom-link my-text-size-50 font-weight-medium pt-2">{{ VIDEO.title }}</a>


                  <v-row no-gutters>
                    <v-col class="d-flex">
                      <v-btn 
                        v-for="(item,i) in VIDEO.performers"
                        :key="i"
                        class="my-fit-contents my-text-size-30 py-1 my-1"
                        :prepend-icon="i === 0 ? 'mdi-account-circle' : ''"
                        >
                        {{item.name}}
                      </v-btn>
                    </v-col>
                  </v-row>

                  <v-row no-gutters>
                    <v-col class="d-flex">
                      <v-btn 
                        v-for="(item,i) in VIDEO.tags"
                        :key="i"
                        class="my-fit-contents my-text-size-30 py-1 my-1"
                        :prepend-icon="i === 0 ? 'mdi-tag-text-outline' : ''"
                        >
                        {{item.name}}
                      </v-btn>
                    </v-col>
                  </v-row>









            <!-- <v-card-title class="py-5 text-h3 font-weight-bold my-text-color-black my-letter-spacing-initial" tag="h3">
              コンビニ人間            
            </v-card-title> -->




            

            <v-row v-if="true" no-gutters>
              <v-col cols="8" class="mx-auto mt-15 mb-10">
                <List_1 />
              </v-col>
            </v-row>




            <Text_2 text_2="あらすじ" />
            

            <v-card-text class="psy-3 my-text-color">
              <a class="text-h5 font-weight-medium my-text-contents">
                {{contents_synopsis}}
              </a>
            </v-card-text>

            <v-row no-gutters>
              <v-col class="d-flex">
                <v-btn 
                  v-for="(item,i) in VIDEO.performers"
                  :key="i"
                  class="my-fit-contents py-1 my-1 mx-auto"
                  >
                  <v-icon size="50">mdi-open-in-new</v-icon> <!-- アイコンのサイズを設定 -->
                  <span class="my-text-size-50">外部サイト</span> <!-- テキストのサイズを設定 -->                </v-btn>
              </v-col>
            </v-row>

          </v-col>
        </v-row>
      </v-card>







    </v-col>
  </v-row>



















          </v-col>




    </v-row>
  </v-container>
</template>





<style scoped>

.video-container {
  position: relative;
  width: 100%;
}
.video-player {
  width: 100%;
}
.control-bar {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: rgba(0, 0, 0, 0.5);
  color: white;
}
</style>
