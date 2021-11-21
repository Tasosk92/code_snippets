from collections import namedtuple

num_of_students = int(input())
Students = namedtuple('Students',input())
attributes = list(Students._fields)
sum_marks = []

for _ in range(num_of_students):
    inputs = input().split()
    s = dict(zip(attributes,inputs))
    student = Students(**s)
    sum_marks.append(int(student.MARKS))

print(sum(sum_marks)/num_of_students)


'''
input:
5
MARKS      CLASS      NAME       ID        
92         2          Calum      1         
82         5          Scott      2         
94         2          Jason      3         
55         8          Glenn      4         
82         2          Fergus     5

output:
81.00
'''