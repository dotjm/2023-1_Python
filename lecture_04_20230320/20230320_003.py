##
# 화씨 온도 -> 섭씨 온도
# 
# 변경된 버전 5강에서 진행. 해당 파일 (001) 참고
#
print("화씨 온도 및 섭씨 온도 변환 프로그램")
print()
print("화씨 온도 -> 섭씨 온도 변환 모드 : 1번 입력")
print("섭씨 온도 -> 화씨 온도 변환 모드 : 2번 입력")
print()
# select_type = int(input("모드 번호 입력 : "))

while True:
    select_type = int(input("모드 번호 입력 : "))

    if select_type == 1: # 화씨 온도를 섭씨 온도로 변환
        in_f = int(input("화씨 온도 입력 : "))
        rst = (in_f - 32.0) * 5.0/9.0 # 화씨 온도를 섭씨 온도로 변환 공식
    elif select_type == 2: # 섭씨 온도를 화씨 온도로 변환
        in_c = int(input("도씨 온도 입력 : "))
        rst = in_c * 1.8 + 32 # 섭씨 온도를 화씨 온도로 변환하는 
    elif select_type == 0:
        print("==== 도움말 : 모드 번호 안내 ====")
        print()
        print("화씨 온도 -> 섭씨 온도 변환 모드 : 1번 입력")
        print("섭씨 온도 -> 화씨 온도 변환 모드 : 2번 입력")
        # print()
        rst = ""
    else:
        break
    print(rst)
    print("\n\n")
