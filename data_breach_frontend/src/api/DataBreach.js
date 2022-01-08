import APIFetch from '@/helpers/APIFetch';

const endpoint = '/api/databreach/';

var headers= {
	"Access-Control-Allow-Origin": "*",
	"Access-Control-Allow-Methods": "GET, POST, PATCH, PUT, DELETE, OPTIONS",
	"Access-Control-Allow-Headers": "Origin, Content-Type, X-Auth-Token"
}

export class DataBreach {
	static getDataBreach() {
		return APIFetch.get(`${endpoint}`, headers=headers);
    }
    static readDataBreachId(id) {
		return APIFetch.get(`${endpoint}${id}/`);
    }
    static createDataBreach(data) {
		return APIFetch.post(`${endpoint}`, data);
	}
	static updateDataBreach(id, data) {
		return APIFetch.put(`${endpoint}${id}/`, data);
	}
	static deleteDataBreach(id) {
		return APIFetch.delete(`${endpoint}${id}/`);
	}
}
