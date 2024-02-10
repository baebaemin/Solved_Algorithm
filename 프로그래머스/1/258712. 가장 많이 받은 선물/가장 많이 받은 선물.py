def solution(friends, gifts):
    present_cnt = {}   # 선물지수
    for name in friends:
        present_cnt[name] = 0

    length = len(friends)
    present_map = [[0] * length for _ in range(length)]
    present_list = [0] * length

    for gift in gifts:
        giver, getter = map(str, gift.split())
        present_cnt[giver] += 1
        present_cnt[getter] -= 1

        giver_idx = friends.index(giver)
        getter_idx = friends.index(getter)
        present_map[giver_idx][getter_idx] += 1

    for giver in range(length):
        for getter in range(giver+1, length):
            # 주고받은 선물이 있다면 누가 더 많이 주었는지 비교하여 선물 받기
            if present_map[giver][getter] > present_map[getter][giver]:
                present_list[giver] += 1
            elif present_map[giver][getter] < present_map[getter][giver]:
                present_list[getter] += 1
            # 주고받은 선물이 없다면 선물지수로 비교하여 선물 받기
            else: 
                if present_cnt[friends[giver]] > present_cnt[friends[getter]]:
                    present_list[giver] += 1
                elif present_cnt[friends[giver]] < present_cnt[friends[getter]]:
                    present_list[getter] += 1

    return max(present_list)
