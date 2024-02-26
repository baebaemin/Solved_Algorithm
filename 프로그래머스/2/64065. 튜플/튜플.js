function solution(s) {
    const answer = [];
    const array = s.slice(2, s.length-2).split('},{');
    const N = array.length;
    array.sort((x, y) => x.length - y.length)
    
    for (let i = 0; i < N; i++) {
        const miniArray = array[i].split(',');
        
        miniArray.map((elem) => {
            let n = Number(elem)
            if (answer.includes(n) === false) {
                answer.push(n)
            }
        })
    }
    
    return answer;
}