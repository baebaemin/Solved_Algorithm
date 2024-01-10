const readline = require("readline");

let N, K;
let coins = [];
let i = 0;

const solution = (coins, N, K) => {
  let cnt = 0;
  for (let j = N - 1; j >= 0; j--) {
    cnt += Math.floor(K / coins[j]);
    K %= coins[j];
  }
  console.log(cnt);
};

(async () => {
  let rl = readline.createInterface({ input: process.stdin });

  for await (const line of rl) {
    if (!N) {
      [N, K] = line.split(" ").map(Number);
      coins = new Array(N).fill(0);
    } else {
      coins[i] = +line;
      i++;
      if (i === N) {
        solution(coins, N, K);
        rl.close();
      }
    }
  }

  process.exit();
})();
