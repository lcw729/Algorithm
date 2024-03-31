def solution(numbers):
    global permuList
    permuList = []
    
    answer = 0
    permutation(list(numbers))
    for num in permuList:
        print(num, isPrime(num))
        if (isPrime(num)): answer += 1
    
    return answer

def permutation(numbers):
    storage = []

    if len(numbers) == 1:
        if int(numbers[0]) not in permuList:
            permuList.append(int(numbers[0]))  # 한글자면 반환
        return numbers
    
    for idx, current in enumerate(numbers):
        numbers[0], numbers[idx] = numbers[idx], numbers[0]  # 첫번째 숫자
        for result in permutation(numbers[1:]):
            num = numbers[0] + ''.join(result)
            if int(num) not in permuList:
                permuList.append(int(num))
            storage.append(num)
                
    return storage

def isPrime(num):
    if num <= 1: 
        return False
    if (num == 2 or num == 3):
        return True
    for i in range(2, int(num ** 1/2) + 1):
        if num % i == 0:
            return False
    return True