function solution(s) {
    const answer = [];
    const array = s.slice(2, s.length-2).split('},{').map(str => str.split(',').map(Number));
    array.sort((x, y) => x.length - y.length)
    
    const checkSet = new Set(); // 중복 제거용
    array.forEach(item => {
        item.forEach(num => {
            if (!checkSet.has(num)) {
                answer.push(num);
                checkSet.add(num);
            }
        });
    });
    
    return answer;
}