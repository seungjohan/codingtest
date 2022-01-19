def solution(money, expected, actual):

    bet = 100
    
    for i in range(len(expected)):
    
        if expected[i] == actual[i]:
        
            if money > bet:
        
                money += bet
        
            else:
                money += money
        
            bet = 100
        else:
        
            if money > bet:
                money -= bet
            
                bet *= 2
            
            elif money == 0:
                return money
            
            else:
                money -= bet
                bet = money

    return money
