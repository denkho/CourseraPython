number_of_students = int(input())
student_list = list()
for _ in range(number_of_students):
    student = input().split()
    student_list.append([int(student[1]), student[0]])

student_list.sort(reverse=True)

for student in student_list:
    print(student[1])
