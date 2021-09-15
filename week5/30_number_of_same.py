numbers = list(map(int, input().split()))
answer = [numbers[0]]

for pos in range(1, len(numbers)):
    if numbers[pos - 1] != numbers[pos]:
        answer.append(numbers[pos])

print(len(answer))
