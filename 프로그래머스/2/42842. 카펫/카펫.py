def solution(brown, yellow):
    answer = []
    
    total = brown + yellow
    for num in range(3, int(total ** 1/2) + 1):
        if (total % num == 0):
            w, h = total / num, num
            if ((w-2) * (h-2) == yellow):
                return [w, h]
            
    return answer