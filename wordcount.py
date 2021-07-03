import random


sent = input("enter your string")
wcount = 1
lcount = 0

ran = random.randint(1,10)

for i in sent :
    lcount = lcount+1
    if i ==" ":
        wcount=wcount+1

print("alphabetcount","=",lcount)
print("wordcount","=",wcount)
print(ran)