n = int(input())

print('+___ ' * n)
for i in range(1, n + 1):
    print('|', i, ' / ', sep='', end='')
print('\n', '|__\\ ' * n, sep='')
print('|    ' * n)
