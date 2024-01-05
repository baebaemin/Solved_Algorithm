const readline = require("readline");

let N, K;

(async () => {
  let rl = readline.createInterface({ input: process.stdin });

  for await (const line of rl) {
    [N, K] = line.split(" ").map(Number);
    let peoples = Array.from({ length: N }, (v, i) => i + 1);
    let ans = [];
    let next;
    if (K % N - 1 >= 0) {
        next = K % N - 1;
    } else {
        next = K - 1;
    }

    while (peoples.length > 0) {
      ans.push(peoples.splice(next, 1)); // 형변환
      next = (next + K - 1) % (peoples.length);
    }
    console.log('<'+ans.join(', ')+'>');
    rl.close();
  }

  process.exit();
})();
