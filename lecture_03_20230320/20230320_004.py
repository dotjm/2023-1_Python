import math

PI = 3.141592653589793238 # 상수 섭언
rad = int(input("반지름 입력 : "))

rst = rad * rad * math.pi # <== 상수
rst = rad * rad * PI
#rst = result


print("Area = ", rst)