#!/usr/bin/node
const { createWriteStream } = require('fs');
const fetch = require('node-fetch');

(async () => {
  const response = await fetch(process.argv[2]);
  const writer = createWriteStream(process.argv[3]);

  await new Promise((resolve, reject) => {
    response.body.pipe(writer)
      .on('finish', resolve)
      .on('error', reject);
  });
})();
