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

  for (const userId in completedTasks) {
    console.log(`${userId} : ${completedTasks[userId]}`);
  }
});
