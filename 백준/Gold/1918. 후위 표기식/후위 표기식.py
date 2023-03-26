icp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3, ')': 0}  # 스택 밖에 있을 때
isp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0, ')': 0}  # 스택 안에 있을 때

lst = input()
postfix = ''
S = []

for ch in lst:
    if ch in icp:
        if ch == ')':
            while S[-1] != '(':
                postfix += S.pop()
            S.pop()
        else:
            while S and icp[ch] <= isp[S[-1]]:
                postfix += S.pop()
            S.append(ch)
    else:
        postfix += ch
while S:
    postfix += S.pop()

print(postfix)