# 자릿수의 합
n = int(input())
nlist = list(map(int, input().split()))

def digit_sum(a: int)-> int:
    sum = 0
    while(a > 0):
        sum += a % 10
        a = a // 10
    return sum

'''
def digit_sum(a: int)-> int:
    sum = 0
    for i in str(a):
        sum += int(i)
    return sum
'''

result = map(digit_sum, nlist)
max = 0
max_idx = 0
for idx, val in enumerate(result):
    if val > max:
        max = val
        max_idx = idx

print(nlist[max_idx])