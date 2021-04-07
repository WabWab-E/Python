### 도전문제 12 ###
# 다음과 같은 리스트 lista = [1,2,3,4,5,6,7,8]
# - 사용자에게 값을 입력 받고, 해당 값의 인덱스 값을 출력
# - 존재하지 않는 수라면 '값이 리스트에 없습니다'를 출력

listA = [1, 2, 3, 4, 5, 6, 7, 8]
key = None

while [True]:
    key = int(input("찾아낼 값을 입력 : "))

    if key in listA:
        print("%d 번째 자리에 있습니다" % (listA.index(key) + 1))
        break
    else:
        print("값이 리스트에 없습니다")
