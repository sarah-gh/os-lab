num=int(input('enter secend:'))
if num>0:
    hour=num//3600
    num=num%3600
    min=num//60
    sec=num%60
    h=str(hour)
    if len(h)==1:
        h='0'+h
    m=str(min)
    if len(m)==1:
        m='0'+m
    s=str(sec)
    if len(s)==1:
        s='0'+s
    print(h+':'+m+':'+s)
else :
    print('error')