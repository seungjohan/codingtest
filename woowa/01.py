def solution(grades, weights, threshold):
    
    dict = {    
    'A+' : 10,
    'A0' : 9,
    'B+' : 8,
    'B0' : 7,
    'C+' : 6,
    'C0' : 5,
    'D+' : 4,
    'D0' : 3,
    'F'  :  0
    }
    
    score = 0

    for i in range(len(grades)):
        score += dict[grades[i]] * weights[i]
    
    return score - threshold