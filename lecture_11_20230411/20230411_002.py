# while 조건:
#     반복문장
#     여기에 조건 탈피 문장

pas = "asdf"

in_val = input("암호 입력 : ")

while in_val != pas:
    print("암호를 확인해주세요. ")
    in_val = input("입력 : ")

print("로그인 성공")
