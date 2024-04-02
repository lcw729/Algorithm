from collections import Counter

def solution(k, tangerine):
    answer = 0
    
    sortedBox = Counter(tangerine).most_common()
    
#     sortedBox = sorted(sizeBox.items(), key=lambda x: x[1], reverse=True)
    
    total = 0
    for key, value in sortedBox:
        total += value
        answer += 1
        if total >= k: break;
        
    return answer