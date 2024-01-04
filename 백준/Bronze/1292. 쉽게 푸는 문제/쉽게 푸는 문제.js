const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
})

const solution = (S, E) => {
    let questions = new Array(E).fill(0)
    let num = 0;
    for (i = 0; i < E; i++) {
        num ++;     // 1씩 증가하는 문제
        let numCnt = num;
        while (numCnt !== 0) {
            questions[i] = num
            i ++;
            numCnt --;
        }
        i --;
    }
    const ans = questions.slice(S-1, E).reduce((val, sm) => val + sm, 0)
    return ans
}

readline.on('line', function(line) {
    const [S, E] = line.split(' ').map(Number);
    console.log(solution(S, E));
    readline.close();
}).on('close', function() {
    process.exit();
})