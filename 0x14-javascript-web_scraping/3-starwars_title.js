#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/';
const endpoint = url + process.argv[2];
const options = {
  url: endpoint,
  method: 'GET',
  headers: {
    Accept: 'application/json',
    'Accept-Charset': 'utf-8'
  }
};
request(options, (error, response, body) => {
  if (error) {
    console.log(error.code);
  } else {
    const json = JSON.parse(body);
    console.log(json.title);
  }
});
