# lists = ["a", "b", "c", "d"]
#           0    1    2    3   첨자 (인덱스)
# lists.append("k")

# print(lists)

# 공백 리스트에 추가하기
# alist = []
# alist.append("ok")
# print(alist)
# alist.append("rk")
# print(alist)

# 리스트 값 접근하기
# lists = ["a", "b", "c", "d"]

# for i in lists:
#     print(i, end=" ")

# print("\n")

# for i in range(len(lists)):
#     print(lists[i])

# 슬라이싱 : 끝 값 = 변수 - 1
# lists = ["a", "b", "c", "d"]
# print(lists[0:3])
# print(lists[1:2])
# print(lists[2:4])
# print(lists[:3])
# print(lists[2:])
# print(lists[:])

# 리스트 값 변경
lists = ["a", "b", "c", "d"]

lists[1] = "k" # 값 변경 (대체) (값 개수 그대로)
print(lists)

lists.insert(1, "ok") # 해당 자리에 값 추가 (값 개수 +  1)
print(lists)

lists.remove("c") # 처음 값만 지워짐
print(lists)

if "ok" in lists:
    lists.remove("ok")
print(lists)

del lists[1]
print(lists)

print(lists.pop())

# 숙제
# 스택 구조를 작성하시오
# 입력 받는 부분
# 출력 하는 부분 을 모두 작성

print(lists.index("a"))

# 리스트 정렬
lists = ["a", "d", "b", "c"]
print(lists)
lists.sort() # 내장 함수 사용, 앞으로는 직접 만들어 활용, 오름차순
print(lists)

lists.sort(reverse=True) # 내림차순
print(lists)

num = [10, 3, 6, 1, 5, 4, 2, 7, 8, 9]
a_n = sorted(num)
print(a_n)