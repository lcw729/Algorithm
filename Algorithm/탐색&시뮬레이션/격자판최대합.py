n = int(input())
nlist = []
for i in range(n):
    nlist.append(list(map(int, input().split())))

res = []
L = 0
R = 0
for i in range(n):
    R += nlist[i][n-1-i] # 오른쪽 대각선
    L += nlist[i][i] # 왼쪽 대각선
    tmp1 = 0
    tmp2 = 0
    for j in range(n):
        tmp1 += nlist[j][i] # 열
        tmp2 += nlist[i][j] # 행
    res.append(tmp1)
    res.append(tmp2)

res.append(R)
res.append(L)

print(max(res))
