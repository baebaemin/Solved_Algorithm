def solution(picks, minerals):
    minerals += [''] * 5
    picks_num = sum(picks)
    section_lst = []
    tired = 0
    
    for i in range(picks_num):        
        minerals_section = minerals[i*5:i*5+5]
        if not minerals_section or minerals_section == ['', '', '']:
            break
            
        diamond_cnt = minerals_section.count('diamond')
        iron_cnt = minerals_section.count('iron')
        stone_cnt = minerals_section.count('stone')
        section_lst.append([diamond_cnt, iron_cnt, stone_cnt])
    
    section_lst.sort(key=lambda x: (x[0], x[1]), reverse=True)

    while picks[0] and section_lst:
        picks[0] -= 1
        section = section_lst.pop(0)
        tired += sum(section)
    
    while picks[1] and section_lst:
        picks[1] -= 1
        section = section_lst.pop(0)
        tired += 5 * section[0]
        tired += section[1]
        tired += section[2]
    
    while picks[2] and section_lst:
        picks[2] -= 1
        section = section_lst.pop(0)
        tired += 25 * section[0]
        tired += 5 * section[1]
        tired += section[2]
    
    return tired

    