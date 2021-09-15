v, n = list(map(int, input().split()))
a = list()
number = 0
for i in range(n):
    a.append(int(input()))
a.sort()
s = 0
for i in a:
    s += i
    if s <= v:
        number += 1

print(number)
