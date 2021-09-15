numbers = list(map(int, input().split()))

pos_min = numbers.index(min(numbers))
pos_max = numbers.index(max(numbers))

numbers[pos_min], numbers[pos_max] = numbers[pos_max], numbers[pos_min]

print(*numbers)
