### 도전문제 21 ###
# 전역변수 m을 만들고 20번 문제에서 만든 diffSum 함수를 실행시킨뒤
# 결과값이 기존의 m 보다 클 때 큰 값을 m에 대입하는 diffSum2 함수 생성

m = 0


def diffSum(x, y, z):
    numSum = x + y + z
    squareSum = (x ** 2) + (y ** 2) + (z ** 2)

    rv = abs(numSum - squareSum)

    diffSum2(rv)
    return rv


def diffSum2(x):
    global m

    if x > m:
        m = x

    print("현재 수 : ", x, end=" ")


while True:
    xx, yy, zz = map(int, input("3개의 수 입력 : ").split(" "))

    if xx + yy + zz == 0:
        print("종료")
        break
    diffSum(xx, yy, zz)

    print("가장 컸던 수 : ", m)
