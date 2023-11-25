answer = 0
def dfs(k, cnt, dungeons, check):
    global answer
    answer = max(answer, cnt)
    if k <= 0:
        return
    
    for i, dungeon in enumerate(dungeons):
        if not check[i] and k >= dungeon[0]:
            check[i] = 1
            dfs(k-dungeon[1], cnt + 1, dungeons, check)
            check[i] = 0
        
def solution(k, dungeons):
    global answer
    check = [0] * len(dungeons)
    dfs(k, 0, dungeons, check)
    return answer