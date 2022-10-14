'''
p. 113
선형 검색
'''

from typing import Sequence, Any


def seq_search(a: Sequence, key: Any) -> int:
    """시퀸스 a에서 key와 값이 같은 원소를 선형 검색"""
    for idx, val in enumerate(a):
        if val == key:
            return idx
    return -1

if __name__ == '__main__':
    num = int(input("원소의 개수를 입력하세요 : "))
    arr = [None] * num

    for i in range(num):
        arr[i] = input(f"arr[{i}]의 값을 입력하세요 : ")

    key = input("검색하고 싶은 값을 입력하세요 : ")

    result = seq_search(arr, key)

    if result == -1:
        print("값을 찾지 못했습니다.")
    else:
        print(f"{key} 값은 배열의 {result} 인덱스에 존재합니다.")
    