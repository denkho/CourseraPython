a1, b1 = int(input()), int(input())
a2, b2 = int(input()), int(input())

if a1 + b1 < a2 + b2:
    if (a1 + b1) % 2 == (a2 + b2) % 2:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
