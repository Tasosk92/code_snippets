num_students,num_subjects = list(map(int,input().split()))
marks= []
for _ in range(num_subjects):
    marks.append(list(map(float,input().split(' '))))

avg = [sum(tup)/num_subjects for tup in list(zip(*marks))]

for value in avg:
    print(value)
