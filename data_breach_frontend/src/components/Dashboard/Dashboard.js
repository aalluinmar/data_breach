import { API } from '@/api';
import { mapState } from 'vuex';
import { Bar } from 'vue-chartjs';
import databreach from '../../store/modules/databreach';

export default {
	extends: Bar,
	components: {
	},
	data() {
		return {
			data_breach: ''
		};
	},
	async created() {
        this.getDataBreachList()
	},
	computed: {
	},
	methods: {
		get_bar_chart(data_breach_data) {
			var barChartStateObject = []
			var barChartIndividualsObject = []
			for(var i = 0; i < data_breach_data.length; i++) {
				console.log(data_breach_data[i].state, data_breach_data[i].individuals_affected)
				var count = parseInt(data_breach_data[i].individuals_affected);
				for(var j = 0; j < data_breach_data.length; j++) {
					if(data_breach_data[i].state === data_breach_data[j].state) {
						count = count + parseInt(data_breach_data[j].individuals_affected)
					}
				}
				barChartStateObject.push(data_breach_data[i].state)
				barChartIndividualsObject.push(count)
				console.log(data_breach_data.length)
				data_breach_data.splice(data_breach_data.findIndex(a => a.state === data_breach_data[i].state), 1)
			}
			console.log(barChartStateObject)
			console.log(barChartIndividualsObject)
		},
        async getDataBreachList() {
			await API.DataBreach.getDataBreach().then(res => {
				if(res.data.count > 0){
					this.$Notice.success({
						title: 'DataBreach List',
						desc: "DataBreach Loaded Successfully."
					});
				} else {
					this.$Notice.error({
						title: 'DataBreach List',
						desc: "DataBreach data Initiation Failed."
					});
				}
				this.$store.dispatch('databreach/getAllDataBreachDataList')
				this.data_breach = res.data.results
			}).catch(err => {
				console.log(err)
				this.$Notice.error({
					title: 'Products List',
					desc: "Products data Initiation Failed."
				});
			})
            this.$store.dispatch('databreach/getAllDataBreachDataList')
			this.get_bar_chart(this.data_breach)
        },
	}
};
