def solution(park, routes):
    dir_dict = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}
    
    # 출발 지점 탐색
    r = c = 0
    for y in range(len(park)):
        for x in range(len(park[y])):
            if park[y][x] == 'S':
                r, c = y, x
                break
                
    for route in routes:    # 각 명령문별 방향 및 이동거리 추출
        dr, dc = dir_dict[route[0]]
        moves = int(route[2])
        
        # park의 범위를 벗어나지 않는지 검사
        if 0 <= r + dr*moves < len(park) and 0 <= c + dc*moves < len(park[0]):
            # 벗어나지 않는다면, 명령문별 도착지 좌표 설정
            nr = r + dr*moves
            nc = c + dc*moves
            # 도착지로 이동 중 장애물을 만나지 않는지 검사
            if all(park[r+i*dr][c+i*dc] != 'X' for i in range(1, moves+1)):
                r, c = nr, nc
                
    answer = [r, c] 
    return answer