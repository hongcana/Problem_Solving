def solution(lottos, win_nums):
    win = 0 # 몇 개의 번호가 같은지 체크
    best = 0
    for i in range(0,6):
        if lottos[i] in win_nums: # O(N^2)
            win += 1
        elif lottos[i] == 0 :
            best += 1
    best += win
    
    # elif? switch?
    if win == 0 or win == 1: # 낙첨
        win = 6
    elif win >= 2:
        win = 7 - win
    
    if best == 0 or best == 1:
        best = 6
    elif best >= 2:
        best = 7 - best
        
    return [best, win]