team_name = 'Period5__Team2'
strategy_name = 'Finding Nemo'
strategy_description = 'Do Stuff'
def move(my_history, their_history, my_score, their_score):
    b_value = 0
    c_value = 0
    if len(my_history) == 0:
        return 'b'
    if len(my_history) == 1:
        return 'b'
    if len(my_history) == 2:
        return 'b'
    if len(my_history) == 3:
        return 'b'
    if len(my_history) == 4:
        return 'b'
    if len(my_history) == 5:
        return 'b'
    if len(my_history) == 6:
        return 'c'
    if len(my_history) == 7:
        return 'c'
    if len(my_history) == 8:
        return 'c'
    if len(my_history) == 9:
        return 'c'
    if len(my_history) == 10:
        return 'c'
    if (their_history[-1] == 'c' and their_history[-2] == 'c' and their_history[-3] == 'c' and their_history[-4] == 'c' and their_history[-5] == 'c'):
        b_value += 1
        return 'c' 
    else:
        c_value += 1
        return 'b'
    if (their_history[-6] == 'b' and their_history[-7] == 'b' and their_history[-8] == 'b' and their_history[-9] == 'b' and their_history[-10] == 'b'):
        b_value += 1
        return 'b'
    if (their_history[-1] == 'c' and their_history[-2] == 'b' and their_history[-3] == 'c' and their_history[-4] == 'b' and their_history[-5] == 'c'):
        flag1 = 1
        if flag1 == 1:
            return 'b'
            flag1 == 0
        if flag1 == 0:
            return 'c'
    if (their_history[-1] == 'b' and their_history[-2] == 'c' and their_history[-3] == 'b' and their_history[-4] == 'c' and their_history[-5] == 'b'):
        flag2 = 1
        if flag2 == 1:
            return 'b'
            flag2 == 0
        if flag2 == 0:
            return 'c'
        
    if b_value > 40:
        return 'b'
    if c_value > 40:
        return 'c'
    
        
        
        