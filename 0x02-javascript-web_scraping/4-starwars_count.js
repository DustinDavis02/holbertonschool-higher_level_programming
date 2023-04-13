#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

const characterId = 18;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  if (response.statusCode !== 200) {
    console.error(`Error: Status code ${response.statusCode}`);
    return;
  }
  const films = JSON.parse(body).results;
  let count = 0;
  for (let i = 0; i < films.length; i++) {
    const characters = films[i].characters;
    if (characters.includes(`https://swapi-api.hbtn.io/api/people/${characterId}/`)) {
      count++;
    }
  }
  console.log(count);
});
