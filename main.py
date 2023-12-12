#Урок №7. Списки
#Homework 1
n = int(input())
spisok = []

for i in range(n):
    a = int(input())
    spisok.append(a)
spisok.reverse()
print(*spisok)

#Homework 2
n = int(input())
tmp = list(map(int, input().split()))
tmp.insert(0, tmp.pop())
print(*tmp)


#Homework 3
n = int(input())
m = int(input())
a = []
b = []

for i in range(n):
    a.append(int(input()))

for u in range(len(a)):
    if a[u] + min(a) <= m:
        b += [[a[u], min(a)]]
        a[u] += m
        a[a.index(min(a))] += m
    else:
        if a[u] > m:
            continue
        else:
            b += [[a[u]]]
print(len(b))
