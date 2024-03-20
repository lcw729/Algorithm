def solution(word):
    oneChar = {
        'A' : 0,
        'E' : 1,
        'I' : 2,
        'O' : 3,
        'U' : 4
    }
    
    lenOfChar = [781, 156, 31, 6, 1]
    lenOfWord = len(word) - 1
    answer = 0
    
    for idx, current in enumerate(word):
        answer = answer + oneChar[current] * lenOfChar[idx] + 1
        
    return answer