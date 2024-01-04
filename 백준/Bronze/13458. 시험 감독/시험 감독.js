const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
});

const solution = (N, A, B, C) => {
    let cnt = 0;
    A.forEach(room => {
        room -= B;  // 총감독 1명 배치
        cnt ++;
        if (room > 0) { // 감독 부족
            cnt += Math.ceil(room / C) 
        } 
    });
    return cnt
}

let N = 0;
let A = [];

readline.on('line', function(line) {
    if (!N) {
        N = +line;
    } else if (A.length === 0) {
        A = line.split(' ').map(Number);
    } else {
        let [B, C] = line.split(' ').map(Number);
        const ans = solution(N, A, B, C);
        console.log(ans)
        readline.close();
    }

}).on('close', function() {
    process.exit();
})