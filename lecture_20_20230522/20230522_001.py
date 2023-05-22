import random

guesses = ""
tries = 10

infile = open("D://University/Develop/2023-1_Python/lecture_20_20230522/words.txt", "r", encoding="UTF-8")
lines = infile.readlines()
word = random.choice(lines).rstrip()
# print(word)

while tries > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end="")
        else:
            print("_", end="")
            failed += 1
    print("")    
    if failed == 0:
        print("사용자 승리")
        break
    in_char = input("단어 추측 : ")
    guesses += in_char
    if in_char not in word:
        tries -= 1
        print("틀렸습니다")
        print(tries, "번의 기회가 남았습니다")
        if tries == 0:
            print("사용자 패배 정답은 '", word, "'")



infile.close()