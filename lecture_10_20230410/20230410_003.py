abc = [1, 2, 3, 4, 5]

for i in abc: # for i in [1, 2, 3, 4, 5]:
    # print(i)
    print("U", 9*i)

for i in [1, 2, 3, 4, 5]:
    # print(i)
    print("M", 9*i)  

for i in range(5):
    # print(i)
    print("L", 9*(i+1))

for i in range(1, 6):
    # print(i)
    print("L2", 9*i)

for i in range(1, 6, 1): # 이게 중요
    # print(i)
    print("L2-step", 9*i)