# laptop
a, b, c = int(input()), int(input()), int(input())
# wharehouse
x, y, z = int(input()), int(input()), int(input())

check1 = (a // x) * (b // y) * (c // z)
check2 = (a // x) * (b // z) * (c // y)
check3 = (a // z) * (b // y) * (c // x)
check4 = (a // z) * (b // x) * (c // y)
check5 = (a // y) * (b // z) * (c // x)
check6 = (a // y) * (b // x) * (c // z)

result = (max(check1, check2, check3, check4, check5, check6))

print(result)
