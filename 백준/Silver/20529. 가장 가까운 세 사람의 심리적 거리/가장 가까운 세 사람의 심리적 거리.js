const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = (P, mbtiLst) => {
  if (P > 32) {
    console.log(0);
  } else {
    let minV = 12;
    
    for (let i = 0; i < P - 2; i++) {
      for (let j = i + 1; j < P - 1; j++) {
        for (let k = j + 1; k < P; k++) {
          const one = mbtiLst[i];
          const two = mbtiLst[j];
          const three = mbtiLst[k];
          let cnt = 0;
          // 1과 2 비교
          for (let m = 0; m < 4; m++) {
            if (one[m] !== two[m]) cnt++;
            if (one[m] !== three[m]) cnt++;
            if (two[m] !== three[m]) cnt++;
          }
          minV = Math.min(minV, cnt);
        }
      }
    }
    console.log(minV);
  }
};

let N, P;
let currentLine = 0;

readline
  .on("line", (line) => {
    if (!currentLine) {
      N = +line;
    } else if (currentLine % 2) {
      P = +line;
    } else {
      solution(P, line.split(" "));
    }
    if (++currentLine === N * 2 + 1) {
      readline.close();
    }
  })
  .on("close", () => {
    process.exit();
  });
