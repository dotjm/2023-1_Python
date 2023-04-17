# 변수를 중복해서 사용 가능 한가? 
# => 중복해서 사용 불가
# 그러나 함수 안에서와 밖에서 같은 이름의 변수 사용했음
# 변수 => 지역변수, 전역변수. 우리가 쓴건 지역변수

# 함수 : 매개변수 있거나, 없거나, 리턴 값이 있거나 없거나. 

def sum(start, end):
    sum = 0
    for i in range(start, end+1):
        sum = sum + i
    return sum

sum = sum(1, 10)
print("Sum = ", sum)