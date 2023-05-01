# 숙제
# 스택 구조를 작성하시오
# 입력 받는 부분
# 출력 하는 부분 을 모두 작성

stack = []
while True:
    print("- 모드 - \n1. 입력 2. 출력 3. 종료")
    mode = int(input("모드 숫자를 입력하시오 : "))
    if (mode == 1):
        inval = input("입력할 숫자를 뛰어쓰기로 구분하여 입력")
        inlist = inval.split()
        stack = stack + inlist
    elif (mode == 2):
        print("출력된 값 : ", stack.pop())
    elif (mode == -1 or mode == 3):
        print("종료합니다. ")
        break
    print("현재 스택 상태 : ", stack)
