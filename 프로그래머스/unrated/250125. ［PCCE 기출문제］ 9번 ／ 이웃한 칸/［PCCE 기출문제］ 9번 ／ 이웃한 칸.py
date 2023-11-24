def solution(board, h, w):
    length = len(board)
    dh, dw = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    cnt = 0
    for i in range(4):
        check_dh= h+dh[i]
        check_dw = w+dw[i]
        if 0 <= check_dh < length and 0 <= check_dw < length and board[check_dh][check_dw] == board[h][w]:
            cnt += 1

    return cnt