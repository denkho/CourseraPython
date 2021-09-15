def zeros(n: int) -> int:
    zero = 0
    for i in range(n):
        if int(input()) == 0:
            zero += 1
    return zero


N = int(input())
print(zeros(N))
