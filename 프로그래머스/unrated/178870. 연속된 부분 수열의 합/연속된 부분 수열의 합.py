def solution(sequence, k):
    answer = []
    sp = sm = 0
    ep = -1
    length = len(sequence)
    
    while True:
        if sm < k:
            ep += 1
            if ep >= length:
                break
            sm += sequence[ep]
        else:  # 같거나 같은경우 모두
            sm -= sequence[sp]
            if sp >= length:
                break
            sp += 1
        if sm == k:
            answer.append([sp, ep])
    answer.sort(key=lambda x: (x[1]-x[0], x[0]))
    return answer[0]
            