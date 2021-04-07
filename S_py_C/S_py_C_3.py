### 도전문제 3 ###
# 몇 시인지 입력받고
# 8 ~ 9 사이라면 아침
# 11 ~ 13 사이라면 점심
# 17 ~ 20 사이라면 저녁
# 그 외는 식사시간 아님 출력

time_Hour = int(input("시간을 입력하세요 : "))

if 8 <= time_Hour <= 9:
    print("아침식사시간")
elif 11 <= time_Hour <= 13:
    print("점심식사시간")
elif 17 <= time_Hour <= 20:
    print("저녁식사시간")
else:
    print("식사시간 아님")