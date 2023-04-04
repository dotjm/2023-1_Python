score = int(input("점수 입력 : "))
sel = int(input("선택 : "))

# if score >= 90: # 단일 if
#     print("잘했어요")
# else:
#     print("노력하세요")

# if 인자값이 너무 길면 함수를 이용해서 return 값을 받도록 조치해서 줄이기
if score >= 90 and sel == 1: # 다중 if
    print("학점 : A")
elif score >= 80:
    print("학점 : B")
elif score >= 70:
    print("학점 : C")
elif score >= 60:
    print("학점 : D")
else:
    print("학점 : F 많은 노력하세요")