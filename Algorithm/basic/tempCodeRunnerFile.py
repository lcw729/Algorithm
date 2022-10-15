n = int(input())
max = 0
for i in range(n):
    tmp = input().split()
    tmp.sort()
    a, b, c = map(int, tmp)
    if a == b and b == c:
        res = a * 1000 + 10000
    elif a == b or b == c:
        res = b * 100 + 1000 
    else:
        res = c * 100
    if res > max:
        max = res

print(max)
