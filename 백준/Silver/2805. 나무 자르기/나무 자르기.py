N, M = map(int, input().split())
trees = list(map(int, input().split()))

minV, maxV = 1, max(trees)
while minV <= maxV:
    midV = (minV + maxV) // 2
    cutted = 0
    for tree in trees:
        cutted += max(tree-midV, 0)

    # 자른게 목표값보다 작다면 절단기 높이를 낮춰야 함
    if cutted < M:
        maxV = midV - 1
    else:
        minV = midV + 1

print(maxV)