ch_dict = {}
for ch in input().lower():
    try: ch_dict[ch] += 1
    except: ch_dict[ch] = 1

rev_dict = sorted(ch_dict, key=lambda x: ch_dict[x], reverse = True)

try:
    if ch_dict[rev_dict[0]] == ch_dict[rev_dict[1]]:
        print('?')
    else:
        print(rev_dict[0].upper())
except: print(rev_dict[0].upper())