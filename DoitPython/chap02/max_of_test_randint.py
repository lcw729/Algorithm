# 배열 원소의 최댓값을 구해서 출력하기(원솟값을 난수로 생성)

import random
from max import max_of

print('난수의 최댓값을 구합니다.')

n = int(input('생성할 난수의 개수를 입력하세요.: '))
max = int(input('생성할 난수 범위의 최댓값을 입력하세요.: '))
min = int(input('생성할 난수 범위의 최솟값을 입력하세요.: '))

x = []

for i in range(n):
    x.append(random.randint(min,max))

print(f'배열의 최댓값은 {max_of(x)}입니다.')