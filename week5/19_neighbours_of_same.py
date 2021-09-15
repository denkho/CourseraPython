numbers = list(map(int, input().split()))

for pos in range(1, len(numbers)):
    if numbers[pos - 1] > 0 and numbers[pos] > 0 or \
            numbers[pos - 1] < 0 and numbers[pos] < 0:
        print(numbers[pos - 1], numbers[pos])
        break
