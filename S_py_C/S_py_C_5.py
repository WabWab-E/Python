### 도전문제 5 ###
# 코드 게이트 입장료 계산
# [개인] : 50000원 [단체] : 10000원
# 단체는 10인 이상부터

people = int(input("입장 인원을 입력하세요 : "))

if people < 10:
    print("단체할인 미적용 ", people * 50000, "원 입니다.")
else:
    print("단체할인 적용 ", people * 10000, "원 입니다.")

print("-------------------------------------------------------")