### 도전문제 13 ###
# 다음과 같은 리스트 [3,6,2,1,7,8,9,3,2,6,7,5,2]
# 사용자에게 값을 입력 받고 입력 값이 리스트에 있다면 인덱스 값을 출력
# 사용자가 입력한 값이 리스트에 여러 개 존재한다면 몇개가 있는지 출력
# 사용자가 입력한 값이 리스트에 없는 경우는 '값이 존재하지 않습니다' 라고 출력한다

listA = [3, 6, 2, 1, 7, 8, 9, 3, 2, 6, 7, 5, 2]
key = None

while [True]:
    key = int(input("값을 입력 : "))

    if key in listA:
        if listA.count(key) > 1:
            print(listA.count(key), "개")
            break
        else:
            print(listA.index(key))
            break
    else:
        print("값이 존재하지 않습니다")
