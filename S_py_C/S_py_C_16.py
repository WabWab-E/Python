### 도전문제 16 ###
# 로또번호를 추첨하는 프로그램
# [randint] [choice] [shuffle] 사용하여 각각 출력

import random

#### 1 #### - [randint]

LottoListA = [1, 2, 3, 4, 5, 6]

for i in range(len(LottoListA)):
    LottoListA[i] = random.randint(1, 45)
    if LottoListA[i] in LottoListA:
        i -= 1

LottoListA.sort()
print(LottoListA)

#### 2 #### - [choice]

LottoListB = [0, 0, 0, 0, 0, 0]

num = list(range(1, 46))

for i in range(len(LottoListB)):
    LottoListB[i] = random.choice(num)
    if LottoListA[i] in LottoListA:
        i -= 1

LottoListB.sort()
print(LottoListB)

#### 3 #### - [shuffle]

LottoListC = []

num = list(range(1, 46))

random.shuffle(num)

LottoListC.extend(num[1:7])

LottoListC.sort()
print(LottoListC)
