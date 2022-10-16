tmp = []
for i in range(10):
    tmp.append(list(map(int, input().split())))

nlist = [i for i in range(1,21)]

for a, b in tmp:
    tmp = nlist[a-1:b]
    tmp.reverse()
    nlist[a-1:b] = tmp

print(nlist)