from math import pi # 파이 값 가져오기

rad = int(input("반지름을 입력 : ")) # radius 값 저장

# area = 3.14 * rad * rad
area = pi * rad * rad # math 라이브러리의 pi 값 가져오기

print("반지름", rad, "인 원의 면적 = ", area)
print("반지름" + str(rad) + "인 원의 면적 = " + str(area)) # 형 변환 (더하기로 출력하려면 필수)