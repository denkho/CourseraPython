def IsAscending(s):
    pos = 1
    while pos < len(s):
        if s[pos] > s[pos - 1]:
            pos += 1
            continue
        else:
            return "NO"
    return "YES"


numbers = list(map(int, input().split()))
print(IsAscending(numbers))
