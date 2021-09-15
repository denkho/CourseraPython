num1, num2 = int(input()), int(input())

for i in range(num1, num2 + 1):
    if (i // 100) % 10 * 10 + (i // 100) // 10 == i % 100:
        print(i)
