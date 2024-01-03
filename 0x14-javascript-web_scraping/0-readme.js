#!/usr/bin/node
const fs = require('fs');
try {
  const contents = fs.readFileSync(process.argv[2], 'utf8');
  console.log(contents, '\n');
} catch (error) {
  console.error({
    Error: error.message,
    errno: error.errno,
    code: error.code,
    syscall: error.syscall,
    path: error.path
  });
}
