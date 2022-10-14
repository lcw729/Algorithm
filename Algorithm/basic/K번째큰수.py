
n, k = map(int, input().split())
nlist = list(map(int, input().split()))
res = set()

for i in range(len(nlist)-2):
    num1 = nlist[i]
    for j in range(i+1, len(nlist)-1):
        num2 = nlist[j]
        for p in range(j+1, len(nlist)):
            num3 = nlist[p]
            res.add(num1+num2+num3)

klist= list(res)
klist.sort(reverse=True)
print(klist[k-1])
