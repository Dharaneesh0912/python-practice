word=input("Enter a word:")
dict={}
for i in word:
    if i in ["a","e","i","o","u"]:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
print(dict)
