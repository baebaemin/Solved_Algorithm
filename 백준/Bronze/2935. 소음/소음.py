def plus(a, b):
    return a + b

def multiple(a, b):
    return a * b

A = int(input())
calc = input()
B = int(input())

if calc == '+':
    print(plus(A, B))
else:
    print(multiple(A, B))