### 도전문제 18 ###
# - 윤년 평년을 구분하는 함수
# - 한 달의 일 수를 구하는 함수


#### 1 #### - 윤년, 평년
def LY_NY(year):
    leap_YR = "윤년"
    normal_YR = "평년"

    if year % 4 == 0:
        return leap_YR
    elif year % 100 == 0:
        if year % 400 == 0:
            return leap_YR
        else:
            return normal_YR
    else:
        return normal_YR


#### 2 #### - 한 달의 일 수

thirty = [4, 6, 9, 11]
thirtyOne = [1, 3, 5, 7, 8, 10, 12]


def days(month):
    if month in thirty:
        return 30
    elif month in thirtyOne:
        return 31
    else:
        return 28


#### 3 #### - 종합


thirty = [4, 6, 9, 11]
thirtyOne = [1, 3, 5, 7, 8, 10, 12]


def LYNY_Days(x, y):
    is_Leap_year = False

    if x % 4 == 0:
        is_Leap_year = True
    elif x % 100 == 0:
        is_Leap_year = True
        if x % 400 == 0:
            is_Leap_year = True

    if y in thirty:
        return 30
    elif y in thirtyOne:
        return 31
    else:
        if is_Leap_year:
            return 29
        else:
            return 28


year, month = map(int, input("년 월 : ").split())

print(LYNY_Days(year, month))
