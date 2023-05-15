def findPrime(num):
    if num <= 1 or (num > 2 and num % 2 == 0):
        return False
    for divnum in range(3, num // 2, 2):
        if not num % divnum:
            return False
    return True

N = int(input())
arr = list(map(int, input().split()))
print(sum([findPrime(n) for n in arr]))