# 뮤터블 시퀸스 원소를 역순으로 정렬

from typing import Any, MutableSequence

def reverse_array(a : MutableSequence) -> None:
    """ 뮤터블 스퀸스 a의 원소를 역순으로 정렬 """
    n = len(a)
    for i in range(n//2):
        a[i], a[n - 1 - i] = a[n - 1 - i], a[i]

    
if __name__ == '__main__':
    print('배열의 원소를 역순으로 정렬합니다.')
    xn = int(input('배열의 크기를 입력하세요.: '))

    x = [None] * xn
    for i in range(xn):
        x[i] = int(input(f'x[{i}]의 원소를 입력하세요.: '))

    reverse_array(x)

print('배열 원소를 역순으로 정렬한 결과입니다.')
for i in range(xn):
    print(f'x[{i}] = {x[i]}')