def solution(penter, pexit, pescape, data):
    answer = ''
    
    pen = len(penter)
    
    for i in range(0, len(data), pen):

        if data[i:i+pen] == penter or data[i:i+pen] == pexit or data[i:i+pen] == pescape:
            answer += pescape
            
        answer += data[i:i+pen]
    
    answer = penter + answer + pexit

    return answer
