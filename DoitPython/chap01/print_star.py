# *을 n개 출력하되 w마다 줄바꿈하기 1

print('*를 출력합니다.')
n = int(input('몇 개를 출력할까요?'))
w = int(input('몇 개마다 줄바꿈할까요?: '))

'''
for i in range(1, n + 1):
    print('*', end=' ')
    if i % w == 0:
        print()
'''

# for문을 실행할 때마다 if문을 실행하므로 비효율적이다.

# 개선한 코드 
for _ in range(n // w):
    print('*' * w)

rest = n % w
if rest:
    print('*' * rest)

