from typing import Sequence, Any


def bin_search(a :Sequence, key: Any) -> int:
    pl = 0
    pr = len(a) - 1
    
    while (pl <= pr):
        pc = (pl + pr) // 2
        if a[pc] < key:
            pl = pc + 1
        elif a[pc] > key:
            pr = pc - 1
        else:
            return pc
    return -1


if __name__ == '__main__':
    num = int(input("원소의 개수를 입력하세요 : "))
    arr = [None] * num

    arr[0] = int(input(f"arr[0]의 값을 입력하세요 : "))
    for i in range(1,num):
        arr[i] = int(input(f"arr[{i}]의 값을 입력하세요 : "))
        if arr[i-1] > arr[i]:
            break


    key = int(input("검색하고 싶은 값을 입력하세요 : "))

    result = bin_search(arr, key)

    if result == -1:
        print("값을 찾지 못했습니다.")
    else:
        print(f"{key} 값은 배열의 {result} 인덱스에 존재합니다.")
    