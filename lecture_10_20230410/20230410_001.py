import random

# random 함수 살펴보기

# # n = random.randint(1, 10)
# # n = random.randrange(5)
# # print(n)
# for i in range(5):
#     n = random.randrange(5) # 0 ~ 4
#     print(n)


# random 함수와 if문 사용하기

# num = int(input("입력"))
# ok = random.choice([True, False])
# if num >= 6 and num < 9 and ok:
#     print("잘했어요")
# else:
#     print("잘못했어요")


# 로그인 프로그램

# id = "idoko" # 실제론 DB에서 아이디 값 가져옴
# vals = input("아이디 입력 : ")

# if vals == id:
#     print("환영합니다. ")
# else:
#     print("아이디를 찾을 수 없음")


# 축구게임
vals = int(input("입력 : "))
ok = random.randrange(3) # random.randint(0,2)

if vals == ok:
    print("패널티 킥 실패 (노골)")
else:
    print("패널티 킥 성공 (골)")


