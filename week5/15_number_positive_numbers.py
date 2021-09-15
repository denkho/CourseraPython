# Найдите количество положительных элементов в данном списке.
# Вводится список чисел. Все числа списка находятся на одной строке.

numbers = list(map(int, input().split()))


def number_of_positive_numbers(nums):
    result = 0
    for number in nums:
        if number > 0:
            result += 1
    return result


print(number_of_positive_numbers(numbers))
