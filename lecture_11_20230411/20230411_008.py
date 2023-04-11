# 4장

def p_msg(name):
    print("Hello ")
    print(name + " Happy Birthday")

def testValue(a):
    a = a + 100
    return a
    
p_msg("이름")
p_msg("이름2")

rst1 = testValue(100)
rst2 = testValue(200)

print("First", rst1)
print("Second", rst2)