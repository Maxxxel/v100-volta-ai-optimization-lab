'use strict';
const fs=require('fs'),assert=require('assert');assert.equal(process.getuid(),65534);const src=fs.readFileSync(0);if(src.length>1048576)throw Error('Input bound');const catalog=JSON.parse(src);require('/harness/caveman-shrink.cjs').compressDescriptionsInPlace(catalog);process.stdout.write(JSON.stringify(catalog));
