# 1000이하의 소수를 나열하기

# step 1
"""
counter = 0

for n in range(2,1001): 
    for i in range(2, n): 
        counter += 1
        if n % i == 0: # 나누어 떨어지면 소수가 아님
            break      # 반복은 더 이상 불필요하려 중단
    else:              # 끝까지 나누어 떨어지지 않으면 다음을 수행
        print(n)

print(f'나눗셈을 실행한 횟수: {counter}') # 78022
"""
# 문제점 : n이 소수인 경우에는 for문을 2부터 n-1까지 돌려야 한다. 즉, 나눗셈 연산이 필요이상으로 많다.

# 2와 3으로 나누어지지 않는다면, 2 x 2와 2 x 3으로도 나누어지지 않는다.
# 앞서 존재하는 소수들로만 나누어지는지 확인하면 된다.

# step 2
"""
counter = 0
x = []

for n in range(2, 1001):
    for i in x:
        counter += 1
        if n % i == 0:
            break
    else:
        x.append(n)
        print(n)
        
print(f'나눗셈을 실행한 횟수: {counter}') #15620
"""

# 2를 배열 x에 초기에 넣어준다면, 2의 배수인 짝수는 확인할 필요가 없다.

# step 3

counter = 0
x = [2]
ptr = 1

for n in range(3, 1001, 2): # 홀수만을 대상으로 설정
    for i in range(1, ptr): # 이미 찾은 소수로 나눔
        counter += 1
        if n % x[i] == 0: # 나누어 떨어지면 소수가 아님
            break
    else:
        x.append(n) # 소수라면 배열 x에 추가하기
        ptr += 1
        
for i in range(ptr):
    print(x[i])
        
print(f'나눗셈을 실행한 횟수: {counter}') #14622