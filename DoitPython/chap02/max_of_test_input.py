# 배열 원소의 최댓값을 구해서 출력하기(원솟값을 입력받음)

from max import max_of


print('배열의 최댓값을 구합니다.')
print('주의: "End"를 입력하면 종료합니다.')

number = 0
x = []

while True:
    s = input(f'x[{number}]의 값을 입력하세요.: ')
    if s == "End":
        break

    number += 1
    x.append(int(s))

print(f'입력한 원소의 갯수는 {number}개 입니다.')
print(f'베열 원소의 최댓값은 {max_of(x)}입니다.')
