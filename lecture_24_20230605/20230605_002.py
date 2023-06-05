import fibo # 전체 불러오기 # as로 별칭 가능
from fibo import fib, fib2 # 특정 함수 불러오기

fibo.fib(1000) # 전체불러올 경우
fib(1000) # 특정 함수 불러왔을 경우
print(fibo.fib2(1000)) # 전체불러올 경우
print(fib2(1000)) # 특정 함수 불러왔을 경우

print(fibo.__name__)


import calendar 

cal = calendar.month(2023, 6)
print(cal)