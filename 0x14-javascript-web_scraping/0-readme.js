#!/usr/bin/node
require('fs').readFile(process.argv[2], 'utf-8', (err, d) => { if (err) { console.log(err); } else { console.log(d); } });
