numbers = list(map(int, input().split()))
numbers_to_check = set()

for number in numbers:
    if number not in numbers_to_check:
        print('NO')
        numbers_to_check.add(number)
    else:
        print('YES')
