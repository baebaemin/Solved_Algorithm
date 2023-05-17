import sys; input = sys.stdin.readline

N = int(input())
numDict = {}
arrN = list(map(int, input().split()))
for n in arrN:
    try: numDict[n] += 1
    except: numDict[n] = 1

M = int(input())
arrM = list(map(int, input().split()))
for m in arrM:
    try: print(numDict[m])
    except: print(0)