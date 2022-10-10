'''
n의 제곱근 이하의 어떤 소수로도 나누어 떨어지지 않는다.
'''

counter = 0
ptr = 0

prime = [None] * 500
prime[0] = 2
ptr += 1

prime[1] = 3
ptr += 1

for n in range(5, 1001, 2):
    i = 1
    while prime[i] * prime[i] <= n:
        print(prime[i] * prime[i])
        print(n)
        print(prime[i] * prime[i] < n)
        print('*')
        counter += 2
        if n % prime[i] == 0:
            break
        i += 1
    else:
        counter += 1
        prime[ptr] = n
        print(f"==== {prime[ptr]}")
        ptr += 1

for i in range(ptr):
    print(prime[i])
print(f'나눗셈을 실행한 횟수 : {counter}')
