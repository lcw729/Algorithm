# 리스트에서 임의의 원솟값을 업데이트하기

def change(lst, idx, val):
    """lst[idx]의 값을 val로 업데이트"""
    lst[idx] = val

x = [1,2,3,4,5]
change(x,2,9)

print(x) # [1,2,9,4,5]