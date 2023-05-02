# lista = []

# for i in range(3):
#     in_val = input("값 입력 : ")
#     lista.append(in_val)

# while True:
#     in_val = input("값 입력 : ")
#     if in_val == "":
#         break
#     else:
#         lista.append(in_val)

# 성적 처리 프로그램
score = []
over80count = 0
for i in range(5):
    in_val = int(input("값 입력 : "))
    score.append(in_val)
    if in_val >= 80:
        over80count += 1
print(score)
print("최고 점수 : ", max(score))
print("최저 점수 : ", min(score))
print("평균 점수 : ", sum(score)/len(score))
print("80점 이상인 학생 수 : ", over80count)


