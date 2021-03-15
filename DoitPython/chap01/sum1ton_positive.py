# 1부터 n까지 정수의 합을 구하기(n값은 양수만 입력받음)

print('1부터 n까지 정수의 합을 구합니다.')

while(True):
    n = int(input('정수 n을 입력하세요. : '))
    if (n > 0):
        break
    else:
        print('양수를 입력하세요.')

sum = 0
for i in range(1, n+1):
    sum += i

print(f'1부터 {n}까지 합한 값은 {sum}입니다.')