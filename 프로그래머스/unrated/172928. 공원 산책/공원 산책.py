def solution(park, routes):
    dir_dict = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}
    r = c = 0
    for y in range(len(park)):
        for x in range(len(park[y])):
            if park[y][x] == 'S':
                (r, c) = (y, x)
                break

    for route in routes:  # 명령
        dr, dc = dir_dict[route[0]] # 방향
        moves = int(route[2])   # 얼마나 가야 하는지
        
        # 범위 check
        if 0 <= r + dr*moves < len(park) and 0 <= c + dc*moves < len(park[0]):  # 범위내일때
            (nr, nc) = (r, c)
            for _ in range(moves):  # 가야하는만큼 반복
                nr += dr
                nc += dc
                if park[nr][nc] == 'X':
                    break
            else:
                (r, c) = (nr, nc)
                
    answer = [r, c] 
    return answer