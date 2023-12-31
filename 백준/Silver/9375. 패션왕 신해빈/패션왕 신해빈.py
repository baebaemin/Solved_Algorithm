tc_num = int(input())
for tc in range(tc_num):
    n = int(input())
    wardrobe_dict = {}
    for _ in range(n):
        name, case = map(str, input().split())
        wardrobe_dict[case] = wardrobe_dict.get(case, 0) + 1

    combinations = 1
    for case in wardrobe_dict:
        combinations *= (wardrobe_dict[case] + 1)

    print(combinations - 1)