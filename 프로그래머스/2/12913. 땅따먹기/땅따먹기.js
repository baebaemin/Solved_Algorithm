function solution(land) {
    const N = land.length
    
    for (let i = 0; i < N - 1; i++) {
        for (let j = 0; j < 4; j++) {
            let maxV = 0;
            for (let k = 0; k < 4; k++) {
                if (j === k) continue;
                maxV = Math.max(maxV, land[i][k] + land[i+1][j])
            }
            land[i+1][j] = maxV;
        }
    }
    return Math.max(...land[N - 1])
}