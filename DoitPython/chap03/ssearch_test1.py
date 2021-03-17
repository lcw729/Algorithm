# seq_search()함수를 사용하여 실수 검색하기

from ssearch_while import seq_search

number = 0
a = []
print('실수를 검색합니다.')
print('주의: "End"를 입력하면 종료합니다.')

while True:
    s = input(f'a[{number}]: ')
    if s == "End":
        break
    a.append(float(s))
    number += 1

k = float(input('검색할 값을 입력하세요.: '))

idx = seq_search(a, k)

if idx == -1:
    print('검색값을 갖는 원소가 존재하지 않습니다.')
else:
    print(f'검색값은 a[{idx}]에 존재합니다.')