class Counter:
    def __init__(self, init_val = 0): # 생성자
        self.count = init_val

    def increment(self):
        self.count += 1

a = Counter()

a.increment()
print("카운트 실행 : ", a.count)

b = Counter(1000)

b.increment()
print("카운트 실행 : ", b.count)