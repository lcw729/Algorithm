# +와 -를 번갈아 출력하기 1

print('+와 -를 번갈아 출력합니다.')
n = int(input('몇 개를 출력할까요?: '))

'''
for i in range(n): 
    if i % 2: # 홀수인 경우 + 출력
        print('+', end=' ')
    else: # 짝수인 경우 - 출력
        print('-', end=' ')
'''
# 문제점1 : for문을 수행할 때마다 if문을 수행한다.
# 문제점2 : 유연한 수정이 (range의 범위) 어렵다.

# 개선한 코드 
for _ in range(n // 2): 
    print('+ -', end = ' ')

if n % 2:
    print('+')

