### 도전문제 14 ###
# - 5명의 이름, 전화번호, 나이를 입력 받아서 2차원 리스트에 저장하는 프로그램 작성
# - 5명의 이름은 반복문으로 처리

listA = []
name = phone = age = None

for i in range(5):
    name, phone, age = input("[이름] [전화번호] [나이] : ").split(" ")
    listA.append([name, phone, int(age)])

for i in range(5):
    print(listA[i])