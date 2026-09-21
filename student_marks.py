marks={}
for i in range(3):
    name=input("Enter student name:")
    mark=int(input("Enter marks:"))
    marks[name]=mark
print(marks)
total=0
avg=0
count=0
max=marks[name]
min=marks[name]
for key,value in marks.items():
    total+=value
    count+=1
    if value>max:
        max=value
    if value<min:
        min=value

avg=total//count
print("Total:", total)
print("Average:", avg)
print("Maximum marks:", max)
print("Minimum marks:", min)
