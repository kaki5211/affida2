<script setup>

import { computed } from 'vue';
// import { useRoute } from 'vue-router';
import { useStore } from 'vuex';


// const route = useRoute();
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




</script>

<template>

  <div>
    <a href="https://vitejs.dev" target="_blank">
      <img src="/vite.svg" class="logo" alt="Vite logo" />
    </a>
    <a href="https://vuejs.org/" target="_blank">
      <img src="../assets/vue.svg" class="logo vue" alt="Vue logo" />
    </a>
    <p>ABOUT！</p>
        ■■■VIDEOS：{{ VIDEOS }}
  </div>
</template>


