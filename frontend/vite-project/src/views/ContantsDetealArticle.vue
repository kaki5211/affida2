<script setup lang="ts">


import { useRoute } from 'vue-router';

import { useStore } from 'vuex';
import { computed } from 'vue';
import { ref, onMounted, watch } from 'vue';
import { reactive } from 'vue';


import { VDataTable,
  VDataTableServer,
  VDataTableVirtual, } from 'vuetify/labs/VDataTable'



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
const ARTICLE_CLASS = ref(route.path.split("/").slice(2, 6))



const ARTICLE_DETEAL = ref([]);

watch(ARTICLE_LIST, (newVal, oldVal) => {
  if (newVal) {  
    ARTICLE_DETEAL.value = newVal.filter(item => 
    item.classmajor === ARTICLE_CLASS.value[0] && 
    item.classmedium === ARTICLE_CLASS.value[1] && 
    item.classminor === ARTICLE_CLASS.value[2] &&
    item.title_number === parseInt(ARTICLE_CLASS.value[3])
    );
  }
});





let headers_name = ref("雑記");

const headers = ref([])
// sortable: false,
// if (SUBCONTENTS.value === "performer") {
//   headers.value.push({title: "名前", align: 'start', key: 'name', value: 'name' });
//   headers.value.push({title: "生年月日", align: 'start', key: 'birth', value: 'birth' });
//   headers.value.push({ title: "年齢", align: 'start', key: 'age', value: 'age' });
// }

headers.value.push({ title: "項目", align: 'start', key: 'name', value: 'name' });
headers.value.push({ title: "項目2", align: 'start', key: 'price', value: 'price' });
headers.value.push({ title: "投稿日", align: 'start', key: 'post_day', value: 'post_day' });
headers.value.push({ title: "クリック数", align: 'start', key: 'views', value: 'views' });
headers.value.push({ title: "説明", align: 'start', key: 'views', value: 'views' });





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
});





</script>



<template>




      <v-row no-gutters class="my-bg-color-white">
        <p>{{ ARTICLE_LIST }}</p>-------------------
        <p>{{ ARTICLE_CLASS }}</p>-------------------
        <p>{{ ARTICLE_DETEAL }}</p>-------------------

        <!-- {{ filteredData }} -->
        <v-col cols="12" class="mx-auto px-10">

        <v-container fluid>
                  
      <v-row v-if="ARTICLE_DETEAL" dense>
        <v-col
          class="py-3"

        >
        <v-card class="">
        <p class="mt-0 my-bg-color my-text-color-white">2022-04-02</p>




        <div>
          <VDataTable
          v-if="ARTICLE_DETEAL"
          color="var(--my-color-black)"
          :loading="false"
          :items-per-page="-1"
          :headers="headers"
          :items="ARTICLE_DETEAL"
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
        <template v-slot:item.title="{ item }">
            {{ item.title }}
        </template>





        <!-- <template v-slot:item.name="{ item }">
          <router-link :to="{ name: 'Videos', query: { 'searchrequest': JSON.stringify([{[SUBCONTENTS + 's']:item.name}])}}">
              {{ item.name }}
            </router-link>
        </template>
        -->

        </VDataTable>
        </div>





        </v-card>

        </v-col>
      </v-row>






      <v-row v-if="ARTICLE_DETEAL" dense>
        <v-col
          v-for="card in ARTICLE_DETEAL"
          :key="card.number"
          class="py-3"

        >
        <v-card class="">
        <p class="mt-0 my-bg-color my-text-color-white">2022-04-02</p>

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
