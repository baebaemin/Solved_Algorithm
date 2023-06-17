def solution(name, yearning, photo):
    missing = {name[i]: yearning[i] for i in range(len(name))}
    P = len(photo)
    answer = [0] * P
    for p in range(P):
        rlt = 0
        for ppl in photo[p]:
            try:
                rlt += missing[ppl]
            except:
                continue
        answer[p] = rlt
    return answer