k = int(input())

if k <= 9:
    if k % 3 == 0 or k % 5 == 0:
        print("YES")
    else:
        print("NO")
else:
    print("YES")
