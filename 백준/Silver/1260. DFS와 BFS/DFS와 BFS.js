const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

let N, M, V;
let adj;

const solution = () => {
  let visitedForDfs = new Array(N + 1).fill(false);
  let ansD = dfs(V, visitedForDfs);
  let ansB = bfs();
  console.log(ansD.trim());
  console.log(ansB);
};

const dfs = (V, visitedForDfs) => {
  visitedForDfs[V] = true;
  let ans = V + " ";

  if (adj[V].length > 0) {
    adj[V].forEach(node => {
      if (!visitedForDfs[node]) {
        ans += dfs(node, visitedForDfs);
      }
    });
  }

  return ans;
};

const bfs = () => {
  let ans = "";
  let visited = new Array(N + 1).fill(false);
  let queue = [V];
  visited[V] = true;

  while (queue.length > 0) {
    let node = queue.shift();
    ans += node + " ";

    if (adj[node].length > 0) {
      adj[node].forEach(next => {
        if (!visited[next]) {
          visited[next] = true;
          queue.push(next);
        }
      });
    }
  }
  return ans.trim();
};

readline.on("line", line => {
  if (!N) {
    [N, M, V] = line.split(" ").map(Number);
    adj = Array.from({ length: N + 1 }, () => []);
  } else {
    let [t, u] = line.split(" ").map(Number);
    adj[t].push(u);
    adj[u].push(t);

    if (--M === 0) { 
      // 인접 리스트의 각 리스트를 오름차순으로 정렬
      adj.forEach(nodes => nodes.sort((a, b) => a - b));
      solution();
      readline.close();
    }
  }
}).on("close", () => {
  process.exit();
});
