numbers = list(map(int, input().split()))

min_number = 0

for number in numbers:
    if number % 2 != 0:
        if min_number == 0:
            min_number = number
        if min_number > number:
            min_number = number


print(min_number)
