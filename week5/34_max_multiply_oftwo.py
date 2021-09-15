numbers = list(map(int, input().split()))

num_11 = min(numbers)
num_12 = max(numbers)
numbers.remove(num_11)
numbers.remove(num_12)
num_21 = min(numbers)
num_22 = max(numbers)

if num_11 * num_21 > num_12 * num_22:
    result = [num_11, num_21]
else:
    result = [num_12, num_22]

print(*sorted(result))
