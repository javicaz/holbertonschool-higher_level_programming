#!/usr/bin/node
// This script display the status code of a GET request.
const request = require('request');

request.get(process.argv[2])
  .then(res => {
    console.log('code:', res.status);
  })
  .catch(err => {
    console.log('code:', err.response.status);
  });
