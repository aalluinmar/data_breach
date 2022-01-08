import Vue from 'vue'
import Vuex from 'vuex'

import databreach from './modules/databreach'

Vue.use(Vuex)

export default new Vuex.Store({
	modules: {
		databreach
	},
})
