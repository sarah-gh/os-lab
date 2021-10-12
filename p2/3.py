import random
i=0

def chek_win1(user,computer1,computer2):
    if(user=='back' and computer1=='palm' and computer2=='palm') or (user=='palm' and computer1=='back' and computer2=='back'):
        return True
def chek_win2(user,computer1,computer2):
    if(computer1=='palm' and computer2=='back' and user=='back') or (computer1=='back' and computer2=='palm' and computer2=='palm'):
        return True
def chek_win3(user,computer1,computer2):
    if(computer2=='back' and computer1=='palm' and user=='palm') or (computer2=='palm' and computer1=='back' and user=='back'):
        return True
def palamPulumPilish(c1,c2,p):
    player=input('Enter palm or back = ')
    choices=["palm","back"]
    computer1=random.choice(choices) 
    print('computer1 = ',computer1)       
    computer2=random.choice(choices)
    print('computer2 = ',computer2)

    if(player==computer1 and player==computer2):
        return print('same')
    if chek_win1(player,computer1,computer2):
        p[0]+=1
        return print('user win')
    if chek_win2(player,computer1,computer2):
        c1[0]+=1
        return print('computer1 win')
    if chek_win3(player,computer1,computer2):
        c2[0]+=1
        return print('computer2 win')

num_c1=[0]
num_c2=[0]
num_p=[0]

while(i<5):
    palamPulumPilish(num_c1,num_c2,num_p)
    i+=1

if (num_p > num_c1 and num_p> num_c2) or (num_c2 == num_c1 and num_p> num_c2):
    print("\n--------------\nplayer: ", num_p ,"\ncomputer 1 : ", num_c1 ,"\ncomputer 2 : ", num_c2,"\n-------------")
    print(" *** winner : player *** ")   

if (num_p < num_c1 and num_c1> num_c2) or (num_p == num_c2 and num_p< num_c1):
    print("\n--------------\nplayer: ", num_p ,"\ncomputer 1 : ", num_c1 ,"\ncomputer 2 : ", num_c2,"\n-------------")
    print(" *** winner : computer 1 *** ")   

if (num_c2 > num_c1 and num_p< num_c2) or (num_p == num_c1 and num_p< num_c2):
    print("\n--------------\nplayer: ", num_p ,"\ncomputer 1 : ", num_c1 ,"\ncomputer 2 : ", num_c2,"\n-------------")
    print(" *** winner : computer 2  *** ")

if (num_p == num_c1 and num_p> num_c2):
    print("\n--------------\nplayer: ", num_p ,"\ncomputer 1 : ", num_c1 ,"\ncomputer 2 : ", num_c2,"\n-------------")
    print(" *** winner : player  and computer 1 *** ")  

if (num_c2 == num_c1 and num_p< num_c2):
    print("\n--------------\nplayer: ", num_p ,"\ncomputer 1 : ", num_c1 ,"\ncomputer 2 : ", num_c2,"\n-------------")
    print(" *** winner : computer 1 and computer 2 *** ")

if (num_p == num_c2 and num_p> num_c1):
    print("\n--------------\nplayer: ", num_p ,"\ncomputer 1 : ", num_c1 ,"\ncomputer 2 : ", num_c2,"\n-------------")
    print(" * winner : player and computer 3 * ")

if (num_p == num_c2 and num_p == num_c1):
    print("\n--------------\nplayer: ", num_p ,"\ncomputer 1 : ", num_c1 ,"\ncomputer 2 : ", num_c2,"\n-------------")
    print(" * winner : all * ")  