<template>
	<div>
		<div>
			<navigation></navigation>
			<dashboard></dashboard>
			<router-view></router-view>
		</div>
	</div>
</template>
<script>
import Navigation from './Navigation';
import Dashboard from '../components/Dashboard/Dashboard.vue';
import { mapState } from 'vuex';
import { API } from '@/api';
export default {
	components: {
    	Navigation,
		Dashboard
	},
	data() {
		return {
			msg: 'I am a Base Component',
		};
	},
	async created() {
		// await API.DataBreach.getDataBreach().then(res => {
		// 	// console.log(res.data);
		// 	if(res.data.count > 0){
		// 		this.$Notice.success({
		// 			title: 'DataBreach List',
		// 			desc: "DataBreach Loaded Successfully."
		// 		});
		// 	} else {
		// 		this.$Notice.error({
		// 			title: 'DataBreach List',
		// 			desc: "DataBreach data Initiation Failed."
		// 		});
		// 	}
		// 	this.$store.dispatch('databreach/getAllDataBreachDataList')
		// }).catch(err => {
		// 	console.log(err)
		// 	this.$Notice.error({
		// 		title: 'Products List',
		// 		desc: "Products data Initiation Failed."
		// 	});
		// })
	},
	methods: {
	}
};
</script>
<style lang="stylus" scoped>
</style>
