
def preorder(n):
    if n != '.': # 완전이진이 아니므로
        print(n, end='')
        preorder(P[n][0])  # 자식을 부모 key로 level down
        preorder(P[n][1])

def inorder(n):
    if n != '.':
        inorder(P[n][0])
        print(n, end='')
        inorder(P[n][1])

def postorder(n):
    if n != '.':
        postorder(P[n][0])
        postorder(P[n][1])
        print(n, end='')

N = int(input())  # 노드의 개수
P = {}

for i in range(1, N + 1):
    line = list(input().split())
    P[line[0]] = [line[1], line[2]]

preorder('A')  # 첫번째 부모부터
print()
inorder('A')
print()
postorder('A')