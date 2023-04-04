num = int(input("숫자 입력 : "))

if num % 2 == 0:
    print("짝수네")
else:
    print("홀수네")

if num % 3 == 0:
    print("3의 배수네")
else:
    print("3의 배수가 아니네")

if num % 5 == 0:
    print("5의 배수네")
else:
    print("5의 배수가 아니네")

if num % 3 == 0 and num % 5 == 0: 
    print("3과 5의 배수네")
else:
    print("3과 5의 배수가 아니네")