numbers = list(map(int, input().split()))

for pos in range(1, len(numbers)):
    if numbers[pos] > numbers[pos - 1]:
        print(numbers[pos], end=" ")
