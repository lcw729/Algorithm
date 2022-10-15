# 소수의 개수 구하기
import math 

n = int(input())

prime = []
prime.append(2)
prime.append(3)

for i in range(5, n+1, 2): # 짝수 제외
    idx = 0
    while(prime[idx] <= math.sqrt(i)): # 제곱근 이하의 수만 비교
        if i % prime[idx] == 0:
            break
        idx += 1
    else: # 실수한 부분
        prime.append(i)

print(len(prime))
