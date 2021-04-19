## 재귀호출 ##

# ex) Factorial 구하기


def Factorial(num):
    if num > 1:
        return num * Factorial(num - 1)

    return 1


num = int(input("!"))

print(Factorial(num))

print("-" * 50)

## 2중 [for]문으로 2중 [list]선언

array_A = [[0 for col in range(5)] for row in range(10)]
print(array_A)
array_B = [[0] * 5 for i in range(10)]
print(array_B)
array_C = [[0] * 5] * 10
print(array_C)
