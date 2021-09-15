numbers = list(map(int, input().split()))
k, c = list(map(int, input().split()))

numbers.append(c)

for pos in range(len(numbers) - 1, k, -1):
    numbers[pos], numbers[pos-1] = numbers[pos-1], numbers[pos]

print(' '.join(map(str, numbers)))
