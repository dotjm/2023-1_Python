# 키워드 인수

def cali(x, y, z):
    return x+y+z

rst = cali(10, 20, 30) # 순서대로 입력
rst2 = cali(y=20, x=10, z=30) # 순서 상관 X
print("Result =", rst, rst2)

# 가변 인수
def acals(*args): # 여러개의 값을 받도록 지정
    print(args)
    sum = 0
    for i in args:
        sum += i
    print(sum)

acals(10)
acals(10, 20, 30, 40, 50)
