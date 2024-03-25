def solution(num):
    answer = 0
    
    answer = calculator(0, num)
    return answer

def calculator(count, current):
    if current == 1:
        if count == 0: return 0
        return count
    if count == 500:
        return -1
    else:
        if current%2==0:
            nextValue=current/2
        else:
            nextValue=current*3+1
        nextCount = count + 1
        return calculator(nextCount, nextValue)