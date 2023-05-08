eng_dic = dict()


eng_dic['one'] = "하나"
eng_dic['two'] = "둘"
eng_dic['three'] = "셋"
# eng_dic['one'] = "하나"


print(eng_dic)
wd = input("검색 : ")
print(wd, " : ", eng_dic[wd])