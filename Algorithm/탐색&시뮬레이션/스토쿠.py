
nlist = list()

for _ in range(9):
    nlist.append(list(map(int, input().split())))

num = set(range(1,10))
def checkSudoku(nlist):
    for i in range(9):
        row = list()
        col = list()
        for j in range(9):
            if nlist[i][j] in row:
                return "NO"
            else:
                row.append(nlist[i][j])
            if nlist[j][i] in col:
                return "NO"
            else:
                col.append(nlist[j][i])
        if (set(col) != num) | (set(row) != num):
            return "NO"
    
    for i in range(1,8,3):
        for j in range(1,8,3):
            section = list()
            for tmpx in list([i-1,i,i+1]):
                for tmpy in list([j-1,j,j+1]):
                    section.append(nlist[tmpx][tmpy])
            if num != set(section):
                return "NO"    
    else:
        return "YES"

print(checkSudoku(nlist))
        