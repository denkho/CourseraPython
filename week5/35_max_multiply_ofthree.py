numbers = list(map(int, input().split()))

if len(numbers) == 3:
    print(*numbers)
else:
    numbers_c = numbers.copy()
    mi_1 = min(numbers)
    numbers.remove(mi_1)
    mi_2 = min(numbers)
    numbers.remove(mi_2)
    mi_3 = min(numbers)
