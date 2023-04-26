while True:
    line = input()
    if line == '0':
        break
    else:
        half_l = half_r = len(line) // 2
        if len(line) % 2:
            half_r += 1
        R_line = ''.join(reversed(list(line[half_r:])))
        if line[:half_l] == R_line: print('yes')
        else: print('no')