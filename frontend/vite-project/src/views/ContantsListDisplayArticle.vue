<script setup lang="ts">


import { useRoute } from 'vue-router';

import { useStore } from 'vuex';
import { computed } from 'vue';
import { ref, onMounted, watch } from 'vue';
import { reactive } from 'vue';


// import { VDataTable } from 'vuetify/labs/VDataTable'



const route = useRoute();
const store = useStore();



let VIDEOS = computed(() => { return store.getters.GET_VIDEOS; });
const PERFORMER_LIST = computed(() => { return store.getters.GET_PERFORMER_LIST; });
const TAG_LIST = computed(() => { return store.getters.GET_TAG_LIST; });
const MAKER_LIST = computed(() => { return store.getters.GET_MAKER_LIST; });
const LABEL_LIST = computed(() => { return store.getters.GET_LABEL_LIST; });
const SERIES_LIST = computed(() => { return store.getters.GET_SERIES_LIST; });
const KYOUNUKI_LIST = computed(() => { return store.getters.GET_KYOUNUKI_LIST; });
const VIDEOS_LOADED = computed(() => { return store.getters.GET_VIDEOS_LOADED; });
const URL_LIST = computed(() => { return store.getters.GET_URL_LIST; });
const URL_PARAM = computed(() => { return store.getters.GET_URL_PARAM; });
const URL_JUDGE_PARAM = computed(() => { return store.getters.GET_URL_JUDGE_PARAM; });
// const SUBCONTENTS = computed(() => { return store.getters.GET_SUBCONTENTS; });
const SUBCONTENTS_ALL = computed(() => { return store.getters.GET_SUBCONTENTS_ALL; });
const ARTICLE_LIST = computed(() => { return store.getters.GET_ARTICLE_LIST; });



store.dispatch('FETCH_GET_BREADCRUMBS')



let SUBCONTENTS = ref(route.path.split("/")[1])


let ARTICLE_LIST_DUP = ref()
watch(ARTICLE_LIST, (newVal, oldVal) => {
  if (SUBCONTENTS.value === "article" && newVal) {
    const uniqueTitles = [...new Set(newVal.map(item => item.title))];
    ARTICLE_LIST_DUP.value = uniqueTitles.map(title => {
      return newVal.find(item => item.title === title);
    });
    SUBCONTENTS_ALL.value = ARTICLE_LIST_DUP.value;

  //  SUBCONTENTS_CLASS_MAJOR.value = [...new Set(newVal.map(item => item.classmajor))];
  //  SUBCONTENTS_CLASS_MEDIUM.value = [...new Set(newVal.map(item => item.classmedium))];
  //  SUBCONTENTS_CLASS_MINOR.value = [...new Set(newVal.map(item => item.classminor))];
  }
})
if (SUBCONTENTS.value === "article" && ARTICLE_LIST.value) {
    const uniqueTitles = [...new Set(ARTICLE_LIST.value.map(item => item.title))];
    ARTICLE_LIST_DUP.value = uniqueTitles.map(title => {
      return ARTICLE_LIST.value.find(item => item.title === title);
    });
    SUBCONTENTS_ALL.value = ARTICLE_LIST_DUP.value;
  }



  



</script>


<script lang="ts">
import { defineComponent } from 'vue'
import GlobalStyles from '../components/_GlobalStyles.vue';
import { Icon } from '@iconify/vue';
import Text_1 from '../components/_Text_1.vue';



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
      showCheckboxes: true,
      items_tes: ['foo', 'bar', 'fizz', 'buzz'],
      value_tes: ['foo', 'bar', 'fizz', 'buzz'],
      selectedTags: [],
      amenities: [1, 4],
      neighborhoods: [1],
      search_view_performer: true,
      search_view_tag: true,


      // searchparams: {
      //   performers: null,
      //   tags: ["tag1"],
      //   maker: ["メーカー２"],
      //   label: null,
      //   series: null,
      //   duration: null,
      //   title: null,
      //   description: null,
      //   views: null,
      //   kyounuki_post_day: null,
      //   active: null,
      // },
      filteredData: [],
      media: [false,false,false,false,false,false,false,false,false,false],
      model: [0,0,0,0,0,0,0,0,0,0],
      currentImageIndex: 0,
      startX: 0,
      startIndex: 0,
      currentX: 0,
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
        { title: '【まとめ】〇〇賞についてまとめました！', src: 'https://cdn.vuetifyjs.com/images/cards/house.jpg', flex: 12 },
        { title: '【個人ブログ】好きな小説家について', src: 'https://cdn.vuetifyjs.com/images/cards/road.jpg', flex: 12 },
        { title: '【考察】今後の本の在り方について', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 12 },
        { title: '【まとめ】〇〇賞についてまとめました！', src: 'https://cdn.vuetifyjs.com/images/cards/house.jpg', flex: 12 },
    ],
    tab: null,
    }    
  },
  // watch: {
  //   'searchparams.tags': {
  //     handler: 'updateFilteredData',
  //     deep: true,
  //   },
  // },
  mounted() {
    // ビデオ要素の高さを設定
    this.setVideoHeight();
    // ウィンドウのリサイズ時にビデオの高さを再計算
    window.addEventListener("resize", this.setVideoHeight);
  },


  beforeUnmount() {
    window.removeEventListener("resize", this.setVideoHeight);
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
  setVideoHeight() {
      const video = this.$refs.videoRef;
      const toolbar = this.$el.querySelector(".control-bar");
      if (video && toolbar) {
        const videoHeight = video.getBoundingClientRect().height;
        toolbar.style.height = `${videoHeight}px`;
      }
  },

  }
});





</script>



<template>

      <v-row no-gutters class="my-bg-color-white">
        <!-- {{ filteredData }} -->
        <div>
          aaaa{{ ARTICLE_LIST_DUP }}

        </div>
        <v-col cols="12" class="mx-auto px-10">

        <v-container fluid>

      <v-row dense>
        <v-col
          v-for="card in ARTICLE_LIST_DUP"
          :key="card.title"
          cols="12"
          class="py-3"

        >
        <v-card class="">
        <p class="pl-5 my-font-size-20 my-fit-contents my-text-size-30 mt-0 my-bg-color my-text-color-white">2022-04-02</p>

          <v-card
            aria-disabled
            
            class="rounded-0"
            :to="{ name: 'Article', params: { param: card.classmajor, param2: card.classmedium, param3: card.classminor, param4: card.number} }"
          >


      
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


                      <v-col cols="12" class="d-flex"
                      >

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










                    
              <v-card-title class="text-white text-h3" style="white-space: pre-wrap;" v-text="card.title"></v-card-title>
            </v-img>

              <!-- <v-card-actions>
                <v-spacer></v-spacer>

              <v-btn
                color="var(--my-color-green)"
                class="ms-auto px-6"
                size="x-large"
                variant="outlined"
                prepend-icon=""http://172.20.10.4:5173/article/matome/performer/amature/1
                append-icon="mdi-account-circle"

                >
                この記事を読む...
                <template v-slot:prepend>
                  <v-icon color="orange"></v-icon>
                </template>
              </v-btn>
            </v-card-actions> -->
          </v-card>
        </v-card>

        </v-col>
      </v-row>
    </v-container>
















        <Btn_1 text="もっとみる"/>


      </v-col>
    </v-row>














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

.custom-chip-style {
  /* ここに独自のスタイルを追加 */
  /* font-size: 40px; */
  /* 他のスタイルプロパティを追加 */
  height: fit-content!important;
  font-size: 30px!important;


  
}
</style>
