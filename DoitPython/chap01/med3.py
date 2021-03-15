
print('세 정수의 중앙값을 구합니다.')
a = int(input('정수 a의 값을 입력하세요 : '))
b = int(input('정수 b의 값을 입력하세요 : '))
c = int(input('정수 c의 값을 입력하세요 : '))

def medium(a,b,c):
    if a >= b:
        if b >= c:
            return b
        else:
            if a >= c:
                return c
            else:
                return a
    else:
        if a >= c:
            return a
        else:
            if c >= b:
                return b
            else:
                return c


print(f'중앙값은 {medium(a,b,c)}입니다.')