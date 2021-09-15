n = int(input())


def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)


def sum_of_factorials(num):
    sum = 0
    for i in range(1, num + 1):
        sum += factorial(i)
    return sum


print(sum_of_factorials(n))
