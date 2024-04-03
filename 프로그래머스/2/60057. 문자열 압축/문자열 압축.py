def solution(s):
    answer = 0
    minimum = len(s)
    for l in range(1, len(s)//2+1):
        result = calculateResult(l, s)
        if result < minimum:
            minimum = result
    
    return minimum

def calculateResult(l, s):
    lst = list()
    count = 1
    for idx in range(0, len(s) + 1, l): # 0 ~ 끝까지 l 간격으로
        if idx+l >= len(s): 
            targetStr = s[idx:]
        else:
            targetStr = s[idx:idx+l]
        if len(lst) > 0:
            if lst[len(lst) - 1] == targetStr: 
                count += 1
            else:
                if count > 1: 
                    lst.append(str(count))
                lst.append(targetStr)
                count = 1
        else: 
            lst.append(targetStr)
    
    return len(''.join(lst))