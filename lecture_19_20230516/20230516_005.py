infile = open("d://University/Develop/2023-1_Python/lecture_19_20230516/proverbs.txt", "r", encoding="UTF-8")


for line in infile:
    line = line.rstrip() # \n 제거
    word_list = line.split()
    # print(line)
    for word in word_list:
        print(word)


infile.close()
