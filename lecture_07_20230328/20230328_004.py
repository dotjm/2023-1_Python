slist = ["서울", "인천", "천안", "대구", "부산"]
nslist = []

print(slist)
slist.append("광주")
print(slist)

slist.remove("부산")
print(slist)


nslist.append("광주")
print("1. nslist => ", nslist)
nslist.remove("광주")
print("2. nslist => ", nslist)