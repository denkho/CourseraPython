'''
Проверьте, есть ли среди данных N чисел нули.
Формат ввода
Вводится число N, а затем N чисел.
Формат вывода
Выведите True, если среди введенных чисел есть хотя бы один нуль, или False в противном случае.
'''


def zero_not(s: [int]) -> bool:
    if 0 in s:
        return True
    else:
        return False


t = list()
n = int(input())
for _ in range(n):
    t.append(int(input()))

print(zero_not(t))
