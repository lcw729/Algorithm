n = int(input())
nlist = []

for _ in range(n):
    nlist.append(list(map(int, input().split())))

res = 0
for i in range(n):
    if i <= n//2:
       res += sum(nlist[i][n//2-i:n//2+i+1])
    else:
       res += sum(nlist[i][n//2-(n-i-1):n//2+(n-i-1)+1])


print(res)
