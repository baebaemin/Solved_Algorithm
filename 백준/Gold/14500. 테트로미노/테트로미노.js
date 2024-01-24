const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

let N, M, countN;
let board = [];

const shapeAdir = [
  [-1, 0],
  [-1, 1],
  [-1, 2],
  [0, 3],
  [1, 0],
  [1, 1],
  [1, 2],
];

const shapeBdir = [
  [0, -1],
  [1, -1],
  [2, -1],
  [3, 0],
  [0, 1],
  [1, 1],
  [2, 1],
];
const shapeCdirPlus = [
  [-1, 0],
  [-1, 1],
  [1, -1],
  [1, 2],
];
const shapeCdirMinus = [
  [1, 0],
  [1, 1],
  [1, 1],
  [1, 0],
];

const checkShapeA = (r, c, smA) => {
  let maxV = smA;
  for (let [dr, dc] of shapeAdir) {
    let nr = dr + r,
      nc = dc + c;
    if (nr >= 0 && nc >= 0 && nr < N && nc < M) {
      maxV = Math.max(maxV, smA + board[nr][nc]);
    }
  }
  return maxV;
};

const checkShapeB = (r, c, smB) => {
  let maxV = smB;
  for (let [dr, dc] of shapeBdir) {
    let nr = dr + r,
      nc = dc + c;
    if (nr >= 0 && nc >= 0 && nr < N && nc < M) {
      maxV = Math.max(maxV, smB + board[nr][nc]);
    }
  }
  return maxV;
};

const checkShapeC = (r, c, smC) => {
  let maxV = smC;
  for (let i = 0; i < 4; i++) {
    let [dr, dc] = shapeCdirPlus[i];
    let nr = dr + r,
      nc = dc + c;
    if (nr >= 0 && nc >= 0 && nr < N && nc < M) {
      let [mr, mc] = shapeCdirMinus[i];
      maxV = Math.max(maxV, smC + board[nr][nc] - board[r + mr][c + mc]);
    }
  }
  return maxV;
};

const solution = (board) => {
  let maxV = 0;

  for (let r = 0; r < N; r++) {
    for (let c = 0; c < M; c++) {
      let maxA = 0, maxB = 0, maxC = 0;

      if (c + 2 < M) {
        let smA = board[r][c] + board[r][c + 1] + board[r][c + 2];
        maxA = checkShapeA(r, c, smA);
      }
      if (r + 2 < N) {
        let smB = board[r][c] + board[r + 1][c] + board[r + 2][c];
        maxB = checkShapeB(r, c, smB);
      }
      if (r + 1 < N && c + 1 < M) {
        let smC = board[r][c] + board[r + 1][c] + board[r][c + 1] + board[r + 1][c + 1];
        maxC = checkShapeC(r, c, smC);
      }
      maxV = Math.max(maxV, maxA, maxB, maxC);
    }
  }
  console.log(maxV);
};

readline
  .on("line", (line) => {
    if (!N) {
      [N, M] = line.split(" ").map(Number);
      countN = N;
    } else {
      board.push(line.split(" ").map(Number));
      countN--;
      if (!countN) {
        solution(board);
        readline.close();
      }
    }
  })
  .on("close", () => {
    process.exit();
  });
