## 문자열 형식화 ##

# 형식지정 문자열 [%s] - 문자열 [%d] - 정수 [%f] - 부동소수점 실수

name = input("이름 : ")
age = int(input("나이 : "))

print("%s은 %d세 입니다" % (name, age))

print("-" * 50)

# 고급 형식지정 문자열 [%20s] - 20칸을 차지하는 문자열 (공백을 앞에 붙임) [%-10d] - 10칸을 차지하는 숫자 (공백을 뒤에 붙임) [%.5f] - 소수점 아래 5자리까지 표시

# [format] 을 이용한 문자열 형식화

firstNum, secondNum = map(int, input("덧셈할 두 수를 입력 : ").split(" "))
line = "-" * 13

print(
    "{0:>10}\n{1:<5}{2:>5}\n{3}\n{4:10}".format(
        firstNum, "+", secondNum, line, firstNum + secondNum
    )
)

print("-" * 50)

## 함수 ##

# [def]


def twotimes(x):
    y = x * 2
    return y


print(twotimes(2))

print("-" * 50)

## 도전문제 ##
# 1 - 홀짝 출력 함수
# 2 - 윤년, 평년 함수

## 1 ##


def oddOreven(x):
    odd = "홀수"
    even = "짝수"

    if x % 2 == 0:
        return even
    else:
        return odd


num = int(input("홀짝 : "))

print(oddOreven(num))

print("-" * 50)

## 2 ##


def LY_NY(x):
    leap_YR = "윤년"
    normal_YR = "평년"

    if x % 4 == 0:
        return leap_YR
    elif x % 100 == 0:
        if x % 400 == 0:
            return leap_YR
        else:
            return normal_YR
    else:
        return normal_YR


ly_Year = int(input("윤년? 평년? : "))

print(LY_NY(ly_Year))

print("-" * 50)

## 3 ##

thirty = [4, 6, 9, 11]
thirtyOne = [1, 3, 5, 7, 8, 10, 12]


def days1(month):
    if month in thirty:
        return 30
    elif month in thirtyOne:
        return 31
    else:
        return 28


print("-" * 50)

## 4 ##

thirty = [4, 6, 9, 11]
thirtyOne = [1, 3, 5, 7, 8, 10, 12]


def days2(x, y):
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

print(days2(year, month))

print("-" * 50)

## 람다 함수 (익명함수) [lambda] - lambda 매개변수 : 리턴값
# 람다 표현식 자체 호출 시 - (lambda 매개변수 : 리턴값) (인수)
