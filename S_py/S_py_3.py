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

print("-" * 50)

# 불규칙한 모양의 2차원 리스트 자료 모두 출력

x = [[1, 2, 3], [4, 5], [6, 7, 8, 9, 10]]

for i in range(len(x)):
    for j in range(len(x[i])):
        print(x[i][j], end=" ")
    print()

print("-" * 50)

# 집합 자료형 [set]
# - 순서가 없음
# - 중복을 허용 X

aa = set([1, 2, 3, 4, 5])
bb = set("love")
cc = set()
dd = set("I love you")

ran = [8, 1, 6, 4, 8, 4, 6, 5, 4, 8, 7, 6]

print("aa = ", aa)
print("bb = ", bb)
print("cc = ", cc)
print("dd = ", dd, "\n")

print("-" * 50)

# 중복 제거 [set]

print("ran = ", ran)
print("중복 제거 : set(ran) = ", set(ran))

print("-" * 50)

# 합집함, 교집합, 차집합
# - [intersection] [union] [difference]
# - [     |      ] [  &  ] [    -     ]

y = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
z = set([3, 6, 9, 12, 15])

print("y이 %s 이고 z이 %s 일때, " % (y, z))

print("y와 z의 합집합은 ", y | z)  #     y.intersection(z)
print("y와 z의 교집합은 ", y & z)  #     y.union(z)
print("y와 z의 차집합은 ", y - z)  #     y.difference(z)
print("z와 y의 차집합은 ", y - z)  #     z.difference(y)

print("-" * 50)

# 집합 자료형에 값 추가, 제거

y.add(10)
print(y)
y.update([11, 12, 13])
print(y)
y.remove(13)
print(y)
