## 문자열 형식화 ##

# 형식지정 문자열 [%s] - 문자열 [%d] - 정수 [%f] - 부동소수점 실수

name = input("이름 : ")
age = int(input("나이 : "))

print("%s은 %d세 입니다" % (name, age))

print("-" * 50)

# 고급 형식지정 문자열 [%20s] - 20칸을 차지하는 문자열 (공백을 앞에 붙임) [%-10d] - 10칸을 차지하는 숫자 (공백을 뒤에 붙임) [%.5f] - 소수점 아래 5자리까지 표시

# [format] 을 이용한 문자열 형식화

a, b = map(int, input("덧셈할 두 수를 입력 : ").split(" "))
c = "-" * 13

print("{0:>10}\n{1:<5}{2:>5}\n{3}\n{4:10}".format(a, "+", b, c, a + b))

print("-" * 50)

## 함수 ##

# [def]


def twotimes(x):
    y = x * 2
    return y


d = twotimes(2)
print(d)

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


inp = int(input("홀짝 : "))

print(oddOreven(inp))

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


inp = int(input("윤년? 평년? : "))

print(LY_NY(inp))

print("-" * 50)