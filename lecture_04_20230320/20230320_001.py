# distance = 40*10**12 # 책의 예제 값
# distance = 40*10**6 # 교수님 예제 값
distance = int(input("입력 = "))
light_speed = 300000

# secs = distance / light_speed
# light_year = secs / (60 * 60 * 24 *365)


# print("시간(초) :", secs)
# print("광년 :", light_year)

r_dist = distance // light_speed
print("시간은", r_dist, "초")

minute =  r_dist // 60 # 나머지의 몫만 표현
# minute =  r_dist / 60 #==> 나머지의 몫에서 소수점까지 표현 
sec = r_dist % 60 # 나머지 연산자를 활용

print("시간은", minute, "분", sec, "초")