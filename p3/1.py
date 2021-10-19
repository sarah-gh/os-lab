
import requests  
# pip install requests

api='https://random-word-api.herokuapp.com/word?number=1'
response = requests.get(api)

word=response.json()
word=word[0]
print(word)

word_length=len(word)
x = ''
i = word_length

game_mode=0
while game_mode <= 0 or game_mode > 3:
    game_mode = int(input('\nSelect :\n1.Easy\n2.Normal\n3.Hard\n'))
if game_mode == 1:
    i+= 5
elif game_mode == 2:
    i+= 3

while i > 0:      
    check = 0             
    for char in word:  
        if char in x:    
            print (char,end="  ")
            check += 1
            
        else:
            print ("__",end="  ")
        
    
            
    if check == word_length:        
        print ("\n\n*** congratulation You won ***\n")
        break  

    print("\n\nYou have (", i , ") times for guess")

    guess = input("guess a character : ")
    print("\n") 
    guess=guess.lower() 
    x+=guess                    
    if guess not in  word:  
        i-=1        
        print("Wrong : ", guess)
        print("\n")      
        if i == 0:           
            print ("\n &&& You lose &&& ")
