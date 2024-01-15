const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = (N) => {
  let dp = new Array(N + 1).fill(Infinity);
  dp[0] = 0;

  for (let i = 1; i <= N; i++) {
    for (let j = 1; j * j <= i; j++) {
      dp[i] = Math.min(dp[i], dp[i - j * j] + 1);
    }
  }

  console.log(dp[N]);
};

readline
  .on("line", (line) => {
    solution(+line);
    readline.close();
  })
  .on("close", () => {
    process.exit();
  });
