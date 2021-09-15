numbers = list(map(int, input().split()))

min_number = 1001

for number in numbers:
    if min_number > number > 0:
        min_number = number

print(min_number)
