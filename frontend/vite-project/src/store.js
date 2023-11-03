import { createStore } from 'vuex';
import axios from 'axios';
import { useRoute } from 'vue-router';
const route = useRoute();

// import createPersistedState from 'vuex-persistedstate'





// URL選択
// const host = "http://127.0.0.1:8000"
// const host_api = "http://127.0.0.1:8000/api"
// const host = "http://172.20.10.5:8000"
// const host_api = "https://localhost:8000/api"
// const host_api = "https://153.122.199.147]:8000/api"
// const host_api = "https://153.122.199.147:8080/api"



// const host_api = "https://kyounuki.jp:8080/api"
const host_api = "http://172.20.10.4:8000/api"


// http://localhost:8000/api/your-endpoint/






// fetchDataAndCommit
async function fetchDataAndCommit({ commit, endpoint, mutationType }) {
  const response = await axios.get(`${host_api}/${endpoint}/`);
  commit(mutationType, response.data);
}














const store = createStore({
  // plugins: [createPersistedState()],
  state: {
    videos: null,
    performer_list: null,
    tag_list: null,
    maker_list: null,
    label_list: null,
    series_list: null,
    kyounuki_list: null,
    contents_list: null,
    article_list: null,
    article_list_dup: null,
    article_list_params: {
      classmajor: [],
      classmedium: [],
      classminor: [],
    },



    searchparams: {
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
    },
    searchparams_article: {
      classmajor: [],
      classmedium: [],
      classminor: [],
    },
    set_videos_loaded: null,

    url_list: null,
    url_param: null,
    url_judge_param: null,
    subcontents: null,
    subcontents_all: null,

    debug: null,
    breadcrumbs: null,

    // Contents_list: [], 
    // Url_list_loaded: null, // urllist取得完了フラグ
    // Contents_loaded: null, // コンテンツデータ取得完了フラグ
  },
  mutations: {
    SET_VIDEOS(state, data) { state.videos = data; },
    SET_PERFORMER_LIST(state, data) { state.performer_list = data; },
    SET_TAG_LIST(state, data) { state.tag_list = data; },

    SET_ARTICLE_LIST(state, data) { state.article_list = data; },
    SET_ARTICLE_LIST_DUP(state, data) { state.article_list_dup = data; },
    SET_ARTICLE_LIST_PARAMS(state, data) { state.article_list_params = data; },


    SET_MAKER_LIST(state, data) { state.maker_list = data; },
    SET_LABEL_LIST(state, data) { state.label_list = data; },
    SET_SERIES_LIST(state, data) { state.series_list = data; },
    SET_KYOUNUKI_LIST(state, data) { state.kyounuki_list = data; },

    SET_VODEOS_LOADED(state, data) { state.set_videos_loaded = data; },

    SET_URL_LIST(state, data) { state.url_list = data; },

    SET_URL_PARAM(state, data) { state.url_param = data; },
    SET_URL_JUDGE_PARAM(state, data) { state.url_judge_param = data; },
    SET_SUBCONTENTS(state, data) { state.subcontents = data; },
    SET_SUBCONTENTS_ALL(state, data) { state.subcontents_all = data; },

    SET_DEBUG(state, data) { state.debug = data; },
    SET_BREADCRUMBS(state, data) { state.breadcrumbs = data; },

    SET_CONTENTS_LIST(state, data) { state.contents_list = data; },

    SET_SEARCHPARAMS(state, data) { state.searchparams = data; },
    SET_SEARCHPARAMS_ARTICLE(state, data) { state.searchparams_article = data; },
    
    // SET_CONTENTS(state, data) { state.Contents_list = [data]; },
    // ADD_CONTENTS(state, data) { state.Contents_list.push(data); },
    // ADD_CONTENTS(state, data) { Vue.set(state.Contents_list, state.Contents_list.length, data); },

  
    
    // SET_URL_LOADED(state, data) { state.Url_list_loaded = data; },
    // SET_CONTENTS_LOADED(state, data) { state.Contents_loaded = data; },
  },

  actions: {
    async FETCH_GET_VIDEOS({ commit }) {
      commit('SET_VODEOS_LOADED', false); // データの取得状態を初期化
      fetchDataAndCommit({ commit, endpoint: 'videos_view', mutationType: 'SET_VIDEOS' });
      commit('SET_VODEOS_LOADED', true); // データの取得状態を更新
      console.log('SET_URL_LOADED: Completed')
      
    },
    async FETCH_GET_PERFORMER_LIST({ commit }) {
      await fetchDataAndCommit({ commit, endpoint: 'performer_list_view', mutationType: 'SET_PERFORMER_LIST' });
    },
    async FETCH_GET_TAG_LIST({ commit }) {
      await fetchDataAndCommit({ commit, endpoint: 'tag_list_view', mutationType: 'SET_TAG_LIST' });
    },
    async FETCH_GET_KYOUNUKI_LIST({ commit }) {
      await fetchDataAndCommit({ commit, endpoint: 'kyounuki_list_view', mutationType: 'SET_KYOUNUKI_LIST' });
    },
    async FETCH_GET_URL_LIST({ commit }) {
      await fetchDataAndCommit({ commit, endpoint: 'url_list_view', mutationType: 'SET_URL_LIST' });
    },
    async FETCH_GET_MAKER_LIST({ commit }) {
      await fetchDataAndCommit({ commit, endpoint: 'maker_list_view', mutationType: 'SET_MAKER_LIST' });
    },
    async FETCH_GET_LABEL_LIST({ commit }) {
      await fetchDataAndCommit({ commit, endpoint: 'label_list_view', mutationType: 'SET_LABEL_LIST' });
    },
    async FETCH_GET_SERIES_LIST({ commit }) {
      await fetchDataAndCommit({ commit, endpoint: 'series_list_view', mutationType: 'SET_SERIES_LIST' });
    },
    async FETCH_GET_ARTICLE_LIST({ commit }) {
      await fetchDataAndCommit({ commit, endpoint: 'article_list_view', mutationType: 'SET_ARTICLE_LIST' });
    },
    async FETCH_GET_ARTICLE_LIST_DUP({ commit }) {
      await fetchDataAndCommit({ commit, endpoint: 'article_list_dup_view', mutationType: 'SET_ARTICLE_LIST_DUP' });
    },
    async FETCH_GET_ARTICLE_LIST_PARAMS({ commit }) {
      await fetchDataAndCommit({ commit, endpoint: 'article_list_params_view', mutationType: 'SET_ARTICLE_LIST_PARAMS' });
    },

    async FETCH_GET_DEBUG({ commit }) {
        
      console.log("urlhost.includes('172.')", urlhost.includes("172."))
      commit('SET_DEBUG', urlhost.includes("kyounuki"));
    },
    async FETCH_GET_BREADCRUMBS({ commit }, newpath) {
      // const { path_ } = payload; // payloadオブジェクトから引数を取り出す
      // URLのパスを取得
      // const urlPath2 = path_
      
      let urlPath;

      if (newpath != null) {
        urlPath = newpath;
        console.log("urlPath", newpath)
      } else {
        urlPath = window.location.pathname;
        console.log("window.location.pathname", window.location.pathname)

      }


      


      
      
      // 事前に定義したパスと表示する文字列の対
      const pathMapping = {
        video: "動画",
        performer: "パフォーマー",
        maker: "メーカー",
        kyounuki: "今日抜き",
        matome: "まとめ",
        article: "雑記"
        
,        // ...
      };
      

      
      
      
      // パスを"/"で区切ってリストに変換
      const pathList = urlPath.split("/").filter((path) => path !== "");
      console.log("urlPath", urlPath)
      // console.log("urlPath2", urlPath2)
      console.log("pathList", pathList)


      
      // パンくずリストの初期化
      let breadcrumbsList = ""
      breadcrumbsList = [
        {
          title: 'ホーム',
          disabled: false,
          to: '/',
        },
      ];
      console.log("breadcrumbsList", breadcrumbsList)
      
      // パスごとにパンくずリストを作成
      let currentPath = "";
      for (let i = 0; i < pathList.length; i++) {
        const path = pathList[i];
        currentPath += `/${path}`;
        const name = pathMapping[path] || path;
        const disabled = i === (pathList.length - 1); // 最後の要素の場合のみ disabled: true
        breadcrumbsList.push({ title: name, disabled, to: currentPath });
      }
      // console.log("pathList",pathList)
      // console.log("breadcrumbsList", breadcrumbsList)


      
      // let title =''
      // console.log("pathList.value[1]", pathList.value[1], pathList.value[2], pathList.value[3])


      // if (pathList.includes("article") && !pathList.includes("list")) {  
      //   title = this.article_list.filter(item => 
      //   item.classmajor === pathList.value[1] && 
      //   item.classmedium === pathList.value[2] && 
      //   item.classminor === pathList.value[3] &&
      //   item.title_number === parseInt(pathList.value[4])
      //   );
      // }
      
      // if (title !== '') {
      //   breadcrumbsList[breadcrumbsList.length - 1].title = title;
      // }
      console.log("SET_BREADCRUMBS>breadcrumbsList", breadcrumbsList)
      commit('SET_BREADCRUMBS', breadcrumbsList);
    },
    async FETCH_GET_CONTENTS_LIST({ commit }) {
      await fetchDataAndCommit({ commit, endpoint: 'contents_list', mutationType: 'SET_CONTENTS_LIST' });
    },

    // async FETCH_GET_URL_LIST({ commit }) {
    //   await fetchDataAndCommit({ commit, endpoint: 'url_list_view', mutationType: 'SET_URL_LIST' });
    // },


    // async FETCH_GET_maker_LIST({ commit }) {
    //   await fetchDataAndCommit({ commit, endpoint: 'maker_list_view', mutationType: 'SET_MAKER_LIST' });
    // },



    // async FETCH_GET_PERFORMER_LIST({ commit }) {
    //   const get_performer_list = axios.get(`${host_api}/performer_list_view/`);
    //   const performer_list = await get_performer_list;
    //   await commit('SET_PERFORMER_LIST', performer_list.data);
    // },

    // async FETCH_GET_TAG_LIST({ commit }) {
    //   const get_tags_list = axios.get(`${host_api}/tag_list_view/`);
    //   const tags_list = await get_tags_list;
    //   await commit('SET_TAG_LIST', tags_list.data);
    // },

    // async FETCH_GET_maker_LIST({ commit }) {
    //   const get_makers_list = axios.get(`${host_api}/maker_list_view/`);
    //   const makers_list = await get_makers_list;
    //   await commit('SET_MAKER_LIST', makers_list.data);
    // },


},  


  getters: {
    GET_VIDEOS: (state) => state.videos,
    GET_PERFORMER_LIST: (state) => state.performer_list,
    GET_TAG_LIST: (state) => state.tag_list,

    GET_ARTICLE_LIST: (state) => state.article_list,
    GET_ARTICLE_LIST_DUP: (state) => state.article_list_dup,
    GET_ARTICLE_LIST_PARAMS: (state) => state.article_list_params,

    GET_MAKER_LIST: (state) => state.maker_list,
    GET_LABEL_LIST: (state) => state.label_list,
    GET_SERIES_LIST: (state) => state.series_list,
    GET_KYOUNUKI_LIST: (state) => state.kyounuki_list,
    

    GET_SEARCHPARAMS: (state) => state.searchparams,
    GET_SEARCHPARAMS_ARTICLE: (state) => state.searchparams_article,

    GET_VIDEOS_LOADED: (state) => state.set_videos_loaded,


    GET_URL_LIST: (state) => state.url_list,
    GET_URL_PARAM: (state) => state.url_param,
    GET_URL_JUDGE_PARAM: (state) => state.url_judge_param,
    GET_SUBCONTENTS: (state) => state.subcontents,
    GET_SUBCONTENTS_ALL: (state) => state.subcontents_all,

    GET_DEBUG: (state) => state.debug,
    GET_BREADCRUMBS: (state) => state.breadcrumbs,

    GET_CONTENTS_LIST: (state) => state.contents_list,


  } 
});


(async () => {
  try {
    // await store.dispatch('fetchUrlListData');
    // await store.dispatch('fetchData');
    await store.dispatch('FETCH_GET_VIDEOS');
    await store.dispatch('FETCH_GET_PERFORMER_LIST');
    await store.dispatch('FETCH_GET_TAG_LIST');
    await store.dispatch('FETCH_GET_KYOUNUKI_LIST');
    await store.dispatch('FETCH_GET_URL_LIST');
    await store.dispatch('FETCH_GET_MAKER_LIST');
    await store.dispatch('FETCH_GET_LABEL_LIST');
    await store.dispatch('FETCH_GET_SERIES_LIST');
    // await store.dispatch('FETCH_GET_DEBUG');
    // await store.dispatch('FETCH_GET_BREADCRUMBS', { path_: "success!" })
    // await store.dispatch('FETCH_GET_BREADCRUMBS')
    await store.dispatch('FETCH_GET_CONTENTS_LIST');
    await store.dispatch('FETCH_GET_ARTICLE_LIST');
    await store.dispatch('FETCH_GET_ARTICLE_LIST_DUP');
    await store.dispatch('FETCH_GET_ARTICLE_LIST_PARAMS');

    

    // await store.dispatch('FETCH_GET_URL_LIST');

    console.log('Data fetched successfully');
    
  } catch (error) {
    console.log('Error fetching data:', error);
  }
})();

export default store;
