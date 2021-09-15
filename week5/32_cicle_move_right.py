line = list(map(int, input().split()))

for pos in range(1):
    line.insert(0, line.pop())

print(*line)
