T = int(input())
scores = list(map(int, input().split()))
print(sum(list(s / max(scores) * 100 for s in scores)) / T)