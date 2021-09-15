numbers = list(map(int, input().split()))
k = int(input())

numbers.pop(k)
for number in numbers:
    print(number, end=" ")
