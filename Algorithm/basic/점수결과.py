n = int(input())
nlist = list(map(int, input().split()))
sum = 0
count = 0
for val in nlist:
    if val:
        count += 1
        sum += count
    else:
        count = 0

print(sum)
        
