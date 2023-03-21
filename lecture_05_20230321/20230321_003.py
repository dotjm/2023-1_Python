principal = int(input("원금 입력 :"))
interest_rate = float(input("이자율 입력 :"))
term = int(input("기간 입력 :"))

result = principal*(1+interest_rate)**term

# print("원리금 합계 =", result)
print("원리금 합계 = %.2f" %result)


# 입력 방법 예제
# ok = input("입력") # 문자로 입력
# ok2 = int(input("정수 입력 :")) # 정수로 입력
# ok3 = float(input("실수 입력 :")) # 실수로 입력

