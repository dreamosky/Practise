def linearSearch(values, target):
    for i in range(len(values)):
        if values[i]==target:
            return i
        return -1

from random import randint
n=10
values=[]
for i in range(n):
    values.append(randint(1,100))
print(values)

done=False
while not done:
    target=int(input("Enter number to search for, -1 to quit:"))
    if target ==-1:
        done=True
    else:
        pos=linearSearch(values,target)
        if pos ==-1:
            print("Not found")
        else:
            print("Fond in position", pos)
