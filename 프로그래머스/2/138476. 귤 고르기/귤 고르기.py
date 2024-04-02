def solution(k, tangerine):
    answer = 0
    sizeBox = dict()
    for item in tangerine:
        if item not in sizeBox: sizeBox[item] = 1
        else: sizeBox[item] += 1
    
    sortedBox = sorted(sizeBox.items(), key=lambda x: x[1], reverse=True)
    
    total = 0
    for key, value in sortedBox:
        if total >= k: break;
        total += value
        answer += 1
        
    return answer