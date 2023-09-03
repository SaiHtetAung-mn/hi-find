const axios = require('axios');

const BASE_URL = 'http://localhost:8000/api';

module.exports = axios.default.create({ 
    baseURL: BASE_URL, 
    headers: { "Content-Type": "application/json" } 
});