#!/usr/bin/node

const len = process.argv[2];
const size = parseInt(process.argv[2]);

if (len && size) {
  for (let i = 0; i < len; i++) {
    console.log('X'.repeat(len));
  }
} else {
  console.log('Missing Size');
}
