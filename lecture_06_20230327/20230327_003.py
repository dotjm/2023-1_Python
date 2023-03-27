weight = float(input("몸무게를 kg 단위로 입력 : "))
height = float(input("키를 미터 단위로 입력 : "))

bmi = (weight/(height**2))
print("당신의 BMI=", bmi)
if bmi < 18.5:
    print("당신은 저체중. ")
elif bmi < 24.99:
    print("당신은 표준. ")
elif bmi < 29.99:
    print("당신은 과체중. ")
else:
    print("당신은 비반. ")