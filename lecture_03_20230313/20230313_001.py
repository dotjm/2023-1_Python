a = int(input("첫 번째 정수를 입력하시오 : ")) # input으로 String 값을 받아서 int로 형변환
b = int(input("두 번째 정수를 입력하시오 : ")) # input으로 String 값을 받아서 int로 형변환

c = a ** b # a의 b 제곱 구하기
print(a, "의 ", b, "승은 ", c, "입니다. ") # 결과 출력

sum = a + b # 합 구하기 
print(a, "와 ", b, "의 합은 ", sum, "입니다. ") # 결과 출력
print("합은 ", sum) # 결과 출력

score = 10
# score = score + 1 # 변수에 1 더하기
score += 1 # 위와 동일한 실행결과
print(score)
