def solution(s):
    lst = sorted(list(map(int,s.split())))
    answer = str(lst[0]) + " " + str(lst[-1])
    return answer