a, b = int(input()), int(input())
'''
if a > b:
    for i in range(a, b - 1, -1):
        print(i)
else:
    for i in range(a, b + 1):
        print(i)
'''
step = 1
if a > b:
    step = -1

for i in range(a, b + step, step):
    print(i)