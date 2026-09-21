input1=input("Enter Student Name:")
sub1=int(input("Enter marks for subject 1:"))
sub2=int(input("Enter marks for subject 2:"))
sub3=int(input("Enter marks for subject 3:"))
sub4=int(input("Enter marks for subject 4:"))
sub5=int(input("Enter marks for subject 5:"))
total=sub1+sub2+sub3+sub4+sub5
avg=total/5
if(avg>90):
    grade="A"
elif(avg>50 and avg<90):
    grade="B"
else:
    grade="c"
print("Total:",total)
print("Average:",avg)
print("Grade:",grade)