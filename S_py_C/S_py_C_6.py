### 도전문제 6###
# 숫자 5개를 입력받고 입력 받은 수 중에서 가장 큰 수를 출력

#### 1 #### - [for문 + max]

listA = [0, 0, 0, 0, 0]

for i in range(len(listA)):
    listA[i] = int(input("5개의 수를 입력 : "))

print(max(listA))

print("-" * 50)

#### 2 #### - [for(append) + max]

listB = [0, 0, 0, 0, 0]

for i in range(len(listB)):
    listB.append(int(input("5개의 수를 입력 : ")))

print(max(listB))

print("-" * 50)

#### 3 #### - [map,split함수 + max함수]

listC = [0, 0, 0, 0, 0]

listC = map(int, input("5개의 수를 입력 (예시 - 1,2,3,4,5) : ").split(","))

print(max(listC))

#### 4 #### - [Algorithm]

listD = [0, 0, 0, 0, 0]
max_num = 0

for i in range(len(listD)):
    listD[i] = int(input("5개의 수를 입력 : "))

for j in range(len(listD)):

    if max_num < listD[i]:
        max_num = listD[i]

print(max_num)