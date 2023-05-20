while True:
    Q = []
    line = input()
    if line == '.':
        break

    for ch in line:
        if ch in ['(', '[']:
            Q.append(ch)
        elif ch == ')':
            if Q and Q[-1] == '(':
                Q.pop()
            else:
                Q.append(')')
                break
        elif ch == ']':
            if Q and Q[-1] == '[':
                Q.pop()
            else:
                Q.append(']')
                break

    print('no' if Q else 'yes')