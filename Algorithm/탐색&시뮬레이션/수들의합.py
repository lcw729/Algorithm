n, m = map(int,input().split())
nlist = list(map(int, input().split()))

cnt = 0 
for i in range(n):
    sum = 0
    for j in range(i,n):
        sum += nlist[j]
        if sum == m:
            cnt += 1
            break
        elif sum > m:
            break

print(cnt)
