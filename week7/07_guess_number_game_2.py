text = open('input_gues_num_2.txt', 'r')

august = set(range(1, int(text.readline()) + 1))
beatrice = text.readline()

while beatrice != "HELP":
    beatrice_set = set(map(int, beatrice.split()))
    if len(august & beatrice_set) <= len(august) // 2:
        print('NO')
        august -= beatrice_set
    else:
        print('YES')
        august &= beatrice_set
    beatrice = text.readline()

print(*sorted(august))
text.close()
