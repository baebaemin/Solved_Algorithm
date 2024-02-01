const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = (N) => {
  const dp = new Array(N + 1).fill(1);
  for (let i = 1; i < N + 1; i++) {
    i % 2 === 1 ? dp[i] = (dp[i - 1] * 2 - 1) % 10007 : dp[i] = (dp[i - 1] * 2 + 1) % 10007;
  }
  console.log(dp[N]);
};

readline
  .on("line", function (line) {
    solution(+line);
    readline.close();
  })
  .on("close", function () {
    process.exit();
  });
