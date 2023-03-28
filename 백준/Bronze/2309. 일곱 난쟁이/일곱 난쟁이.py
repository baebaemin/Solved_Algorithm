def nCr(n, r, s):   # n개에서 r개를 고르는 조합, s = 선택할 수 있는 구간의 시작
    if r == 0:
        if sum(heights) == 100:
            for gnome in heights:
                print(gnome)
            exit()
    else:
        for i in range(s, n-r+1):
            heights[r-1] = gnomes[i]
            nCr(n, r-1, i+1)

gnomes = [int(input()) for _ in range(9)]
gnomes.sort(reverse=True)
heights = [0] * 7
nCr(9, 7, 0)