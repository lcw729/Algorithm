from curses import nl


n = int(input())
nlist = []
for _ in range(n):
    nlist.append(list(map(int,input().split())))

m = int(input())
mlist = []
for _ in range(m):
    mlist.append(list(map(int,input().split())))

def move(k, p, q):
    q = q % n
    if p: # 오른쪽
        nlist[k-1] = nlist[k-1][-q:] + nlist[k-1][0:n-q]
        """
        for _ in range(q):
            nlist[k-1].append(nlist[k-1].pop(0))
        """
    else: # 왼쪽
        nlist[k-1] = nlist[k-1][q:] + nlist[k-1][0:q]
        """
        for _ in range(q):
            nlist[k-1].insert(0, nlist[k-1].pop())
        """        

for i in mlist:
    k, p, q = map(int, i)
    move(k, p, q)

for i in nlist:
    print(i)

res = 0
for i in range(n):
    if i == 0 | i == n-1:
        print(nlist[i])
        res += sum(nlist[i])
    elif i <= n//2:
        print(nlist[i][i:n-i])
        res += sum(nlist[i][i:n-i])
    else:
        print(nlist[i][n-1-i:i+1])
        res += sum(nlist[i][n-1-i:i+1])

print(res)