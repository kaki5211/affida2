<script setup lang="ts">


import { useRoute } from 'vue-router';

import { useStore } from 'vuex';
import { computed } from 'vue';
import { ref, onMounted,reactive } from 'vue';


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

let SUBCONTENTS = ref(route.path.split("/")[1]+"s")

let SUBCONTENTS_ALL = ref()
if (SUBCONTENTS.value === "performers") { SUBCONTENTS_ALL = PERFORMER_LIST }
else if (SUBCONTENTS.value === "tags") { SUBCONTENTS_ALL = TAG_LIST }
else if (SUBCONTENTS.value === "videos") { SUBCONTENTS_ALL = VIDEOS }
else if (SUBCONTENTS.value === "articles") { SUBCONTENTS_ALL = VIDEOS }


let headers_name = ref("");
if (SUBCONTENTS.value === "actors") { headers_name.value = "アクター"; } 
else if (SUBCONTENTS.value === "performers") { headers_name.value = "パフォーマー"; }
else if (SUBCONTENTS.value === "videos") { headers_name.value = "動画"; }
else if (SUBCONTENTS.value === "articles") { headers_name.value = "記事"; }






const headers = ref([
          { title: headers_name.value, align: 'start', key: 'name', value: 'name' },
          // { title: 'Calories', align: 'end', key: 'calories', value: 'calories' },
          // { title: 'Fat (g)', align: 'end', key: 'fat', value: 'fat' },
          // { title: 'Carbs (g)', align: 'end', key: 'carbs', value: 'carbs' },
          // { title: 'Protein (g)', align: 'end', key: 'protein', value: 'protein' },
          // { title: 'Iron (%)', align: 'end', key: 'iron', value: 'iron' },
        ])
        // sortable: false,

if (SUBCONTENTS.value === "performers") {
  headers.value.push({title: "生年月日", align: 'start', key: 'birth', value: 'birth' });
  headers.value.push({ title: "年齢", align: 'start', key: 'age', value: 'age' });
}

if (SUBCONTENTS.value === "videos") {
  headers.value.push({title: "タイトル", align: 'start', key: 'title', value: 'title' });
  headers.value.push({title: "パフォーマース", align: 'start', key: 'performers', value: 'performers' });
  headers.value.push({title: "タグ", align: 'start', key: 'tags', value: 'tags' });
  headers.value.push({title: "製品番号", align: 'start', key: 'productnumber', value: 'productnumber' });
  headers.value.push({title: "時間", align: 'start', key: 'duration', value: 'duration' });
  headers.value.push({title: "メーカー", align: 'start', key: 'maker', value: 'maker' });
}

if (SUBCONTENTS.value === "articles") {
  headers.value.push({title: "タイトル", align: 'start', key: 'title', value: 'title' });
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

            


<!-- 

  <v-table density="compact">
    <thead>
      <tr>
        <th class="text-left text-h3">
          Name
        </th>
        <th class="text-left text-h3">
          Calories
        </th>
      </tr>
    </thead>
    <tbody>
      <tr
        v-for="item in SUBCONTENTS_ALL"
        :key="item.name"
      >
      <td class="text-h4 my-4 py-2">
        <a :href="'/' + SUBCONTENTS + '/' + item.name_eng" class="custom-link">{{ item.name }}</a>
      </td>

      <td class="text-h4 my-4 py-2">
        <a :href="'/' + SUBCONTENTS + '/' + item.name_eng" class="custom-link">{{ item.name }}</a>
      </td>




      </tr>
    </tbody>
  </v-table> -->

  {{ VIDEOS }}
  <div>
    <VDataTable
    v-if="SUBCONTENTS_ALL && SUBCONTENTS"
    color="var(--my-color-black)"
    :loading="false"
    :items-per-page="-1"
    :headers="headers"
    :items="SUBCONTENTS_ALL"
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

  <template v-slot:item.name="{ item }">
    <router-link :to="{ name: 'Videos', query: { 'searchrequest': JSON.stringify([{[SUBCONTENTS]:item.name}])}}">
        {{ item.name }}
      </router-link>



  </template>
  

  </VDataTable>




<!-- 
  <template v-slot:item.name="{ item }">
      komento →　<router-link :to="{ name: SUBCONTENTS.charAt(0).toUpperCase() + SUBCONTENTS.slice(1), params:{param:item.selectable.name_eng }  }">
      <router-link :to="{ name: 'Videos', query: { 'searchrequest': JSON.stringify([{SUBCONTENTS:item.selectable.name}])}}">
        {{ item.selectable.name }}
      </router-link>
    </template> -->







  <!-- v-model:items-per-page="itemsPerPage" -->
  <!-- v-model:sort-by="sortBy" -->
  <!-- v-model:sort-desc="sortDesc" -->

    <!-- <div class="text-center pt-2">
      <v-btn
        color="primary"
        class="mr-2"
        @click="toggleOrder"
      >
        Toggle sort order
      </v-btn>
      <v-btn
        color="primary"
        @click="nextSort"
      >
        Sort next column
      </v-btn>
    </div> -->


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
