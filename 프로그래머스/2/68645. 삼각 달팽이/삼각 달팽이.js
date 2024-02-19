function solution(n) {
    
    let total = 1; 
    const answer = [];
    for (let i = 1; i < n+1; i++) {
        answer.push(new Array(i).fill(0))
        total += i
    }
    let r = 0;
    let c = 0;
    let num = 1;
    let dir = 'down';
    
    for (let j = 0; j < total+n; j++) {
        // 범위 안이고 num 추가
        if (0 <= r && 0 <= c && r < n && c < n && answer[r][c] === 0) {
            answer[r][c] = num
            num++
            if (dir === 'down') {
                r++
            } else if (dir === 'right') {
                c++
            } else if (dir === 'up') {
                r--
                c--
            }
        // 범위 벗어났을때
        } else if (dir === 'down') {
            dir = 'right'
            r--
            c++
        } else if (dir === 'right') {
            dir = 'up'
            r--
            c -= 2
        } else if (dir === 'up') {
            dir = 'down'
            r += 2
            c++
        }        
        
    }
    
    let rlt = [...answer]
    return answer.flat();
}