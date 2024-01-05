let fs = require('fs');
let [N,K] = fs.readFileSync('/dev/stdin').toString().trim().split(' ').map(Number);

const peoples = Array.from({ length: N }, (_, i) => i + 1);
const ans = [];
let next = K - 1;

while (peoples.length > 0) {
  ans.push(peoples.splice(next, 1));
  next = (next + K - 1) % peoples.length;
}
console.log(`<${ans.join(', ')}>`);