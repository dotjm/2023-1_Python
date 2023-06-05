# 주관식 시험에선 안낼 듯...?

print(abs(-100)) # 절대값

mlist = [1, 2, 0] # all -> and type => 하나라도 false인 경우에 => false 반환 0 -> False
print(all(mlist))

mlist = [False, 0, 0]
print(any(mlist)) # any -> or type -> 하나라도 True면 True 반환

# rst = input("입력 : ")
# rst = eval(rst) # 수식 입력 함수
# print("결과", rst)

mlist = [1, 2, 0] 
print(sum(mlist)) # 항목 더하기

mlist = [1, 2, 9] 
print(len(mlist)) # 항목 항목수
print(len("python")) # 항목 길이

s = "abcdefg"
print(list(s))

mlist = [1, 2, 9]
print(max(mlist), min(mlist))

def sq(n):
    return n * n *n

mlist = [1, 2, 9]
rst = list(map(sq, mlist))
print(rst)

mlist = ['ok', 'pk', 'rk']
print(list(enumerate(mlist))) # 열거형

def r(x):
    return x > 3

mlist = [1, 2, 9]
# rst = filter(r, (1, 2, 9))
rst = filter(r, mlist)
print(list(rst))

mlist = [1, 2, 9, 5, 3]
# print(mlist.sort()) # 동작 X -> sort는 return 값이 없는 듯
mlist.sort()
print(mlist)

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return "<이름: %s, 나이: %s>" % (self.name, self.age) # __str__도 있는데 리스트에서 활용위해서 한듯 이라고 함
    
    def __str__(self):
        return "<이름: %s, 나이: %s>" % (self.name, self.age) 
    
def keyAge(person):
    return person.age

people = [Person("홍길동", 20), Person("김철수", 350), Person("최자영", 38)]
print(sorted(people, key = keyAge))
