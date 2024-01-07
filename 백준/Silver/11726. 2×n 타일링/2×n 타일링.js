const N = +require("fs").readFileSync("/dev/stdin").toString();
const dp = Array(N).fill(0);

dp[0] = 1;
dp[1] = 2;

for (let i = 2; i <= N-1; i++) {
  dp[i] = (dp[i - 1] + dp[i - 2]) % 10007;
}

console.log(dp[N - 1]);