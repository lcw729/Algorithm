# 선형 검색 알고리즘(실습 3-1)을 보초법으로 수정

from typing import Any, Sequence
import copy

def seq_search(seq: Sequence, key: Any) -> int:
    """시퀸스 seq에서 key와 일치하는 원소를 선형 검색(보초법)"""
    i = 0
    while True:
        a = copy.deepcopy(seq) # seq 복사
        a.append(key) # 보초 key를 추가

        if a[i] == key:
            break
        i += 1
        return -1 if i == len(seq) else i

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