#!/usr/bin/node
const fs = require('fs');
try {
  fs.writeFileSync(process.argv[2], process.argv[3], { encoding: 'utf8' });
} catch (error) {
  console.error({
    Error: error.message,
    errno: error.errno,
    code: error.code,
    syscall: error.syscall,
    path: error.path
  });
}
