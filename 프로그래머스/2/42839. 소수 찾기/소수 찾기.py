from itertools import permutations
from math import sqrt

def solution(numbers):
    answer = 0
    # 순열 구하기
    per = []
    for n in range(1, len(numbers)+1):
        per += permutations(numbers, n)
    per = set([ int("".join(p)) for p in per]) # 중복 제거
    
    # 소수인지 확인하기
    for num in per:
        if isPrime(num):
            answer += 1
        
    return answer

def isPrime(num):
    if (num < 2):
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True