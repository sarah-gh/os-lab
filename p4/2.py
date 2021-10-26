x = int(input("enter row: "))
y = int(input("enter column: "))
for i in range(1,x+1):
    for j in range(1,y+1):
        if (i%2 != 0 ):
            if(j%2 == 0):
                print("*", end=' ')
            else:
                print("#", end=' ')    
        if(i%2 == 0):
            if(j%2 != 0):
                print("*", end=' ')
            else:    
                print("#", end=' ')    
    print("")
