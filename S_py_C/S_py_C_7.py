### 도전문제 7 ###
# 다음과 같은 리스트 중 sangmi = ['현찬','화준','상욱','승현','현빈']
# 사용자에게 이름을 입력 받고 리스트에 일치하는 이름이 있다면 몇 번째에 있는 지 출력
# 없다면 '리스트에 없는 이름입니다' 라고 출력
friends = ["현찬", "화준", "상욱", "승현", "현빈"]

name = input("이름을 입력 : ")
count = 0

for i in friends + [""]:
    if name == i:
        count += 1
        break
    else:
        count += 1

if count > 5:
    print("리스트에 없는 이름입니다.")
else:
    print(count, "번째에 존재!")
