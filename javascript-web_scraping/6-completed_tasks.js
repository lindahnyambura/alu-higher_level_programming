#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    return console.log(error);
  }
  const toDos = JSON.parse(body);

  const completedTasks = {};
  for (const item of toDos) {
    if (item.completed) {
      if (item.userId in completedTasks) {
        completedTasks[item.userId] += 1;
      } else {
        completedTasks[item.userId] = 1;
      }
    }
  }

// sort keys in ascending order
  const sortedTasks = Object.keys(completedTasks)
    .sort((a, b) => a - b)
    .reduce((acc, key) => {
      acc[key] = completedTasks[key];
      return acc;
    }, {});

  if (Object.keys(sortedTasks).length === 0) {
    console.log(JSON.stringify({}));
  } else {
    console.log(sortedTasks);
  }
});
