import { API } from '@/api';

const state = {	
	data_breach: {},
};
const mutations = {
	getAllDataBreachData(state, data) {
        state.data_breach = data.results;
		// console.log(state.data_breach)
	}
};
const actions = {
	async getAllDataBreachDataList(context) {
		let { data } = await API.DataBreach.getDataBreach();
		context.commit('getAllDataBreachData', data);	
	},
};


export default {
	namespaced: true,
	state,
	mutations,
	actions
}
