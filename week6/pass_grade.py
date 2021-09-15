
def average_grade(students: list) -> list:
    list_of_grades = []

    for student in students:
        if int(student[-1]) < 40 or int(student[-2]) < 40 or int(student[-3]) < 40:
            continue
        else:
            list_of_grades.append(int(student[-1]) + int(student[-2]) + int(student[-3]))
    return sorted(list_of_grades, reverse=True)


f_in = open('input_pass_grade.txt', 'r', encoding='utf-8')
f_out = open('output.txt', 'w', encoding='utf-8')

places_number = int(f_in.readline())
bulk_students = f_in.readlines()
list_of_students = []
for student in bulk_students:
    list_of_students.append(student.split())

av = average_grade(list_of_students)

if places_number >= len(av):
    f_out.write(str(0))
if places_number < len(av):
    if sum(av) / len(av) == av[0]:
        f_out.write(str(1))
    else:
        if av[places_number - 1] == av[places_number]:
            f_out.write(str(av[places_number - 2]))
        else:
            f_out.write(str(av[places_number - 1]))

f_in.close()
f_out.close()
