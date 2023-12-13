def solution(picks, minerals):
    # 광물 리스트를 5개 단위로 분할하기 위함
    minerals.extend([''] * (5 - len(minerals) % 5))
    
    # 5개 단위로 분할한 섹션별 광물 갯수 배열에 저장
    mineral_counts = []
    for i in range(sum(picks)):
        section = minerals[i*5:i*5+5]
        mineral_counts.append([section.count('diamond'), section.count('iron'), section.count('stone')])

    # 다이아몬드, 철 갯수 기준으로 내림차순 정렬
    mineral_counts.sort(key=lambda x: (x[0], x[1]), reverse=True)
    
    tired = 0
    for pick_type, pick_cnt in enumerate(picks):    # 종류(idx)랑 개수
        for _ in range(pick_cnt):                   # 곡괭이 수만큼 반복
            if mineral_counts:
                section = mineral_counts.pop(0)
                if pick_type == 0:
                    tired += sum(section)
                elif pick_type == 1:
                    tired += 5 * section[0] + sum(section[1:])
                elif pick_type == 2:
                    tired += 25 * section[0] + 5 * section[1] + section[2]
            
    return tired

    