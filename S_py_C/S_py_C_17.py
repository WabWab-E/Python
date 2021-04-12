### 도전문제 17 ###
# 홀짝 출력 함수


def oddOReven(x):
    odd = "홀수"
    even = "짝수"

    if x % 2 == 0:
        return even
    else:
        return odd


num = int(input("홀? 짝? : "))

print(oddOReven(num))

