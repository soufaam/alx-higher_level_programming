#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const options = {
  url: process.argv[2],
  method: 'GET',
  headers: {
    'Accept-Charset': 'utf-8'
  }
};
request(options, (error, response, body) => {
  if (error) {
    console.log(error.code);
  } else {
    fs.writeFileSync(process.argv[3], body, { encoding: 'utf8' });
  }
});
