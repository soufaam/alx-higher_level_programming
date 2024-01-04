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
    let number = 0;
    json.results.forEach(element => {
      element.characters.forEach(strin => {
        if (strin.indexOf('18') > -1) {
          number += 1;
        }
      });
    });
    console.log(number);
  }
});
