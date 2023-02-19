S = input()
rlt = []
for ascii in range(97, 123):
    try: rlt.append(S.index(chr(ascii)))
    except: rlt.append(-1)
print(' '.join(str(s) for s in rlt))