infile = open("d://University/Develop/2023-1_Python/lecture_19_20230516/test_phones.txt", "r", encoding="UTF-8")

# lines = infile.read()
# lines = infile.readlines()
# print(lines)

for line in infile:
    # print(line)
    line = line.rstrip()
    print(line)


infile.close()