### 도전문제 4 ###
# 생년월일 입력
# 입력받은 생년월일을 연, 월, 일로 나눠서 출력
# 20세기 인간, 21세기 인간 구별

date_birth = input("생년원일 입력 (YYYYMMDD):")

year, month, day = date_birth[0:4], date_birth[4:6], date_birth[6:8]

print(year, "년")
print(month, "월")
print(day, "일")

if int(year) >= 2000:
    print("21세기 인간")
else:
    print("20세기 인간")
