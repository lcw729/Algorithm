from max import max_of

'''
p. 80 참고
'''

print('배열의 최댓 값을 구합니다.')
print('주의: End를 입력하면 종료합니다.')

number = 0
x = []

while True:
    str = input(f'x[{number}]를 입력하세요. : ')
    if str == 'End':
        break
    else:
        x.append(int(str))
        ++number
    
print(f'최댓값은 {max_of(x)}입니다.')