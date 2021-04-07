### 도전문제 10 ###
# 다음과 같이 출력

## OAAAAAO ##
## OAAAAAO ##
## OAAAAAO ##
## OAAAAAO ##
## OAAAAAO ##

for i in range(5):
    for j in range(7):
        if j == 0 or j == 6:
            print("O", end="")
        else:
            print("A", end="")
    print()

print("-" * 50)

## OOOOOOO ##
## AAAAAAA ##
## OOOOOOO ##
## AAAAAAA ##
## OOOOOOO ##

for i in range(5):
    for j in range(7):
        if i % 2 == 0:
            print("O", end="")
        else:
            print("A", end="")
    print()

print("-" * 50)


## A      ##
## AA     ##
## AAA    ##
## AAAA   ##
## AAAAA  ##
## AAAAAA ##

for i in range(6):
    for j in range(6):
        if j <= i:
            print("A", end="")
    print()
