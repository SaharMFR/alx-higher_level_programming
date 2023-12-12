#!/usr/bin/node

if (isNaN(process.argv[2])) console.log('Missing size');
else {
  const x = parseInt(process.argv[2]);
  for (let i = 0; i < x; i++) {
    let y = 0;
    let myVar = '';

    while (y < x) {
      myVar = myVar + 'X';
      y++;
    }
    console.log(myVar);
  }
}
