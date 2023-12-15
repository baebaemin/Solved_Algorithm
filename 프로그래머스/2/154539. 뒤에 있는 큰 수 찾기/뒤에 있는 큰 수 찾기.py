from collections import deque 

def solution(numbers):
    N = len(numbers)
    rlt = [-1] * N
    stack = deque()
    
    for i in range(N):
        # 현재 숫자가 stack에 쌓인 idx의 수보다 크다면 현재 숫자 = 뒤에 있는 큰 수
        # while문에 걸리지 않으면 -1
        while stack and numbers[i] > numbers[stack[-1]]:
            bigger_idx = stack.pop()        # 인덱스 빼내기
            rlt[bigger_idx] = numbers[i]    # 뒤에 있는 큰 수 적어주기
        stack.append(i)
            
    return rlt