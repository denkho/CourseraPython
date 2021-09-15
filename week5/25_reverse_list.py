numbers = list(map(int, input().split()))

for i in range(len(numbers) // 2):
    numbers[i], numbers[len(numbers) - 1 - i] = \
        numbers[len(numbers) - 1 - i], numbers[i]

for number in numbers:
    print(number, end=" ")
