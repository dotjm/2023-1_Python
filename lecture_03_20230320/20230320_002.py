# 교수님 퀴즈 실습
# 초를 입력하자... 400~10000 사이 8530
# 시, 분, 초 를 출력하자

in_val = int(input("입력 = "))

hour = in_val // (60*60)
minute = (in_val - hour*60*60) // 60
sec = in_val % 60

print(in_val, "초는", hour, "시간", minute, "분", sec, "초 입니다. ")