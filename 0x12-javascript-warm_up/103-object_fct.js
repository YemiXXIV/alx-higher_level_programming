#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
// my code starts here
myObject.incr = () => {
  myObject.value++;
};
// my code ends here
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
