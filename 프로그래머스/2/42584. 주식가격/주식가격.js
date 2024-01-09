function solution(prices) {
    const N = prices.length
    let answer = new Array(N).fill(0);
    // 여기에 cnt를 선언하는게 더 낫나?
    let cnt = 0;
    
    for (let i = 0; i < N - 1; i++) {
        cnt = 0;
        for (let j = i + 1; j < N; j++) {
            cnt++;
            if (prices[i] > prices[j]) { break }
        } 
        answer[i] = cnt;
    }
    return answer;
}