l1, r1 = int(input()), int(input())
l2, r2 = int(input()), int(input())
l3, r3 = int(input()), int(input())
match1 = 1
match2 = 2
match3 = 3

result = 0

# проверка соприкосновения всех спичек
if r1 >= l2 and r2 >= l3:
    print(0)
