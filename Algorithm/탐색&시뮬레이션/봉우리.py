from curses import nl
from imaplib import Int2AP
from turtle import right

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())
nlist = []

for _ in range(n):
    nlist.append(list(map(int, input().split())))

nlist.insert(0, [0]*n)
nlist.append(0, [0]*n)
for x in nlist:
    x.insert(0, 0)
    x.append(0)

cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if all(nlist[i][j] > nlist[i+dx[k]][j+dx[k]] for k in range(4)):
            cnt += 1

"""
isVisited = [[ 0 for _ in range(n)] for _ in range(n)]
cnt = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        if isVisited[i][j] == 0:
            L = j - 1
            R = j + 1
            T = i + 1
            B = i - 1
            if L >= 0:
                if nlist[i][L] < nlist[i][j]:
                    isVisited[i][L] = -1
                else:
                    isVisited[i][j] = -1
                    continue
            if R < n:
                if nlist[i][R] < nlist[i][j]:
                    isVisited[i][R] = -1
                else:
                    isVisited[i][j] = -1
                    continue
            if T < n:
                if nlist[T][j] < nlist[i][j]:
                    isVisited[T][j] = -1
                else:
                    isVisited[i][j] = -1
                    continue
            if B >= 0:
                if nlist[B][j] < nlist[i][j]:
                    isVisited[B][j] = -1
                else:
                    isVisited[i][j] = -1  
                    continue
            isVisited[i][j] = 1
            cnt += 1
        elif isVisited[i][j] == -1:
            continue
"""
print(cnt)