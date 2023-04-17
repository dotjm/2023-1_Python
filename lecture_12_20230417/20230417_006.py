def cals(a, b=100):
    rst = a + b
    return rst

in_val = int(input("입력 : "))
rst = cals(in_val)
rst = cals(in_val, 300)

print("Result =", rst)