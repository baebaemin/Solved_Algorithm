const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

let N, M, countN, countM;
let processingN = true;
let passwordDict = {};

readline
  .on("line", (line) => {
    if (!N) {
      [N, M] = line.split(" ").map(Number);
      countN = N;
      countM = M;
    } else if (processingN) {
      const [site, pw] = line.split(" ");
      passwordDict[site] = pw;
      countN--;
      if (!countN) {
        processingN = false;
      }
    } else {
      console.log(passwordDict[line]);
      countM--;
      if (!countM) {
        readline.close();
      }
    }
  })
  .on("close", () => {
    process.exit();
  });
