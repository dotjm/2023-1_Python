# 함수를 사용한 팩토리얼 계산

# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fact(n-1)


# n = int(input("팩토리얼을 구할 숫자 입력 : "))


# rst = fact(n)
# print("Factorial = ", rst)


##############################
# 반복문을 사용한 팩토리얼 계산

n = int(input("팩토리얼을 구할 숫자 입력 : "))

rst = 1
for i in range(1, n+1):
    rst *= i

print("Factorial = ", rst)