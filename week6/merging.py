def merge(a: list, b: list) -> list:
    c = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        elif a[i] > b[j]:
            c.append(b[j])
            j += 1
        else:
            c.append(a[i])
            c.append(b[j])
            i += 1
            j += 1
    while i < len(a):
        c.append(a[i])
        i += 1
    while j < len(b):
        c.append(b[j])
        j += 1
    return c


list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))

print(*merge(list_a, list_b))


#  def merge(a: list, b: list) -> list:
#     result = []
#     a.extend(b)
#     while a:
#         result.append(a.pop(a.index(min(a))))

#     return result
