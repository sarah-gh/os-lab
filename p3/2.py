import random

length=int(input("Enter the size of array: "))
array=[]
for i in range(length):
    while(True):
        rand=random.randint(-100,100)
        if rand not in array:
            break
    array.append(rand)
print(array)