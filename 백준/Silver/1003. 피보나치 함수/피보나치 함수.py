T = int(input())

for _ in range(T):
    zero, one = 1, 0
    for i in range(int(input())):
        zero, one = one, zero + one
    print(zero, one)