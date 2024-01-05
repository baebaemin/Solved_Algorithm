const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

// MinHeap구현은 https://chamdom.blog/heap-using-js/ 참고
class MinHeap {
  constructor() {
    this.heap = [];
  }

  size() {
    return this.heap.length;
  }

  swap(idx1, idx2) {
    [this.heap[idx1], this.heap[idx2]] = [this.heap[idx2], this.heap[idx1]];
  }

  add(value) {
    this.heap.push(value);
    this.bubbleUp();
  }

  poll() {
    if (this.heap.length === 1) {
      return this.heap.pop();
    }

    const value = this.heap[0];
    this.heap[0] = this.heap.pop();
    this.bubbleDown();
    return value;
  }

  bubbleUp() {
    let index = this.heap.length - 1;
    let parentIdx = Math.floor((index - 1) / 2);
    while (
      this.heap[parentIdx] &&
      this.heap[index][1] < this.heap[parentIdx][1]
    ) {
      this.swap(index, parentIdx);
      index = parentIdx;
      parentIdx = Math.floor((index - 1) / 2);
    }
  }

  bubbleDown() {
    let index = 0;
    let leftIdx = index * 2 + 1;
    let rightIdx = index * 2 + 2;

    while (
      (this.heap[leftIdx] && this.heap[leftIdx][1] < this.heap[index][1]) ||
      (this.heap[rightIdx] && this.heap[rightIdx][1] < this.heap[index][1])
    ) {
      let smallerIdx = leftIdx;
      if (
        this.heap[rightIdx] &&
        this.heap[rightIdx][1] < this.heap[smallerIdx][1]
      ) {
        smallerIdx = rightIdx;
      }

      this.swap(index, smallerIdx);
      index = smallerIdx;
      leftIdx = index * 2 + 1;
      rightIdx = index * 2 + 2;
    }
  }
}

let V, E, K;
let graph;

const dijkstra = (graph, start, V) => {
    const distances = new Array(V + 1).fill(Infinity);
    const minHeap = new MinHeap();
    distances[start] = 0;
    minHeap.add([start, 0]); 

    while (minHeap.size() > 0) {
        const [now, nowWeight] = minHeap.poll(); // 가장 짧은 거리를 가진 노드 선택
        if (distances[now] < nowWeight) continue; // 지금 방문한곳에 지금 경로보다 짧은 경로로 방문했었다면 패스
        
        for (const [next, weight] of graph[now]) { // 다음 갈 곳들
            let nextWeight = nowWeight + weight;
            if (nextWeight < distances[next]) { // 다음 갈 곳에 저장된 경로 거리가 더 크거나 방문한적 없다면
                distances[next] = nextWeight; // 값 줄이기
                minHeap.add([next, nextWeight]);
            }
        }
    }
    return distances;
};

readline
  .on("line", function (line) {
    if (!V) {
      [V, E] = line.split(" ").map(Number);
      graph = Array.from({ length: V + 1 }, () => []);
    } else if (!K) {
      K = +line;
    } else {
      let [u, v, w] = line.split(" ").map(Number);
      graph[u].push([v, w]);
      if (--E === 0) {
        const distances = dijkstra(graph, K, V);
        for (let i = 1; i <= V; i++) {
            console.log(distances[i] !== Infinity ? distances[i] : 'INF')
        }
        readline.close();
      }
    }
  })
  .on("close", function () {
    process.exit();
  });