#!/usr/bin/node
const request = require('request');
const APIurl = process.argv[2];

request.get(APIurl, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const tasks = JSON.parse(body);
  const compTasks = {};

  for (const t of tasks) {
    if (t.completed) {
      if (compTasks[t.userId]) {
        compTasks[t.userId]++;
      } else {
        compTasks[t.userId] = 1;
      }
    }
  }
  console.log(compTasks);
});
