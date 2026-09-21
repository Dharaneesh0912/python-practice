marks=list(map(int,input("Enter the marks of students: ").split(",")))
def avg(sum, count):
    return (sum//count)
sum=0
count=0
for i in marks:
    sum+=i
    count+=1
Average=avg(sum,count)
print("The average marks of students is:",Average)