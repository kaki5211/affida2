<script setup>


// ■■■■■■ import > Packages ■■■■■■
import { computed } from 'vue';
// import { onMounted } from 'vue';
// import { ref } from 'vue';
import { reactive } from 'vue';
import { useStore } from 'vuex';
// import { useRoute } from 'vue-router';



// ■■■■■■ import > Others ■■■■■■
// import { Icon } from '@iconify/vue';




// ■■■■■■ import > Components ■■■■■■
// import Btn_1 from '../components/_Btn_1_mottomiru.vue';
// import Text_1 from '../components/_Text_1.vue';
// import HelloWorld from './components/HelloWorld.vue'
import Meta from './components/Meta.vue';
import ToolBar from './components/ToolBar.vue';
// import Topimage from './components/Topimage.vue';
import Footer from './components/Footer.vue';
// import Breadcrumbs from './components/Breadcrumbs.vue';





// ■■■■■■ VueStore ■■■■■■
const store = useStore();
const VIDEOS = computed(() => { return store.getters.GET_VIDEOS; });
// const PERFORMER_LIST = computed(() => { return store.getters.GET_PERFORMER_LIST; });
// const TAG_LIST = computed(() => { return store.getters.GET_TAG_LIST; });
// const MAKER_LIST = computed(() => { return store.getters.GET_MAKER_LIST; });
// const LABEL_LIST = computed(() => { return store.getters.GET_LABEL_LIST; });
// const SERIES_LIST = computed(() => { return store.getters.GET_SERIES_LIST; });
// const KYOUNUKI_LIST = computed(() => { return store.getters.GET_KYOUNUKI_LIST; });
// const VIDEOS_LOADED = computed(() => { return store.getters.GET_VIDEOS_LOADED; });
// const URL_LIST = computed(() => { return store.getters.GET_URL_LIST; });
// const URL_PARAM = computed(() => { return store.getters.GET_URL_PARAM; });
// const URL_JUDGE_PARAM = computed(() => { return store.getters.GET_URL_JUDGE_PARAM; });
// const SUBCONTENTS = computed(() => { return store.getters.GET_SUBCONTENTS; });
// const SUBCONTENTS_ALL = computed(() => { return store.getters.GET_SUBCONTENTS_ALL; });
const DEBUG = computed(() => { return store.getters.GET_DEBUG; });
console.log("DEBUG", DEBUG.value)


// ■■■■■■ VueRouter ■■■■■■
// const route = useRoute();



</script>




<script>
import GlobalStyles from './components/_GlobalStyles.vue';
import { defineComponent } from 'vue'


export default defineComponent({
	components: {
    GlobalStyles,
	},
});
</script>



















<template>

<v-app id="#my-scroll-target">
  <Meta />

    <!-- <template v-slot:title="{ content }">{{ content ? `${content} | SITE_NAME` : `SITE_NAME` }}</template> -->


  <ToolBar />




  <!-- <Topimage /> -->


  <!-- <Judgeurl /> -->
  <!-- <v-row no-gutters> -->
    <!-- <v-col cols="12"> -->
      <!-- <Breadcrumbs /> -->
    <!-- </v-col> -->
  <!-- </v-row> -->
    
  <v-main class="my-bg-color-white">
    router!!
    <router-view />
  </v-main>


<v-btn>
  あいうえお
</v-btn>
<sparcer>
  
</sparcer>

  <div>
      データを読み込んでいます...
      <!-- url_judge_param: {{ URL_JUDGE_PARAM }} -->
      VIDEOS: {{ VIDEOS }}
  </div>

  <Footer />
</v-app>





</template>

<style>

</style>
