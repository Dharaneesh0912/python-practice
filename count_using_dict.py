numbers=list(map(int,input("Enter numbers:").split(" ")))
count={}
for i in numbers:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)
