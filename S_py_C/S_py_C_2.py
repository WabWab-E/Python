### 도전문제 2 ###
# 두 수를 입력 받아서 더한 값이 100 이상이면, '100 이상입니다.' 라고 출력한다.
# 두 수의 합이 100 미만이라면 '100 미만입니다.' 라고 출력한다

firstNum = int(input("첫 번째 값 : "))
secondNum = int(input("두 번째 값 : "))

if firstNum + secondNum >= 100:
    print("100 이상입니다.")
else:
    print("100 미만입니다.")
