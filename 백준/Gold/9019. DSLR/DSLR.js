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

  while (queue.length > 0) {
    let current = queue.shift();

    // D 연산
    let D = (current * 2) % 10000;
    if (!visited[D]) {
      queue.push(D);
      visited[D] = true;
      command[D] = command[current] + "D";
    }

    // S 연산
    let S = current === 0 ? 9999 : current - 1;
    if (!visited[S]) {
      queue.push(S);
      visited[S] = true;
      command[S] = command[current] + "S";
    }

    // L 연산 (왼쪽으로 회전)
    let L = parseInt(String(current).padStart(4, '0').substring(1) + String(current).padStart(4, '0')[0], 10);
    if (!visited[L]) {
      queue.push(L);
      visited[L] = true;
      command[L] = command[current] + "L";
    }

    // R 연산 (오른쪽으로 회전)
    let R = parseInt(String(current).padStart(4, '0').slice(-1) + String(current).padStart(4, '0').substring(0, 3), 10);
    if (!visited[R]) {
      queue.push(R);
      visited[R] = true;
      command[R] = command[current] + "R";
    }

    // 목표 도달 시
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
