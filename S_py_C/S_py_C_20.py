### 도전문제 20 ###
# 3개의 수를 입력하면 "수들의 합", "수들을 제곱한 수들의 합"의
# 차이를 계산하는 함수 diffSum를 만든다 딘, 결과 >= 0


def diffSum(x, y, z):
    if (x + y + z) > (x ** 2 + y ** 2 + z ** 2):
        return (x + y + z) - (x ** 2 + y ** 2 + z ** 2)
    else:
        return (x ** 2 + y ** 2 + z ** 2) - (x + y + z)


x, y, z = map(int, input("3개의 수 입력 : ").split(" "))
print(diffSum(x, y, z))
