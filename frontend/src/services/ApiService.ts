import {instance as axios} from '../plugins/axios';

class ApiService{
    static async getAll(url: string): Promise<any> {
        try {
            const response = await axios.get(url);
            if (response.status === 200) {
                return response.data;
            } else {
                console.warn(`Unexpected response status: ${response.status}`);
                return null;
            }
        } catch (error) {
            console.error('Error fetching data:', error);
            throw error; // Ensure the error is properly propagated
        }

    }
}

export default ApiService;