time=input('time:')
str = time.split(':')

hour=int(str[0])
min=int(str[1])
sec=int(str[2])

if 0<=hour<100 and 0<=min<60 and 0<=sec<60:
   s=hour*3600+min*60+sec
   print(s)
else:          
  print('false')  