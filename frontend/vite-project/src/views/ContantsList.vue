<script setup lang="ts">


import { useRoute } from 'vue-router';

import { useStore } from 'vuex';
import { computed } from 'vue';
import { ref, onMounted,reactive, watch } from 'vue';


// import VDataTable from '../../node_modules/vuetify/lib/labs/VDataTable/index.mjs';
// import { VDataTable } from '@vuetify/nightly';
import { VDataTable,
  VDataTableServer,
  VDataTableVirtual, } from 'vuetify/labs/VDataTable'


// import { VideoPlayer } from '@videojs-player/vue'
// import 'video.js/dist/video-js.css'




const route = useRoute();
const store = useStore();


const VIDEOS = computed(() => { return store.getters.GET_VIDEOS; });
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
// const SUBCONTENTS_ALL = computed(() => { return store.getters.GET_SUBCONTENTS_ALL; });
const ARTICLE_LIST = computed(() => { return store.getters.GET_ARTICLE_LIST; });


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



    


// let SUBCONTENTS = ref(route.path.split("/")[1]+"s")
let SUBCONTENTS = ref(route.path.split("/")[1])


let SUBCONTENTS_ALL = ref()
if (SUBCONTENTS.value === "performer") { SUBCONTENTS_ALL = PERFORMER_LIST }
else if (SUBCONTENTS.value === "tag") { SUBCONTENTS_ALL = TAG_LIST }
else if (SUBCONTENTS.value === "video") { SUBCONTENTS_ALL = VIDEOS }
// else if (SUBCONTENTS.value === "article") { SUBCONTENTS_ALL = ARTICLE_LIST }


let headers_name = ref("");
if (SUBCONTENTS.value === "actor") { headers_name.value = "アクター"; } 
else if (SUBCONTENTS.value === "performer") { headers_name.value = "パフォーマー"; }
else if (SUBCONTENTS.value === "video") { headers_name.value = "動画"; }
else if (SUBCONTENTS.value === "article") { headers_name.value = "記事"; }





// let SUBCONTENTS_CLASS_MAJOR = ref()
// let SUBCONTENTS_CLASS_MEDIUM = ref()
// let SUBCONTENTS_CLASS_MINOR = ref()
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



  

const headers = ref([])
        // sortable: false,

if (SUBCONTENTS.value === "performer") {
  headers.value.push({title: "名前", align: 'start', key: 'name', value: 'name' });
  headers.value.push({title: "生年月日", align: 'start', key: 'birth', value: 'birth' });
  headers.value.push({ title: "年齢", align: 'start', key: 'age', value: 'age' });
}

if (SUBCONTENTS.value === "video") {
  headers.value.push({title: "タイトル", align: 'start', key: 'title', value: 'title' });
  headers.value.push({title: "パフォーマース", align: 'start', key: 'performers', value: 'performers' });
  headers.value.push({title: "タグ", align: 'start', key: 'tags', value: 'tags' });
  headers.value.push({title: "製品番号", align: 'start', key: 'productnumber', value: 'productnumber' });
  headers.value.push({title: "時間", align: 'start', key: 'duration', value: 'duration' });
  headers.value.push({title: "メーカー", align: 'start', key: 'maker', value: 'maker' });
}

if (SUBCONTENTS.value === "article") {
  headers.value.push({title: "タイトル", align: 'start', key: 'title', value: 'title' });
  headers.value.push({title: "大分類", align: 'start', key: 'classmajor', value: 'classmajor' });
  headers.value.push({title: "中分類", align: 'start', key: 'classmedium', value: 'classmedium' });
  headers.value.push({title: "小分類", align: 'start', key: 'classminor', value: 'classminor' });
  

  // headers.value.push({title: "項目", align: 'start', key: 'classmedium', value: 'classmedium' });



}




// function calculateAge(birthDate) {
//   const today = new Date();
//   const birthDateParts = birthDate.split('-');
//   const birthYear = Number(birthDateParts[0]);
//   const birthMonth = Number(birthDateParts[1]) - 1;
//   const birthDay = Number(birthDateParts[2]);

//   let age = today.getFullYear() - birthYear;
//   console.log("today.getFullYear()", today.getFullYear())
//   console.log("birthYear", birthYear)
//   console.log("age1", age)

//   if (today.getMonth() < birthMonth || (today.getMonth() === birthMonth && today.getDate() < birthDay)) {
//     age--;
//   }
//   console.log("age2", age)

//   return age;
// }

// for (let i = 0; i < SUBCONTENTS_ALL.value.length; i++) {
//   const item = SUBCONTENTS_ALL.value[i];
//   const age = calculateAge(item.birth);

//   item.age = age;
// }

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
    VDataTable,
    VDataTableServer,
    VDataTableVirtual,
    // VideoPlayer,
  },
  data () {
    return {

      search_view_performer: true,
      search_view_tag: true,
      filteredData: [],


      itemsPerPage: 5,
      model: [0,0,0,0,0,0,0,0,0,0],
      currentImageIndex: 0,
      startX: 0,
      startIndex: 0,
      currentX: 0,
      sortBy: 'fat',
      sortDesc: false,
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
  handleTouchMove(event, i, images) {
    const touch = event.touches[0];
    const distance = touch.clientX - this.startX;
    let changeindex = 0;
    changeindex = parseInt(distance / 100, 10);

    this.model[i] = (this.startIndex + changeindex + (images * 50)) % images
    console.log(this.model[i])
  },

  handleTouchMove2(event) {
      const touch = event.touches[0];
      const distance = touch.clientX - this.startX;

      // スワイプ距離とナビゲーションの座標を比較し、一致する座標を見つける
      const matchIndex = Math.round(distance / NAVIGATION_WIDTH); // ナビゲーションの幅に合わせて調整

      // 一致した座標に対応するインデックスを計算し、表示画像を更新する
      this.model = matchIndex;
    },  
  toggleOrder () {
      this.sortDesc = !this.sortDesc
    },
  nextSort () {
    let index = this.headers.findIndex(h => h.key === this.sortBy)
    index = (index + 1) % this.headers.length
    this.sortBy = this.headers[index].key
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

    },


},


computed: {
  filteredDesserts() {
    const { sortBy, sortDesc } = this;
    const sortedDesserts = this.desserts.slice().sort((a, b) => {
      const aValue = a[sortBy];
      const bValue = b[sortBy];
      return sortDesc ? bValue - aValue : aValue - bValue;
    });
    return sortedDesserts;
  }
},

});






</script>



<template>
  <v-app id="#my-scroll-target" v-if="VIDEOS_LOADED" class="my-bg-color">


    <v-row no-gutters class="my-bg-color-white">

        <v-col cols="12" class="mx-auto px-10">
          <v-card class="my-15">
            <v-card-text tag="h3" class="mt-6 my-underline text-center px-5 my-text-size-40 font-weight-medium">一覧</v-card-text>

            

            <!-- SUBCONTENTS_ALL:{{ SUBCONTENTS_ALL }} -->
            <!-- SUBCONTENTS: {{ SUBCONTENTS }} -->
            <!-- headers_name: {{ headers_name }} -->
            <v-card class="my-15 pb-15" v-if="SUBCONTENTS == 'video'">
              <v-row no-gutters class="px-0">
                <!-- <v-checkbox
                  cols="3"
                  v-for="item in TAG_LIST"
                  :key="item.name"
                  v-model="searchparams.tags"
                  :label="item.name"
                  :value="item.name"
                  @change="filteredData = filterVideo(VIDEOS, searchparams)"

                ></v-checkbox> -->


              <v-toolbar
                v-if="SUBCONTENTS == 'video'"

                flat
                dark
                class="my-bg-color"
              >
                <!-- <v-btn icon> -->
                  <!-- <v-icon>mdi-close</v-icon> -->
                <!-- </v-btn> -->
                <v-toolbar-title class="my-text-color-white font-weight-medium my-text-size-40">フィルター</v-toolbar-title>
              </v-toolbar>

              <v-col cols="12" class="mx-auto px-8">

                <div class="d-flex pt-10">
                  <a class="text-h5 ms-auto me-0 text-red">
                  ※項目内では OR検索　/　項目種類では AND検索 <br>
                  　（例１ (performer1 OR performer2) AND (tag1 OR tag2) <br>
                  　（例２ (performer1) AND (maker1) AND (tag1)
                </a>
                </div>

                <!-- <v-card height="" class="my-bg-color-white" elevation=0>
                  <v-row no-gutters>
                    <v-col cols="12" class="border">
                      <v-btn large outlined tile block class="my-text-color my-text-size-40 font-weight-medium rounded-tl-lg" height="50px" href="/performer"><v-icon>mdi-account-circle</v-icon>アカウント</v-btn>
                        <v-row no-gutters class="my-auto">
                          <v-col cols="12" class="border px-2 py-5 pb-10">
                            <v-btn
                              v-for="(item,i) in PERFORMER_LIST"
                              :key="i"
                              class="my-fit-contents my-text-size-30  ms-auto me-0"

                              >
                              {{item.name}}
                            </v-btn>
                          </v-col>
                        </v-row>
                    </v-col>
                  </v-row>
                </v-card>

                <v-card height="" class="my-bg-color-white mt-15" elevation=0>
                  <v-row no-gutters>
                    <v-col cols="12" class="border">
                      <v-btn large outlined tile block class="my-text-color my-text-size-40 font-weight-medium rounded-tl-lg" height="50px" href="/tag"><v-icon>mdi-tag-text-outline</v-icon>タグ</v-btn>
                        <v-row no-gutters class="my-auto">
                          <v-col cols="12" class="border px-2 py-5 pb-10">
                            <v-btn
                            v-for="(item,i) in TAG_LIST"
                            :key="i"
                            class="my-fit-contents my-text-size-30  ms-auto me-0"

                            v-model="searchparams.performers"
                            column
                            multiple
                            @click="filteredData = filterVideo(VIDEOS, searchparams)"
                            
                            >
                            {{item.name}}
                          </v-btn>
                          </v-col>
                        </v-row>
                        {{ searchparams.tags }}

                    </v-col>
                  </v-row>
                </v-card> -->








                  <div class="d-flex py-10">
                    <v-btn
                    @click="resetSearchParams(searchparams, 'all') ;filteredData = filterVideo(VIDEOS, searchparams)"
                    text="全てクリア"          
                    class="ms-auto me-0 my-text-size-30 my-fit-contents"
                    color="red"
                    >
                    <template v-slot:prepend>
                        <v-icon><Icon icon="iwwa:delete" /></v-icon>
                      </template>
                    </v-btn>
                  </div>  
                  <div class="d-flex">
                    <div
                    class="ms-auto me-0 my-text-size-40"
                    
                    >
                      全 
                      
                      <a v-if="VIDEOS" class="text-red">{{ filterVideo(VIDEOS, searchparams).length || "0"}}</a>

                      件 表示
                    </div>
                  </div>

                    <!-- アカウント -->
                    <v-card height="" class="my-bg-color-white" elevation=0>
                      <v-row no-gutters>
                        <v-col cols="12" class="border">
                          <v-btn large outlined tile block class="my-text-color my-text-size-40 font-weight-medium rounded-tl-lg"
                          height="50px" @click="search_view_performer=!search_view_performer"><v-icon>mdi-account-circle</v-icon>アカウント</v-btn>
                            <v-row v-if="search_view_performer" no-gutters class="my-auto">
                              <v-col cols="12" class="border px-2 py-5 pb-10">
                                  <v-chip-group
                                    v-model="searchparams.performers"
                                    column
                                    multiple
                                    color="text-deep-purple-accent-4"

                                    @click="filteredData = filterVideo(VIDEOS, searchparams)"
                                  >
                                      <v-chip
                                      v-for="item in PERFORMER_LIST"
                                      :key="item.id"
                                      label
                                      outline
                                      :value="item.name"
                                      color="red"

                                      class="custom-chip-style mx-0 mb-1 mt-0 elevation-1"

                                    >
                                      {{ item.name }}
                                    </v-chip>
                                  </v-chip-group>
                                  <!-- {{searchparams.performers}} -->

                                  <div class="d-flex py-3">
                                    <v-btn
                                    @click="resetSearchParams(searchparams, 'performers') ;filteredData = filterVideo(VIDEOS, searchparams)"
                                    text="アカウントをクリア"          
                                    class="ms-auto me-0 my-text-size-30 my-fit-contents"
                                    color="red"
                                    >
                                    <template v-slot:prepend>
                                        <v-icon><Icon icon="iwwa:delete" /></v-icon>
                                      </template>
                                    </v-btn>
                                  </div>
                                  
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
                                    v-model="searchparams.tags"
                                    column
                                    multiple
                                    @click="filteredData = filterVideo(VIDEOS, searchparams)"

                                  >
                                      <v-chip
                                      v-for="item in TAG_LIST"
                                      :key="item.id"
                                      label
                                      outline
                                      :value="item.name"
                                      color="red"

                                      
                                      class="custom-chip-style mx-0 mb-1 mt-0 elevation-1"

                                    >
                                      {{ item.name }}
                                    </v-chip>
                                  </v-chip-group>
                                  <!-- {{searchparams.tags}} -->

                                  <div class="d-flex py-3">
                                    <v-btn
                                    @click="resetSearchParams(searchparams, 'tags') ;filteredData = filterVideo(VIDEOS, searchparams)"
                                    text="タグをクリア"
                                    class="ms-auto me-0 my-text-size-30 my-fit-contents"
                                    color="red"
                                    >
                                      <template v-slot:prepend>
                                        <v-icon><Icon icon="iwwa:delete" /></v-icon>
                                      </template>
                                    </v-btn>
                                  </div>
                              </v-col>
                            </v-row>
                        </v-col>
                      </v-row>
                    </v-card>







                  </v-col>
              </v-row>

          </v-card>

          <v-spacer class="py-10"></v-spacer>
  <div>
    <VDataTable
    v-if="SUBCONTENTS_ALL && SUBCONTENTS"
    color="var(--my-color-black)"
    :loading="false"
    :items-per-page="-1"
    :headers="headers"
    :items="filteredData.length === 0 ? SUBCONTENTS_ALL : filteredData"
    item-value="name"
    class="elevation-1 custom-table"
    :items-per-page-options="[ {value: -1, title: 'All'} ]"
    items-per-page-text=""
    page-text=""
    next-icon=""
    prev-icon=""
    first-icon=""
    last-icon=""
    style="overflow-x: scroll; width: 100%; border-collapse: collapse; white-space: nowrap;"
  >
  <template v-if="SUBCONTENTS === 'article'" v-slot:item.title="{ item }">
    <router-link :to="{ name: 'Article', params: { param: item.classmajor, param2: item.classmedium, param3: item.classminor, param4: item.number} }">
      {{ item.title }}
    </router-link>
  </template>
  
  <template v-if="SUBCONTENTS === 'video'" v-slot:item.title="{ item }">
    <router-link :to="{ name: 'Videos', query: { 'searchrequest': JSON.stringify([{[SUBCONTENTS + 's']:item.name}])}}">
        {{ item.title }}
      </router-link>
  </template>
  <template v-if="SUBCONTENTS === 'video'" v-slot:item.tags="{ item }">
    <a v-for="(item2, index) in item.tags" :key="item2.name" style="white-space: nowrap; overflow-x: auto">
      <a>{{ index > 0 && item.tags.length > 0 ? ', ' : '' }}</a>
      <router-link :to="{ name: 'Videos', query: { 'searchrequest': JSON.stringify([{[SUBCONTENTS + 's']:item.name}])}}">
        {{ item2.name }}
      </router-link>
    </a>
  </template>
  <template v-if="SUBCONTENTS === 'video'" v-slot:item.performers="{ item }">
    <a v-for="(item2, index) in item.performers" :key="item2.name" style="white-space: nowrap; overflow-x: auto">
      <a>{{ index > 0 && item.tags.length > 0 ? ', ' : '' }}</a>
      <router-link :to="{ name: 'Videos', query: { 'searchrequest': JSON.stringify([{[SUBCONTENTS + 's']:item.name}])}}">
        {{ item2.name }}
      </router-link>
    </a>
  </template>
  <template v-if="SUBCONTENTS === 'video'" v-slot:item.maker="{ item }">
        {{ item.maker != '' ? item.maker : '' }}
  </template>


  









  </VDataTable>
  </div>





















  <div>
</div>


  </v-card>
</v-col>
</v-row>




  </v-app>
  <div v-else>
      データを読み込んでいます...
  </div>
</template>




<style>


/* .v-table {
    --v-table-header-height: 20px;
    border-radius: inherit;
    line-height: 1.2;
    max-width: 100%;
} */

/* 
.v-data-table__tr>td{
    height: calc(var(--v-table-row-height, 52px) + 10px)!important;
} */
:root {
  --v-table-row-height: 30px;
}
.v-img__img--cover {
    object-fit: cover;
    object-position: right;
}



</style>
