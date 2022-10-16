n = int(input())
nlist = list(map(int, input().split()))
m = int(input())
mlist = list(map(int, input().split()))

res = []
idx = 0
if m > n:
    list1 = mlist
    list2 = nlist
else:
    list1 = nlist
    list2 = mlist
    
for i in list1:
    while(idx < len(list2)):
        if i >= list2[idx]:
            res.append(list2[idx])
            idx += 1
        else:
            break
    res.append(i)

for x in res:
    print(x, end=' ')
