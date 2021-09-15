a = int(input())
b = int(input())
c = int(input())
d = int(input())

if c == 0 and d == 0:
    print("NO")
elif a == 0 and b == 0:
    print("INF")
elif a == 0:
    print("NO")
elif c == 0:
    if (-b // a) == (-b / a):
        print(-b // a)
    else:
        print("NO")
elif (b / a) == (d / c):
    print("NO")
else:
    if (-b // a) == (-b / a):
        print(-b // a)
    else:
        print("NO")
