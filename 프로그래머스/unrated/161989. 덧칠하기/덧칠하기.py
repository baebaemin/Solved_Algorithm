def solution(n, m, section):
    answer = 1
    sp = section[0]
    for np in section:
        if np - sp >= m:
            answer += 1
            sp = np
    return answer