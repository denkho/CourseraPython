text = open('input_gues_num.txt', 'r')
temp = set()
result = set(map(int, range(1, int(text.readline()) + 1)))
lines = text.readlines()

for line in lines:
    if line.strip() == 'HELP':
        break
    elif line.strip() == 'YES':
        result &= temp
    elif line.strip() == 'NO':
        result -= temp
    else:
        temp = set(map(int, line.split()))

print(*sorted(result))
text.close()
