function solution(clothes) {
    const clothDict = {};
    for ([cloth, catogory] of clothes) {
        clothDict[catogory] >= 1 ? clothDict[catogory] += 1 : clothDict[catogory] = 1;
    }
    
    let comb = 1;
    const categories = Object.keys(clothDict);
    for (category of categories) {
        comb *= (clothDict[category] + 1)
    }
    return comb - 1;
}