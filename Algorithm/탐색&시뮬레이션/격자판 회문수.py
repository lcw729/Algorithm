nlist = list()

for _ in range(7):
    nlist.append(list(map(int, input().split())))
    

def palindrome(nlist):
    for i in range(len(nlist)//2):
        if nlist[i] != nlist[len(nlist)-i-1]:
            return False
    return True
            

count = 0
for i in range(7):
    for j in range(2,5):
            if palindrome(nlist[i][j-2:j+3]):
                print(nlist[i][j-2:j+3])
                count += 1
            tmp = list()
            tmp.append(nlist[j-2][i])
            tmp.append(nlist[j-1][i])
            tmp.append(nlist[j][i])
            tmp.append(nlist[j+1][i])
            tmp.append(nlist[j+2][i])
            if palindrome(tmp):
                print(tmp)
                count += 1        
    
print(count)