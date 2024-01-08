function solution(priorities, location) {
    let enumPriorities = priorities.map((val, idx) => [idx, val])  
    let rlt = [];
    
    while (enumPriorities.length > 0) {
        let curV = enumPriorities.shift()
        
        // [1] 뽑은 값이 지금 있는 애들 중에 가장 우선순위가 높지 않다면 -> 같은 값이면?
        if (enumPriorities.find(val => val[1] > curV[1])) { // true라면? 가장 높지 않음
            enumPriorities.push(curV)
        } else {
            rlt.push(curV)
        }
    }
    
    // console.log(rlt)
    // console.log()
    // var answer = 0;
    return rlt.findIndex(val => val[0] === location) + 1;
}