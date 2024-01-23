// 우선 사람을 오름차순으로 정렬
function solution(people, limit) { 
    people.sort((a, b) => a - b);
    let answer = 0; 
    let lightIdx = 0
    let heavyIdx = people.length - 1;
    
    while (lightIdx <= heavyIdx) {
        if (people[lightIdx] + people[heavyIdx] <= limit) {
            lightIdx++;
        }
        heavyIdx--; // 무거운 사람은 1명이라도 늘 태우기
        answer++;
    }
        
    return answer;
}