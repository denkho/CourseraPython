numbers = list(map(int, input().split()))

max_number = numbers[0]
position = 0
for pos in range(len(numbers)):
    if numbers[pos] > max_number:
        max_number = numbers[pos]
        position = pos

print(max_number, position)
