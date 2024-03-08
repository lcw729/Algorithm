def solution(brown, yellow):
    answer = []
    
    total = brown + yellow
    for num in range(3, int(total ** 1/2) + 1):
        if (total % num == 0):
            w = max(num, (total / num))
            h = total / w
            if ((w-2) * (h-2) == yellow):
                return [w, h]
            
    return answer