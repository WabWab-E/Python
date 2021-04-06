# 에러를 찾아보세요~~

print("안녕")

print("난 김상일이라고 해")
print("넌 누구니?")

"""
여긴 주석문이에요.
내가 작성한 코드를 나중에 유지보수하거나, 다른 사람이 작성한 코드를 읽을 때 주석이 있다면 코드를 이해하는데 큰 도움이 됩니다.
"""

b = 100
if b >= 10:
    print("a는 10보다 크다.\n")
    b = 0

print("프로그램을 종료합니다.\n")

e = f = g = 10

m = 1
m = +1  # m=m+1
print(m)
print()

a = input("인사말을 입력해주세요 : ")
print(a)

b = int(input("첫 번째 정수를 입력해주세요 :"))
c = int(input("두 번째 정수를 입력해주세요 :"))
print(b + c)

a, b = input("학교명과 성명을 입력하세요 :").split(",")
print("학교명:", a)
print("성명:", b)

a, b = map(int, input("정수 2개를 입력하세요 :").split())
print(a + b)

print("저 산 위에 바위는 크다", end="!")
print("내 머리도 크다", end="!")

a, b = 10, 5
print(a == b)
print(a != b)

print("성공 !!!  당신은 코딩 천재입니다")
