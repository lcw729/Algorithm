# 10진수 정숫값을 입력받아 2~36진수로 변환하여 출력하기


def card_cov(n: int,r: int) -> str:

    d = '' # 변환 후의 문자열
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    while n:
        d += dchar[n % r] # 해당하는 문자를 꺼내 결합
        n //= r

    return d[::-1] # 역순으로 반환

if __name__ == '__main__':

    print('10진수를 n진수로 변환합니다.')

    while True:
        while True:
            n = int(input('음이 아닌 정수를 입력하세요.: '))
            if n >= 0:
                break

        while True:
            r = int(input('진수를 입력하세요.: '))
            if 2 <= r <= 36:
                break

        print(f'{r}진수로는 {card_cov(n, r)}입니다.')

        retry = input("한 번 더 변환할까요?(Y - 예 / N - 아니요): ")
        if retry in {'N', 'n'}:
            break
    