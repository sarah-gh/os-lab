import random


def rock_paper_scissors(c,p):
    
    player=input('enter rock or paper or scissors = ')
    choices=["rock","paper","scissors"]
    computer=random.choice(choices)
    print('computer =',computer)

    if player==computer:
        return print('same')
    if check_win(player,computer):
        p[0]+=1
        return print('user win')
               
    if check_win(player,computer) !=True:
        c[0]+=1
        return print('computer win')

def check_win(user,computer):
    if(user=='rock' and computer=='scissors') or (user=='scissors' and computer=='paper') or (user=='paper' and computer=='rock'):
        return True

i=0
num_c=[0]
num_p=[0]

while(i<5):
    rock_paper_scissors(num_c,num_p)
    i+=1

if (num_p[0] > num_c[0]):
    print("\nplayer : ", num_p[0] ,  "\ncomputer  : " , num_c[0] )
    print("\n** winner = player **\n")

if (num_p[0] < num_c[0]):
    print("\nplayer : ", num_p[0] ,  "\ncomputer  : " , num_c[0] )
    print("\n** winner = computer **\n")  

if (num_p[0] == num_c[0]):
    print("\nplayer : ", num_p[0] ,  "\ncomputer  : " , num_c[0] )
    print("\n** winner = player & computer **\n")  