# 리스트 내장함수 활용

num = [1, 2, 3, 4, 5]

n = sum(num)
print(n)
max = max(num)
print(max)
min = min(num)
print(min)

max = num[0]
for i in num:
    if max < i:
        max = i
print(max)

min = num[0]
for i in num:
    if min > i:
        min = i
print(min)


# 랜덤 선택
import random

print(random.choice(num))
chr = ["k", "r", "p", "s", "o"]
print(random.choice(chr))
