const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

let N, countN;

const solution = ([num, target]) => {
  const visited = new Array(10001).fill(false);
  const command = new Array(10001).fill("");

  visited[num] = true;
  const queue = [num];

  const checkNum = (next, type, current) => {
    if (!visited[next]) {
      queue.push(next);
      visited[next] = true;
      command[next] = command[current] + type;
    }
  };

  while (queue.length > 0) {
    let current = queue.shift();

    let D = (current * 2) % 10000;
    checkNum(D, "D", current);

    let S = current === 0 ? 9999 : current - 1;
    checkNum(S, "S", current);

    let tempNum = String(current).padStart(4, '0');
    let L = parseInt(tempNum.substring(1) + tempNum[0], 10);
    checkNum(L, "L", current);

    let R = parseInt(tempNum.slice(-1) + tempNum.substring(0, 3), 10);
    checkNum(R, "R", current);

    if (visited[target]) {
      console.log(command[target]);
      return;
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