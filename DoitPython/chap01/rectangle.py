# 가로, 세로 길이가 정수이고, 넓이가 area인 직사각형에서 변의 길이 나열하기

import math
area = int(input('직사각형의 넓이를 입력하세요. : '))

for i in range(1, math.floor(math.sqrt(area)) + 1):
    if area % i  == 0:
       w = area // i
       print(f'{i} x {w}')
