def solution(players, callings):
    p_dict = {player: i for i, player in enumerate(players)}
    
    for called in callings:
        c = p_dict[called]
        p_dict[called] -= 1
        p_dict[players[c-1]] += 1
        players[c-1], players[c] = players[c], players[c-1]

    return players