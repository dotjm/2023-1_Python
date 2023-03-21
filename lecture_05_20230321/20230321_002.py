import math

in_val1 = int(input("입력 :"))
in_val2 = int(input("입력 :"))

# rst = in_val1 ** in_val2
rst = math.pow(in_val1, in_val2)  # math 라이브러리 활용 
print(rst)