n = int(input())
numbers = list(map(int, input().split()))
k = int(input())

new_numbers = []
for number in numbers:
    new_numbers.append(abs(k - number))

print(numbers[new_numbers.index(min(new_numbers))])
