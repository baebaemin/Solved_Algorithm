const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

let N, countN;
let adj;

const solution = (adj) => {
  const ans = bfs(adj);
  console.log(ans.join("\n"));
};

const bfs = (adj) => {
  let visited = new Array(N + 1).fill(false);
  let queue = [1];
  visited[1] = 0;

  while (queue.length > 0) {
    let node = queue.pop();
    for (const next of adj[node]) {
      if (visited[next] === false) {
        queue.push(next);
        visited[next] = node;
      }
    }
  }
  return visited.slice(2, N + 1);
};

readline
  .on("line", function (line) {
    if (!N) {
      N = +line;
      countN = N - 1; // N-1줄만 입력 들어올 예정
      adj = Array.from({ length: N + 1 }, () => []);
    } else {
      let [t, u] = line.split(" ").map(Number);
      adj[t].push(u);
      adj[u].push(t);
      if (--countN === 0) {
        solution(adj);
        readline.close();
      }
    }
  })
  .on("close", function () {
    process.exit();
  });