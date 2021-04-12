### 도전문제 21 ###
# 전역변수 m을 만들고 20번 문제에서 만든 diffSum 함수를 실행시킨뒤
# 결과값이 기존의 m 보다 클 때 큰 값을 m에 대입하는 diffSum2 함수 생성

m = 0

xx, yy, zz = map(int, input("3개의 수 입력 : ").split(" "))


def diffSum(x, y, z):
    result = 0

    if (x + y + z) > (x ** 2 + y ** 2 + z ** 2):
        result = (x + y + z) - (x ** 2 + y ** 2 + z ** 2)
        diffSum2(result)
        return result

    else:
        result = (x ** 2 + y ** 2 + z ** 2) - (x + y + z)
        diffSum2(result)
        return result


def diffSum2(x):
    global m

    if x > m:
        m = x
        return
    else:
        return


diffSum(xx, yy, zz)
print(m)