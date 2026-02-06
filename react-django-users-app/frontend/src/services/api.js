import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api/';

export const fetchUsers = async () => {
    try {
        const response = await axios.get(`${API_URL}users/`);
        return response.data;
    } catch (error) {
        console.error('Error fetching users:', error);
        throw error;
    }
};

export const deleteUser = async (userId) => {
    try {
        await axios.delete(`${API_URL}users/${userId}/`);
    } catch (error) {
        console.error('Error deleting user:', error);
        throw error;
    }
};

export const fetchUserDetails = async (userId) => {
    try {
        const response = await axios.get(`${API_URL}users/${userId}/`);
        return response.data;
    } catch (error) {
        console.error('Error fetching user details:', error);
        throw error;
    }
};