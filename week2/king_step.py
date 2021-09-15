x1, y1 = int(input()), int(input())
x2, y2 = int(input()), int(input())

x = x2 - x1
y = y2 - y1

if abs(x) == 1 and abs(y) == 1:
    print("YES")
elif (abs(x) == 1 and y == 0) or (x == 0 and abs(y) == 1):
    print("YES")
else:
    print("NO")
