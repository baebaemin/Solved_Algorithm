const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

let TC, countTC;

const solution = (N) => {
  let DP = [0, 1, 1, 1, 2];
  for (let i = 5; i < N + 1; i++) {
    DP.push(DP[i - 1] + DP[i - 5]);
  }
  console.log(DP[N]);
};

readline
  .on("line", (line) => {
    if (!TC) {
      TC = +line;
      countTC = TC;
    } else {
      solution(+line);
      countTC--;
      if (!countTC) {
        readline.close();
      }
    }
  })
  .on("close", () => {
    process.exit();
  });
