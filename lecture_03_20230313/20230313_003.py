width = int(input("밑변 입력 : ")) # 밑변 길이 값은 입력받아 int로 변환
height = int(input("높이 입력 : ")) # 높이 길이 값은 입력받아 int로 변환

# width = 10
# height = 10

area = width * height * (1 / 2) # 삼각형 높이 구하기 공식 적용하여 계산
# area = width * height / 2 # 삼각형 높이 구하기 공식 적용하여 계산

print("삼각형의 면적은", area)