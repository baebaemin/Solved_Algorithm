const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

let N, countN;
let stairs = [];

const solution = (stairs, N) => {
  const dp = new Array(N);
  dp[0] = stairs[0]; // 한 칸일 때
  dp[1] = stairs[0] + stairs[1]; // 두 칸일 때
  dp[2] = stairs[2] + Math.max(stairs[0], stairs[1]); // 세 칸일 때 마지막 칸은 무조건 밟음

  for (let i = 3; i < N; i++) {
    // 네 번째 칸일때부터
    dp[i] = stairs[i] + Math.max(dp[i - 3] + stairs[i - 1], dp[i - 2]);
  }

  return dp[N - 1];
};

readline
  .on("line", (line) => {
    if (!N) {
      N = +line;
      countN = N;
    } else {
      stairs.push(+line);
      countN--;
      if (!countN) {
        console.log(solution(stairs, N));
        readline.close();
      }
    }
  })
  .on("close", () => {
    process.exit();
  });
