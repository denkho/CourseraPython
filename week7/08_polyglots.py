in_file = open('input_phones.txt', 'r')

numbers_of_students = int(in_file.readline())
students = []

for _ in range(numbers_of_students):
    numbers_of_languages = int(in_file.readline())
    languages = []
    for _ in range(numbers_of_languages):
        languages.append(in_file.readline().strip())
    students.append(set(languages))

lang_all = students[0].copy()
lang_one = students[0].copy()

for lang in students[1:]:
    lang_all &= lang
    lang_one |= lang

print(len(lang_all), *lang_all, len(lang_one), *lang_one, sep='\n')
