const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

const BFS = (n, graph) => {
  let visited = new Array(N).fill(0);
  let queue = [n];

  while (queue.length > 0) {
    let now = queue.shift();
    graph[now].forEach((next) => {
      if (visited[next] === 0) {
        visited[next] = 1;
        queue.push(next);
      }
    });
  }
  console.log(...visited);
};

const solution = (adj) => {
  let graph = new Array(N).fill().map(() => []);
  adj.forEach((line, idx) => {
    for (let i = 0; i < N; i++) {
      if (line[i] !== 0) {
        graph[idx].push(i);
      }
    }
  });
  for (let n = 0; n < N; n++) {
    BFS(n, graph);
  }
};

let N, countN;
let adj = [];

readline
  .on("line", (line) => {
    if (!N) {
      N = +line;
      countN = N;
    } else {
      adj.push(line.split(" ").map(Number));
      countN--;
      if (!countN) {
        solution(adj);
        readline.close();
      }
    }
  })
  .on("close", () => {
    process.exit();
  });
