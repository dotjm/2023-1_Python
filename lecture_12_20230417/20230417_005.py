# 매개변수를 받은걸 쓰든 안쓰든 상관 X 
# 함수가 요구하는 개수 만큼의 매개변수를 넘겨주기만 하면 OK


def cals():
    rst = 3.14 * r *2 # 지역변수 : rst, 전역변수 : r
    return rst

def cals2(rad):
    rst = 3.14 * rad *2 # 지역변수 : rst, rad
    return rst

r = float(input("반지름 : ")) # 전역변수
area = cals()
area2 = cals2(r)
print("Area = ", area, area2)