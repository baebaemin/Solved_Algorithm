const readline = require("readline");

const solution = (N) => {
    const coins = [500, 100, 50, 10, 5, 1];
    let remains = 1000 - N;
    let cnt = 0;
    for (const coin of coins) {
        cnt += Math.floor(remains / coin);
        remains %= coin;
    }
    console.log(cnt)
}

(async () => {
  let rl = readline.createInterface({ input: process.stdin });

  for await (const line of rl) {
    solution(+line);
    rl.close();
  }

  process.exit();
})();
