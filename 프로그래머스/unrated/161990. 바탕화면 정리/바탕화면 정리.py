def find(arr):
    row = len(arr)
    foundSp = foundEp = False
    for i in range(row): 
        if '#' in arr[i] and not foundSp:
            foundSp = True
            sp = i
        if '#' in arr[(i+1)*-1] and not foundEp:
            foundEp = True
            ep = row-i
        if foundSp and foundEp:
            break
    return sp, ep

def solution(wallpaper):
    sr, er = find(wallpaper)
    sc, ec = find(list(zip(*wallpaper)))
    answer = [sr, sc, er, ec]
    return answer