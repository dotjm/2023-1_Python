score_dic = {
    "Kim" : [99, 83, 95],
    "Oh" : [99, 93, 95],
    "Choi" : [88, 73, 95]
}

# for na in score_dic:
#     print(na)

# for name in score_dic:
#     print(name, score_dic[name])

for name, score in score_dic.items():
    # print(name, score)
    print(name, sum(score)/len(score))