#K번째수

from curses import nl


testcase = int(input())

for _ in range(testcase):
    n, s, e, k = map(int, input().split())
    nlist = list(map(int,input().split()))
    sublist = nlist[s-1:e]
    sublist.sort()
    print(sublist[k-1])