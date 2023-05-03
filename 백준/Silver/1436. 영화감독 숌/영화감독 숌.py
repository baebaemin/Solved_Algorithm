N = int(input())
start = 665
cnt = 0
while cnt != N:
    start += 1
    if '666' in str(start):
        cnt += 1
print(start)