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

## 람다 함수 (익명함수) [lambda] - lambda 매개변수 : 리턴값
# 람다 표현식 자체 호출 시 - (lambda 매개변수 : 리턴값) (인수)

# def
def plus_ten(x):
    return x + 10


print(list(map(plus_ten, [1, 2, 3])))

print("=" * 30)

# lambda
print(list(map(lambda x: x + 10, [1, 2, 3])))

print("=" * 30)

# lambda + input
print(list(map(lambda x: x + 10, map(int, input("수 입력 : ").split()))))

print("=" * 30)
# 람다 함수에는 조건식도 넣을 수 있다 #

oneToTen = list(range(1, 11))

print(list(map(lambda x: str(x) if x % 2 == 0 else x, oneToTen)))

print("-" * 50)

# [map]은 리스트 등 반복 가능한 객체를 여러 개 넣을 수 있다 #

listA = [1, 2, 3, 4, 5]
listB = [2, 4, 6, 8, 10]
print(list(map(lambda x, y: x * y, listA, listB)))

print("-" * 50)

## [filter] ##

# [def + filter]
def f(x):
    return x > 5 and x < 10


listA_f = [8, 5, 7, 1, 0, 9, 4, 6, 11, 2]
print(list(filter(f, listA_f)))

# [lambda + filter]

listA_f = [8, 5, 7, 1, 0, 9, 4, 6, 11, 2]
print(list(filter(lambda x: x > 5 and x < 10, listA_f)))

# [리스트 표현식] {가독성 ++ , 속도 ++}

print([i for i in listA_f if i > 5 and i < 10])
