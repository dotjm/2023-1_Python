dan = int(input("원하는 단 입력 : "))

i = 1
while i <= 9:
    # print("%s * %s = %s" % (dan, i, dan * i)) # 아래와 동일, 각 %s는 문자열 대치를 의미하고, 뒤의 괄호 안에서 순서대로 가져옴. 
    # print(f"{dan} * {i} = ", dan * i) # 아래와 동일, 각 %s는 문자열 대치를 의미하고, 뒤의 괄호 안에서 순서대로 가져옴. 
    print(dan, "*", i,  "=", dan * i) # 위와 동일
    i = i + 1