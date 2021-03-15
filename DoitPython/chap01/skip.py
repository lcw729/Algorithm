# 1 ~ 12까지 8을 건너뛰고 출력하기 
'''
for i in range(1,13):
    if i == 8:
        continue
    print(i, end=' ')
'''
# 12번이나 조건문을 수행해야하기 때문에 비효율적인 프로그램이다. 

# 개선한 코드

for i in list(range(1,8)) + list(range(9,13)):
    print(i, end=' ')

