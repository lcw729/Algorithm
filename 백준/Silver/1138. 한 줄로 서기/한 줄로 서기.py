# input
n = int(input())
lst = list(map(int, input().split(' ')))
zero_lst = [number for number in range(n)]

# initialize
sol = [0] * n
answer = ''

for i, target in enumerate(lst):
    cnt = 0
    for idx in range(n):
        if sol[idx] == 0:
            cnt += 1

        if cnt == target + 1:
            sol[idx] = i + 1
            break

for number in sol:
    print(number, end=' ')