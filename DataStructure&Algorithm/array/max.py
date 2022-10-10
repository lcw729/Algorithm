from typing import Sequence, Any

'''
p. 77
1. 매개변수 a의 자료형 Sequence형이다.
2. 임의의 자료형 Any 반환한다.
3. 모듈 이름이 __main__이면 실행한다. 즉, 다른 모듈에서 임포트되면 실행안된다.
'''

def max_of(a : Sequence) -> Any: 
    maximum = a[0]
    for i in range(1,len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum


if __name__ == '__main__':
    print('배열의 최댓값을 구합니다.')
    num = int(input('원소 수를 입력하세요 :'))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]값을 입력하세요 :'))

    print('최댓값은 %d입니다.' %(max_of(x)))