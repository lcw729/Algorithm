from curses import nl
from imaplib import Int2AP
from turtle import right


n = int(input())
nlist = []

for _ in range(n):
    nlist.append(list(map(int, input().split())))


isVisited = [[ 0 for _ in range(n)] for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(n):
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

print(cnt)