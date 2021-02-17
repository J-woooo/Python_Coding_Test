n = int(input())

students = []
for i in range(n):
    student, grade = input().split(" ")
    students.append((student, int(grade)))

students = sorted(students, key=lambda student: student[1])

for student in students:
    print(student[0], end=' ')
