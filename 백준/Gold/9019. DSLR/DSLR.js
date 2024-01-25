const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

let N, countN;

const solution = ([num, target]) => {
  const visited = new Array(10001).fill(null);
  visited[num] = "";
  const queue = [num];

  while (queue.length > 0) {
    let current = queue.shift();

    if (current === target) {
      console.log(visited[current]);
      return;
    }

    let D = (current * 2) % 10000;
    if (visited[D] === null) {
      queue.push(D);
      visited[D] = visited[current] + "D";
    }

    let S = current === 0 ? 9999 : current - 1;
    if (visited[S] === null) {
      queue.push(S);
      visited[S] = visited[current] + "S";
    }

    let L = (current % 1000) * 10 + Math.floor(current / 1000);
    if (visited[L] === null) {
      queue.push(L);
      visited[L] = visited[current] + "L";
    }

    let R = (current % 10) * 1000 + Math.floor(current / 10);
    if (visited[R] === null) {
      queue.push(R);
      visited[R] = visited[current] + "R";
    }
  }
};

readline
  .on("line", (line) => {
    if (!N) {
      N = +line;
      countN = N;
    } else {
      solution(line.split(" ").map(Number));
      countN--;
      if (!countN) {
        readline.close();
      }
    }
  })
  .on("close", () => {
    process.exit();
  });
