const axios = require('axios');

const url = 'https://api.theracingapi.com/v1/dams/search';
const params = {};
const username = 'VNeWmAgt84wp53xCArH7Jh2u';
const password = 'EbsXq6lsw7fhEBbIrlFgI8Wl';

axios.get(url, {
    auth: {
        username: username,
        password: password
    },
    params: params
})
.then(response => {
    console.log(response.data);
})
.catch(error => {
    console.error(error);
});