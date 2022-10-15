
from math import sqrt
from operator import truediv


n = int(input())
nlist = list(map(int, input().split()))
prime = []
prime.append(2)
prime.append(3)

def reverse(x: int) -> int:
    res = 0
    while(x > 0):
        tmp = x % 10
        res = res * 10 + tmp
        x = x // 10
    return res

def isPrime(x: int) -> int:
    if x == 1:
        return False # 실수한 부분
    for i in range(2, int(sqrt(x))+1): # 모든 수의 약수는 제곱근을 기준으로 대칭을 이룬다.
        if x % i == 0:
            return False
    return True

for i in nlist:
    tmp = reverse(i)
    if isPrime(tmp):
        print(tmp, end=" ")