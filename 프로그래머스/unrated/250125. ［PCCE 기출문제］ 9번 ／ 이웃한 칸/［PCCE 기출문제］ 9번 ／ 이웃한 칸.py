def solution(board, h, w):
    count = 0
    
    try: 
        if board[h][w] == board[h-1][w] and h-1 != -1:
            count += 1
    except: pass

    try: 
        if board[h][w] == board[h+1][w]:
            count += 1
    except: pass
    try: 
        if board[h][w] == board[h][w-1] and w-1 != -1:
            count += 1
    except: pass
    try: 
        if board[h][w] == board[h][w+1]:
            count += 1
    except: pass
            
    return count


["blue", "red", "orange", "red"], 
["red", "red", "blue", "orange"], 
["blue", "orange", "red", "red"], 
["orange", "orange", "red", "blue"]