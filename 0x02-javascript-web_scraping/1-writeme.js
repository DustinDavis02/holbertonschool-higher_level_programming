#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];
const content = process.argv[3];

fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    console.error(`Error writing file: ${err.message}`);
    return;
  }
  console.log(`Successfully wrote ${content.length} bytes to ${filePath}`);
});
