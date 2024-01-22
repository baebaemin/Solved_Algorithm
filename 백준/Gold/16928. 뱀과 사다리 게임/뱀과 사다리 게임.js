const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

const BFS = (snakesAndLadders) => {
  const visited = new Array(101).fill(false);
  visited[1] = 1;

  let queue = [1];
  while (queue.length > 0) {
    let current = queue.shift();

    for (let i = 1; i <= 6; i++) {
      let next = current + i;
      if (next > 100) continue;

      if (snakesAndLadders[next] !== undefined) {
        next = snakesAndLadders[next];
      }

      if (!visited[next] || visited[next] > visited[current] + 1) {
        visited[next] = visited[current] + 1;
        queue.push(next);
      }
    }
  }
  console.log(visited[100] - 1);
};

let N, M, countNM;
let snakesToLadders = {};

readline
  .on("line", (line) => {
    if (!N) {
      [N, M] = line.split(" ").map(Number);
      countNM = N + M;
    } else if (countNM > 0) {
      let [u, v] = line.split(" ").map(Number);
      snakesToLadders[u] = v;
      countNM--;
      if (!countNM) {
        BFS(snakesToLadders);
        readline.close();
      }
    }
  })
  .on("close", () => {
    process.exit();
  });
