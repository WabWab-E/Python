### 도전문제 8 ###
# 두 수를 입력받아 두 수가 같으면 중지되는 [while]

#### 1 ####

firstNumA = 0
secondNumA = 1

while firstNumA != secondNumA:
    firstNumA = int(input("[1] 첫 번째 수 : "))
    secondNumA = int(input("[1] 두 번째 수 : "))

#### 2 ####

firstNumB = None
secondNumB = None

while True:
    firstNumB = int(input("[2] 첫 번째 수 : "))
    secondNumB = int(input("[2] 두 번째 수 : "))
    if firstNumB == secondNumB:
        break