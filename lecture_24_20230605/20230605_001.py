def get_sum(x, y):
    return x + y

print("정수 합 =", get_sum(10, 20))

f = lambda x, y: x+y; # 람다식
print("정수 합 =", f(10, 20))

"""
a++ #단항 연산자?
a+b #이항 연산자
(x>y):x:y # 삼항 연산자
"""

def celsius(in_f): # 일반 함수
    return (5.0/9.0)*(in_f-32.0)

f_temp = [0, 10, 20, 30, 40, 50]

ftoc = lambda in_f: (5.0/9.0)*(in_f-32.0) # 람다식

# c_temp = map(celsius, f_temp)
# c_temp = map(ftoc, f_temp) # 람다식 활용
c_temp = map((lambda in_f: (5.0/9.0)*(in_f-32.0)), f_temp) # 람다식 사용하여 한줄로 처리
print(list(c_temp))
