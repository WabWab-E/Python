### 도전문제 15 ###
# 두 주사위의 값을 난수로 지정하여 두 주사위의 값이 같아질 때까지 반복
# 두 주사위의 값이 같아지면 몇번 반복했는 지 출력

import random

firstDice = 1
secondDice = 2

count = 0

while firstDice != secondDice:

    firstDice = random.randint(1, 6)
    secondDice = random.randint(1, 6)
    print("첫 번째 주사위 : %d | 두 번째 주사위 : %d " % (firstDice, secondDice))
    count += 1

print("두 주사위 값이 같음 %d번 반복" % count)
