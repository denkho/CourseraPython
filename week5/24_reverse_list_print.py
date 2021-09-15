numbers = list(map(int, input().split()))

for i in range(len(numbers) - 1, -1, -1):
    print(numbers[i], end=" ")
