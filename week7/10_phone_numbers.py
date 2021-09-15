def clean_number(line: str) -> str:
    line = [x for x in line if x.isdigit()]
    if len(line) == 11:
        return line[4:]
    else:
        return line


file_in = open('input_phones.txt', 'r')
number_add = clean_number(file_in.readline().strip())
numbers_in_phone = file_in.readlines()

for number in numbers_in_phone:
    if clean_number(number) == number_add:
        print('YES')
    else:
        print('NO')

file_in.close()
