#!/usr/bin/env node
/*
 * This script computes the number of tasks
 * completed by user ID.
 */

const request = require('request');

const url = process.argv[2];
const tasksCompleted = {};

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  const data = JSON.parse(body);
  for (const element of data) {
    if (!(element.userId in tasksCompleted)) {
      if (element.completed === true) {
        tasksCompleted[element.userId] = 1;
      }
    } else {
      if (element.completed === true) {
        tasksCompleted[element.userId] = tasksCompleted[element.userId] + 1;
      }
    }
  }
  console.log(tasksCompleted);
});
