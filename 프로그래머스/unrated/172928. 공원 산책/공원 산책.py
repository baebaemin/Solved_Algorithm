def solution(park, routes):
    dir_dict = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}
    
    r = c = 0
    for y in range(len(park)):
        for x in range(len(park[y])):
            if park[y][x] == 'S':
                r, c = y, x
                break

    for route in routes:
        dr, dc = dir_dict[route[0]]
        moves = int(route[2])
        
        if 0 <= r + dr*moves < len(park) and 0 <= c + dc*moves < len(park[0]):
            nr = r + dr*moves
            nc = c + dc*moves
            if all(park[r+i*dr][c+i*dc] != 'X' for i in range(1, moves+1)):
                r, c = nr, nc
                
    answer = [r, c] 
    return answer