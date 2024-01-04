#!/usr/bin/node

const request = require('request');
const options = {
  url: process.argv[2],
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
    const ob = {};
    json.forEach(element => {
      if (ob[element.userId] !== undefined) {
        if (element.completed) {
          ob[element.userId] += 1;
        }
      } else {
        ob[element.userId] = 0;
      }
    });
    console.log(ob);
  }
});
