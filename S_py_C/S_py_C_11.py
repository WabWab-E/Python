### 도전문제 11 ###
# 다음과 같은 리스트에 [1,3,5,7,10]
# - 리스트의 마지막에 11을 추가
# - 리스트의 5와 7 사이에 6을 추가
# - 리스트의 7과 10 사이에 8,9를 추가 (단, 명령어 1개 사용)

listA = [1, 3, 5, 7, 10]
listA.append(11)
listA.insert(3, 6)
listA[5:5] = [8, 9]
print(listA)