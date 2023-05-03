const N = require('fs').readFileSync('/dev/stdin').toString().trim()
let cnt = 0
let start = 665

while (cnt != N){
    start ++
    if (String(start).includes('666')){
        cnt ++
    }
}
console.log(start)