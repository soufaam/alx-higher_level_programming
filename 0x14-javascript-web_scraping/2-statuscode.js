#!/usr/bin/node

const request = new Request(process.argv[2]);
fetch(request)
  .then((response) => {
    console.log('code:', response.status);
  });
