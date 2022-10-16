from cmath import sqrt


s = input()
number = list("0123456789")
res = 0
for i in list(s):
    if i in number: # x.isdecimal()
        res = res * 10 + int(i)

# 약수 구하기  
count = 0
i = 1
while i**2 < res:
    if res % i == 0:
        count += 1
    i += 1
count *= 2

# 제곱수인 경우
if i**2 == res:
    count += 1
    
print(res)
print(count)
