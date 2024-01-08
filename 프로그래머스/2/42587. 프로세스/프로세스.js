function solution(priorities, location) {
    let enumPriorities = priorities.map((val, idx) => [idx, val])  // enumerate
    let queue = [];
    
    while (enumPriorities.length > 0) {
        let curV = enumPriorities.shift()
        // 우선순위가 더 높은 프로세스가 없다면(false) queue에 push
        enumPriorities.find(val => val[1] > curV[1]) ? enumPriorities.push(curV) : queue.push(curV)
    }
    
    return queue.findIndex(val => val[0] === location) + 1;
}