r = int(input())
for s in range(1, r + 1):
    print(f'%{r}s' % ('*' * s))