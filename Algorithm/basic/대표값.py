# 대표값
import math 
from typing import Sequence

n = int(input())
nlist = list(map(int, input().split()))
ave = sum(nlist)/n
ave = int(ave + 0.5) # 소수점 첫째 자리에서 반올림

min = float('inf')

for idx, val in enumerate(nlist):
    diff = abs(val - ave)
    if diff < min:
        min = diff
        number = idx + 1
    elif diff == min:
        if val  > nlist[number - 1]:
            number = idx + 1

print(f"%d %d" %(ave, number))