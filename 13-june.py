seats = [4,1,5,9]
students = [1,3,2,6]
n=len(students)
total=0
seats.sort()
students.sort()
for i in range(n):
    total+=abs(students[i]-seats[i])
print(total)

