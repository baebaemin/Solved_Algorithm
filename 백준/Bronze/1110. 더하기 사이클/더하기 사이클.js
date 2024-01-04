const N = +require("fs").readFileSync("/dev/stdin").toString();

let num = N;
let cnt = 0;
let sum;

while (true) {
    sum = Math.floor(num / 10) + (num % 10); // 각 자릿수를 더함
    num = (num % 10) * 10 + (sum % 10); // 새로운 수 생성
    cnt++;
    if (num === N) {
        break;
    }
}
console.log(cnt);