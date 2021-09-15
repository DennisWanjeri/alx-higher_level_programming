#!/usr/bin/node
const request = require('request');

const movie_id = process.argv[2];

if (parseInt(movie_id) < 8) {
    const url = 'https://swapi-api.hbtn.io/api/films/' + movie_id;
    request(url, function (err, response, body) {
	if (err) {
	    return console.log(err);
	}
	console.log(JSON.parse(body).title);
    });
}
