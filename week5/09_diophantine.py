a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())


def diophantine(a, b, c, d, e):
    result = 0
    for i in range(1001):
        z = i - e
        if z == 0:
            continue
        else:
            if ((a * i**3 + b * i**2 + c * i + d) / z) == 0:
                result += 1
    return result


print(diophantine(a, b, c, d, e))
