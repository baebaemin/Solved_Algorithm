T = int(input())
for tc in range(T):
    R, S = input().split()
    print(''.join([ch * int(R) for ch in S]))