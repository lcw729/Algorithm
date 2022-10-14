# 정다면체
n, m = map(int, input().split())
nlist = [0 for _ in range(n+m)]

for i in range(1,n+1):
    for j in range(1,m+1):
        nlist[i+j-1] += 1

tmp = list()
max = 0
for idx, val in enumerate(nlist):
    if val > max:
        tmp.clear()
        tmp.append(idx + 1)
        max = val
    elif val == max:
        tmp.append(idx + 1)

for i in tmp:
    print(i, end=' ')
        

