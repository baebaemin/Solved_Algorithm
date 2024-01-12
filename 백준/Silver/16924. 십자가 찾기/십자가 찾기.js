const fs = require("fs");
const input = fs.readFileSync("./dev/stdin").toString().trim().split("\n");
const [N, M] = input[0].split(" ").map(Number);
let grid = input.splice(1).map((line) => line.split(""));
const crosses = [];

for (let i = 1; i < N - 1; i++) {
  for (let j = 1; j < M - 1; j++) {
    if (grid[i][j] === "*" && grid[i - 1][j] === "*" && grid[i + 1][j] === "*" && grid[i][j - 1] === "*" && grid[i][j + 1] === "*") {
      // 최초의 size 1짜리 십자가를 찾았을 때
      let size = 1;
      
      while (
        i - size >= 0 &&
        i + size < N &&
        j - size >= 0 &&
        j + size < M &&
        grid[i - size][j] === "*" &&
        grid[i + size][j] === "*" &&
        grid[i][j - size] === "*" &&
        grid[i][j + size] === "*"
      ) {
        size++; // 다음 사이즈 갱신
      }
      crosses.push([i + 1, j + 1, size - 1]);
    }
  }
}

crosses.forEach((val) => {
  let x = val[0];
  let y = val[1];
  let s = val[2];
  grid[x - 1][y - 1] = "."; // 가운데 지우기
  for (let i = 1; i < s + 1; i++) {
    grid[x - 1 + 1 * i][y - 1] = ".";
    grid[x - 1 - 1 * i][y - 1] = ".";
    grid[x - 1][y - 1 + 1 * i] = ".";
    grid[x - 1][y - 1 - 1 * i] = ".";
  }
});

for (let i = 0; i < N; i++) {
  for (let j = 0; j < M; j++) {
    if (grid[i][j] != ".") {
      console.log(-1);
      return;
    }
  }
}

console.log(crosses.length);
crosses.forEach((el, idx) => console.log(...el));
