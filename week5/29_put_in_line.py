students = list(map(int, input().split()))
Pete = int(input())

new_students = []
for student in students:
    if student >= Pete:
        new_students.append(student)

print(len(new_students) + 1)
