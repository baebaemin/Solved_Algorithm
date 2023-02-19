def black_jack():
    M = list(map(int, input().split()))[1]
    min_num = M
    card_lst = sorted(list(map(int, input().split())))
    sum_card = 0    
    save_deck = 0
    

    for i in range(len(card_lst) - 2):
        card1 = card_lst[i]
        for card2 in card_lst[i+1:-1]:
            for card3 in card_lst[i+2:]:
                sum_card = card1 + card2 + card3

                if sum_card == M:
                    return sum_card

                if sum_card < M and M - sum_card < min_num:
                    min_num = M - sum_card
                    save_deck = sum_card
    else: 
        return save_deck
     
print(black_jack())