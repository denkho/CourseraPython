n = int(input())

sum1 = 0
sum2 = 0

for i in range(1, n + 1):
    sum1 += i

for j in range(n - 1):
    sum2 += int(input())

print(sum1 - sum2)
