_, X = map(int, input().split())
lst_A = list(map(int, input().split()))
print(' '.join(str(n) for n in lst_A if n < X))