const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

let tc, N, AC;
let currentline = 0;
let stage = 0;

const solution = (AC, N, arr) => {
  let dir = 1;
  let si = 0;
  let ei = N;
  let countD = 0;

  for (let i = 0; i < AC.length; i++) {
    if (AC[i] === "R") {
      dir *= -1;
    } else {
      countD++;
      if (countD > N) { 
        console.log('error'); 
        return
      } else {
        dir === 1 ? si++ : ei--;
      }
    } 
  }
  
  dir === 1 ? console.log('[' + arr.slice(si, ei).join(',') + ']') : console.log('[' + arr.reverse().slice(N-ei, N-si).join(',') + ']');
};

readline
  .on("line", (line) => {
    if (!currentline) {
      tc = +line;
      currentline++;
    } else {
      if (stage === 0) {
        AC = line;
        stage = 1;
      } else if (stage === 1) {
        N = +line;
        stage = 2;
      } else {
        solution(AC, N, JSON.parse(line));
        stage = 0;
        currentline++;
        if (currentline > tc) {
          readline.close();
        }
      }
    }
  })
  .on("close", () => {
    process.exit();
  });
