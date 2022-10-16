n = int(input())

def palindrome(s)->str:
    tmp = list(s)
    for i in range(len(s)//2):
        if tmp[i].lower() != tmp[len(tmp)-1-i].lower():
            return "NO"
    else:
        return "YES"

"""
if s == s[::-1]:
    print("#%d YES", %(i+1))
else:
    print("#%d NO", %(i+1))
아예 슬라이스로 스트링 자체를 뒤집에서 비교하는 방법도 있다.
"""

res = []
for i in range(n):
    s = input()
    res.append(palindrome(s))


for idx, val in enumerate(res):
    print(f'#{idx+1} {val}')