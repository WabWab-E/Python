# 리스트에 요소 추가 (리스트 중첩, 접근) [append]

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
a.append(b)
b.append(c)
print(a)
print(a[3])
print(a[3][3])

print("-" * 50)

# 리스트에 다중 요소 추가 [extend]

d = [1, 2, 3, 4, 5]
print(d)
d.extend([6, 7, 8])
print(d)

print("-" * 50)

# 리스트의 특정위치에 요소 추가 [insert]

e = [10, 20, 40, 50]
e.insert(2, 30)
print(e)
e.insert(5, 60)
print(e)

print("-" * 50)

# 리스트의 특정위치에 요소 추가 [insert]

l1 = [1, 2, 7, 8]
l2 = [1, 2, 7, 8]
l1.insert(2, [3, 4, 5, 6])
print(l1)
l2[2:2] = [3, 4, 5, 6]
print(l2)

print("-" * 50)

# 리스트 삽입 도전문제
# 다음과 같은 리스트에 [1,3,5,7,10]
# - 리스트의 마지막에 11을 추가
# - 리스트의 5와 7 사이에 6을 추가
# - 리스트의 7과 10 사이에 8,9를 추가 (단, 명령어 1개 사용)

f = [1, 3, 5, 7, 10]
f.append(11)
f.insert(3, 6)
f[5:5] = [8, 9]
print(f)

print("-" * 50)

# 리스트 요소 삭제 [pop] - 인덱스 위치를 찾아 제거

g = [1, 2, 3, 4, 5]
g.pop()
print(g)
g.pop()
print(g)

h = [1, 2, 3, 4, 5]
h.pop(2)
print(h)
del h[1]
print(h)

print("-" * 50)

# 리스트 요소 삭제 [remove] - 값을 찾아 제거

i = [1, 10, 50, 2, 20]
i.remove(50)
print(i)

print("-" * 50)

# ValueError 방지를 위한 코드

j = [1, 32, 8, 4, 5, 7]
print(j)
while True:
    data = int(input("리스트에서 삭제할 값을 입력 : "))
    if data in j:
        j.remove(data)
        print(j)
        break
    else:
        print("존재하지 않는 수 입니다.")

print("-" * 50)

# 리스트 정보조회 [index]

k = [10, 20, 30, 40, 50]
print(k.index(40))

print("-" * 50)

# 리스트 도전문제
# 다음과 같은 리스트 lista = [1,2,3,4,5,6,7,8]
# - 사용자에게 값을 입력 받고, 해당 값의 인덱스 값을 출력
# - 존재하지 않는 수라면 '값이 리스트에 없습니다'를 출력

lista = [1, 2, 3, 4, 5, 6, 7, 8]
key = None

while [True]:
    key = int(input("찾아낼 값을 입력 : "))

    if key in lista:
        print(lista.index(key))
        break
    else:
        print("값이 리스트에 없습니다")

print("-" * 50)

# 찾으려는 값이 여러개라면 [index]를 사용한다면 가장 작은 인덱스 값이 나옴

l = [10, 10, 20, 30, 30, 30, 40]
print(l.index(10))

print("-" * 50)

# 특정 값의 갯수 구하기 [count]

m = [1, 2, 3, 3, 4, 5, 6, 4, 4]
print(m.count(4))

print("-" * 50)

# 리스트 오름,내림차 순으로 정렬

n = [6, 7, 8, 2, 1, 5, 4, 3]
n.sort()  # 오름차순
print(n)
n.sort(reverse=True)  # 내림차순
print(n)

print("-" * 50)

# 리스트를 반대로 뒤집기

n.reverse()
print(n)

print("-" * 50)

# 리스트 종합 도전문제
# 다음과 같은 리스트 존재 test = [3,6,2,1,7,8,9,3,2,6,7,5,2]
# 사용자에게 값을 입력 받고 입력 값이 리스트에 있다면 인덱스 값을 출력
# 사용자가 입력한 값이 리스트에 여러 개 존재한다면 몇개가 있는지 출력
# 사용자가 입력한 값이 리스트에 없는 경우는 '값이 존재하지 않습니다' 라고 출력한다

test = [3, 6, 2, 1, 7, 8, 9, 3, 2, 6, 7, 5, 2]
key = None

while [True]:
    key = int(input("값을 입력 : "))

    if key in test:
        if test.count(key) > 1:
            print(test.count(key), "개")
            break
        else:
            print(test.index(key))
            break
    else:
        print("값이 존재하지 않습니다")

print("-" * 50)

# 리스트의 할당 - EX) a = [1,2,3] | b = a
# 리스트의 할당은 한 메모리의 구조를 공유하는 형태

o = [1, 2, 3, 4, 5]
p = o
print(id(o))  # ┬────────────── 메모리 주소값을 찾는 메소드 (할당이라 주소가 같음)
print(id(p))  # ┘
print(o)
print(p)
p[3] = 40
print(o)
print(p)

print("-" * 50)

# 리스트의 복사 - EX) a = [1,2,3] | b = a.copy()

q = [1, 2, 3, 4, 5]
r = q.copy()
print(id(q))
print(id(r))
print(q)
print(r)
r[3] = 400
print(q)
print(r)

print("-" * 50)

# 리스트 내용을 모두 삭제 [clear]

s = [1, 2, 3, 4, 5]
t = [4, 5, 6, 7, 8]
s.clear()
del t[:]
print(s)
print(t)

print("-" * 50)

# 2차원 리스트

u = [[10, 20], [30, 40], [50, 60]]
print(u)
print(u[0][0])
print(u[1][1])
print(u[2][1])
u[1][0] = 88
print(u)

print("-" * 50)

# 불규칙 2차원 리스트 & 동적 추가

v = [[10, 20, 30], [40, 50], [60, 70, 80, 90]]
print(v)

v[0].append(111)
print(v)

v[0].append(222)
print(v)

v[2].extend([333, 444])
print(v)

# 2차원 리스트 도전문제
# - 5명의 이름, 전화번호, 나이를 입력 받아서 2차원 리스트에 저장하는 프로그램 작성
# - 5명의 이름은 반복문으로 처리

w = []
temp1 = temp2 = temp3 = None

for i in range(5):
    temp1, temp2, temp3 = input("[이름] [전화번호] [나이] : ").split(" ")
    w.append([temp1, int(temp2), int(temp3)])

for i in range(5):
    print(w[i])

# 불규칙한 모양의 2차원 리스트 자료 모두 출력

x = [[1, 2, 3], [4, 5], [6, 7, 8, 9, 10]]

for i in range(len(x)):
    for j in range(len(x[i])):
        print(x[i][j], end=" ")
    print()