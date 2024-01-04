const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
})

const solution = (N, path) => {
    let maxV = 0
    for (i = 0; i < N - 1; i++) {
        let startNum = path[i]    // 기준점 리셋
        while (i < N - 1 && path[i] < path[i+1]) { // 지금 숫자가 기준점보다 높으면
            i++
        }
        maxV = Math.max(path[i] - startNum, maxV)
    }
    return maxV
}

let N = 0;

readline.on('line', function(line) {
    if (!N) {
        N = +line;
    } else {
        const path = line.split(' ').map(Number);
        const ans = solution(N, path);
        console.log(ans);
        readline.close();
    }
}).on('close', function() {
    process.exit();
})
