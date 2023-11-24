def solution(keymap, targets):
    # keymap의 키들을 분해해서 dict에 key랑 value로 넣는다
    keyDict = {}
    for keyList in keymap:
        for k in range(len(keyList)): # 한 글자씩
            if keyList[k] not in keyDict.keys() or keyDict[keyList[k]] > k+1: 
                keyDict[keyList[k]] = k+1
    
    rlt = [0] * len(targets)
    
    for t in range(len(targets)):
        for ch in targets[t]:
            try:
                rlt[t] += keyDict[ch]
            except: 
                rlt[t] = -1
                break
    
    print(rlt, keyDict)
    return rlt