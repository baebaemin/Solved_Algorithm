// 정현아...
function solution(want, number, discount) {
    const N = discount.length
    let answer = 0;
    const jeonghyeonList = {};
    for (let i = 0; i < want.length; i++) {
        jeonghyeonList[want[i]] = number[i];
    }
    
    let cntList = {}
    
    // discount 길이가 10개 이하일 떄
    if (N < 11) { 
        discount.forEach((item) => {
            cntList[item] ? cntList[item] = cntList[item] + 1 : cntList[item] = 1;
        });
        let check = 0;
        want.forEach((wishItem) => {
            if (cntList[wishItem] && cntList[wishItem] >= jeonghyeonList[wishItem]) {
                check++;
            }
        })
        if (check === want.length) {
            answer++;
        }
    } else { // 10개 이상이면?
        let startIdx = 0;
        let endIdx = 10; 
        
        while (endIdx < N + 1) {
            for (let j = startIdx; j < endIdx; j++) {
                let item = discount[j];
                cntList[item] ? cntList[item] = cntList[item] + 1 : cntList[item] = 1;
            }
            
            // 검토
            let check = 0;
            want.forEach((wishItem) => {
                if (cntList[wishItem] && cntList[wishItem] >= jeonghyeonList[wishItem]) {
                    check++;
                }
            })
            if (check === want.length) {
                answer++;
            }
            
            startIdx++;
            endIdx++;
            cntList = {}
        }
    }
    return answer;
}