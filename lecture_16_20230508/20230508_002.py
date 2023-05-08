p_book = {}

p_book["홍길동"] = "010-1234-5678" # 딕셔너리에 입력
p_book["강감찬"] = "010-4321-8765" # 딕셔너리에 입력
print(p_book)
print(p_book["홍길동"]) # 해당 키값 찾아서 출력
print(p_book["강감찬"]) # 해당 키값 찾아서 출력
print(p_book.keys()) 
print(p_book.values())

for key in p_book:
    print(key, p_book[key])