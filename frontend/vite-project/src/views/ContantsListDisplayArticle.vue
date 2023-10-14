<script setup lang="ts">


import { useRoute } from 'vue-router';

import { useStore } from 'vuex';
import { computed } from 'vue';
import { ref, onMounted } from 'vue';
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
const SUBCONTENTS = computed(() => { return store.getters.GET_SUBCONTENTS; });
const SUBCONTENTS_ALL = computed(() => { return store.getters.GET_SUBCONTENTS_ALL; });

store.dispatch('FETCH_GET_BREADCRUMBS')
const searchparams = reactive({
  performers: [],
  tags: [],
  maker: [],
  label: [],
  series: [],
  duration: [],
  title: [],
  description: [],
  views: [],
  kyounuki_post_day: [],
  active: [],
})





try {
  // const searchrequest = route.query.searchrequest;
  var searchrequest = JSON.parse(route.query.searchrequest);
  console.log("searchparams", searchparams.value)
  console.log("searchrequest", searchrequest)

  if (Array.isArray(searchrequest)) {
    console.log("■point1")
    searchrequest.forEach(item => {
      console.log("■point2")

      for (const key in item) {
        console.log("■point3")

        searchparams[key] = [item[key]];
      }
    });
  }
} catch (error) {
  // エラーが発生した場合は何もしない
}
console.log("route.params.serchrequest", route.query.searchrequest)
console.log("searchparams", searchparams.value)


function toggleTag(tagName, searchparams) {
      console.log("tagName", tagName)
      console.log("searchparams.value.tags", searchparams)
      console.log("searchparams.value.tags", searchparams.tags)
      if (searchparams.tags.includes(tagName)) {
        searchparams.tags = searchparams.tags.filter(tag => tag !== tagName);
      } else {
        searchparams.tags.push(tagName);
      }
    }




// const test = SUBCONTENT  S_ALL.value === searchparams.value.tags

// console.log("SUBCONTENTS_ALL.value.tags", VIDEOS.value[0].tags[0].name)
// console.log("searchparams.value.tags", searchparams.value.tags)
// console.log("■■■■test", test)
// 
function filterVideo(data, searchparams) {
  let filteredData = data; // オリジナルのデータを変更せずにコピーを作成

  for (let key in searchparams) {
    const filterValue = searchparams[key];

    if (filterValue !== null && filterValue !== undefined && filterValue.length !== 0) {
      // console.log("■filterValue■", filterValue)
      // console.log("■filterValue■", key)
      if (key === "tags" || key === "performers") {
        console.log("searchparams", searchparams)

        // if (Array.isArray(filterValue) && filterValue.length !== 0) {
        if (Array.isArray(filterValue) && filterValue.length !== 0) {
          filteredData = filteredData.filter(item => {
            return item[key].some(item2 => filterValue.includes(item2.name));
          });
        }
      }
      //  else {
      //   console.log("key", key)

      //   filteredData = filteredData.filter(item => {
      //     return item[key] && item[key].name === filterValue;
      //   });
      //   console.log("filteredData", filteredData)

      // }
    }
  // console.log("filteredData.length", filteredData.length)
  // console.log("searchparams", searchparams)
  }  return filteredData;
}

// const filteredData = ref(filterVideo(VIDEOS.value, searchparams.value))






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
  handleTagsInput(newSelectedItems) {
    console.log(VIDEOS.value)
    console.log(searchparams.value.tags)
    // this.filteredData = filterVideo(VIDEOS.value, searchparams.value.tags);
    // ここで必要な処理を実行する
  },

  resetSearchParams(searchparams, item) {
    if (item == "all") {
      for (let prop in searchparams) {
        console.log(prop)
        searchparams[prop] = [];
      }
    } else {
      searchparams[item] = [];
    }

    }


  // filterVideo(data, searchparams) {
  //   let filteredData = data
  //   // if SUBCONTENTS_ALL
  //   for (let key in searchparams) {
  //   // 各キーに対する処理を行う（ここではコンソールに表示）

  //     if (searchparams[key] != null) {
  //       if ((key === "tags" || key === "performers") && ((key === "tags" || key === "performers") && filteredData.length !== 0)) {
  //       } else {
  //         filteredData = filteredData.filter(item => {
  //         if (Array.isArray(searchparams[key])) {
  //           return searchparams[key].includes(item[key]?.name);
  //         } else {
  //           return item[key] && item[key].name === searchparams[key];
  //         }
  //       });
  //       }
  //     }
  //   }
  //   return filteredData;
  // },
  // searchparams.tagsが変更されたときに呼ばれるメソッド
  // updateFilteredData() {
  //   // filteredDataを再計算
  //   this.filteredData = this.filterVideo(this.SUBCONTENTS_ALL, this.searchparams);
  // },
  }
});





</script>



<template>

      <v-row no-gutters class="my-bg-color-white">
        <!-- {{ filteredData }} -->
        <v-col cols="12" class="mx-auto px-10">

        <v-container fluid>
                  
      <v-row dense>
        <v-col
          v-for="card in cards"
          :key="card.title"
          :cols="card.flex"
          class="py-3"

        >
        <v-card class="">
        <p class="mt-0 my-bg-color my-text-color-white">2022-04-02</p>

          <v-card
            aria-disabled
            disabled
            class="rounded-0"
          >
          


            <v-img
              :src="card.src"
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
                          aaaaaaaaa
                        </v-btn>
                      </v-col>
                    </v-row>










                    
              <v-card-title class="text-white text-h3" v-text="card.title"></v-card-title>
            </v-img>

              <!-- <v-card-actions>
                <v-spacer></v-spacer>

              <v-btn
                color="var(--my-color-green)"
                class="ms-auto px-6"
                size="x-large"
                variant="outlined"
                prepend-icon=""
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
