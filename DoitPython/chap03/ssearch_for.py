from typing import Any, Sequence

def seq_search(a : Sequence, key: Any) -> int:

    for i in range(len(a)):
        if a[i] == k:
            return i
    return -1

if __name__ == '__main__':

    n = int(input('원소 수를 입력하세요.: '))
    a = [None] * n

    for i in range(n):
        a[i] =  int(input(f'a[{i}]: '))

    k = int(input('검색할 값을 입력하세요.: '))

    idx = seq_search(a, k)

    if idx == -1:
        print('검색값을 갖는 원소가 존재하지 않습니다.')
    else:
        print(f'검색값은 a[{idx}]에 존재합니다.')

        