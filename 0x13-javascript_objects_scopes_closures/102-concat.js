#!/usr/bin/node

const fs = require('fs');

const contents = fs.readFileSync(process.argv[2], 'utf8');
fs.writeFileSync(process.argv[4], contents, { encoding: 'utf8' });
const contents2 = fs.readFileSync(process.argv[3]);
fs.appendFileSync(process.argv[4], contents2, { encoding: 'utf8' });
