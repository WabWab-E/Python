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
    elif month == 2:
        return 28
    else:
        return "Error : 월 입력 오류"


#### 3 #### - 종합


thirty = [4, 6, 9, 11]
thirtyOne = [1, 3, 5, 7, 8, 10, 12]


def LYNY_Days(year, month):
    is_Leap_year = False

    if year % 4 == 0:
        is_Leap_year = True
    elif year % 100 == 0:
        is_Leap_year = True
        if year % 400 == 0:
            is_Leap_year = True

    if month in thirty:
        return 30
    elif month in thirtyOne:
        return 31
    elif month == 2:
        if is_Leap_year:
            return 29
        else:
            return 28
    else:
        print("Error : 월 입력 오류")


year, month = map(int, input("년 월 : ").split())

print(LYNY_Days(year, month))
