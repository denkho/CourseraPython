line = list(map(int, input().split()))

for i in range(1, len(line), 2):
    line[i - 1], line[i] = line[i], line[i - 1]

print(' '.join(map(str, line)))
