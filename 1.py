import math

i=1
x=1
while i>0:
    if int(x)==0:
        text = input("\nAre you continuing?(y / n or other keys) :")
        if text== 'y':
            x=1
        else :
            x=0
            break

    if int(x)==1:
        print("\n -- calculator -- ")
        print("""
        1.sum
        2.sub
        3.multiplication
        4.division
        5.radikal
        6.sinus
        7.cosine
        8.tangent
        9.cotangent
        10.log
        11.exit
        """)

    num = input("enter number :")
    x=0
    if int(num)==1:
        a=input("number one : ")
        b=input("number two : ")
        c=int (a) + int (b)
        print("sum = ", c)
        

    if int(num)==2:
        a=input("number one : ")
        b=input("number two : ")
        c=int (a) - int (b)
        print("sub = ", c)
        

    if int(num)==3:
        a=input("number one : ")
        b=input("number two : ")
        c=int (a) * int (b)
        print("multiplication = ", c) 
        

    if int(num)==4:
        a=input("number one : ")
        b=input("number two : ")
        c=int (a) / int (b)
        print("division = ", c) 
        

    if int(num)==5:
        a=input("number : ")
        c=int (a)**(1/2)
        print("radical = ", c) 
        


    if int(num)==6:
        a=int(input("degree : "))
        math.radians=a/360 *2 *math.pi
        c=math.sin (math.radians)
        print("sinus = ", float(c))
        

    if int(num)==7:
        a=int(input("degree : "))
        math.radians=a/360 *2 *math.pi
        c=math.cos (math.radians)
        print("cosine = ", float(c))   
        

    if int(num)==8:
        a=int(input("degree : "))
        math.radians=a/360 *2 *math.pi
        c=math.tan (math.radians)
        print("tangent = ", float(c))
        

    if int(num)==9:
        a=int(input("degree : "))
        math.radians=a/360 *2 *math.pi
        c=math.atan (math.radians)
        print("cotangent = ", float(c))
        


    if int(num)==10:
        a=int(input("number : "))
        c=math.log(a)
        print("log = ", c)  
        

    if int(num)==11:
        break