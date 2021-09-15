k = int(input())  # котлет за раз на сковороде
m = int(input())  # минут жарится
n = int(input())  # кол-во котлет для жарки

if n % k == 0:
    t = m * 2 * (n // k)
elif n < k or n % k > k // 2:
    t = (m * 2 * (n // k)) + m * 2
else:
    t = (m * 2 * (n // k)) + m

print(t)
