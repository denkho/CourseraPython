numbers = list(map(int, input().split()))

pos = 1
number_of_bigger = 0

while pos < len(numbers) - 1:
    if numbers[pos - 1] < numbers[pos] > numbers[pos + 1]:
        number_of_bigger += 1
    pos += 1

print(number_of_bigger)
