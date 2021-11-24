class Time:

    def __init__(self, hour=None, minute=None, second=None):
        self.hour = hour
        self.minute = minute
        self.second = second

    def sub(self, time):
        result = Time()
        result.second = self.second - time.second
        result.minute = self.minute - time.minute
        result.hour = self.hour - time.hour
        if result.second<0:
            result.minute-=1
            result.second+=60
        if result.minute<0:
            result.hour-=1
            result.minute+=60
        return result


    def sum(self, time):
        result = Time()
        result.second = self.second + time.second
        result.minute = self.minute + time.minute
        result.hour = self.hour + time.hour
        if result.second>=60:
            result.second-=60
            result.minute+=1
        if result.minute>=60:
            result.minute-=60
            result.hour+=1
        return result


    def convert_totime(self):
        result = Time()
        result.hour = self.second//3600
        result.minute = (self.second%3600)//60
        result.second = (self.second%3600)%60
        return result


    def convert_tosec(self):
        return self.hour*3600 + self.minute*60 + self.second


    def show(self):
        return ('0'+str(self.hour))[-2:]+':'+('0'+str(self.minute))[-2:]+':'+('0'+str(self.second))[-2:]


def getTime():
    print("first time::")
    h1=int(input("hour: "))
    m1=int(input("minute: "))
    s1=int(input("second: "))
    print("second time::")
    h2=int(input("hour: "))
    m2=int(input("minute: "))
    s2=int(input("second: "))
    return [h1, m1, s1, h2, m2, s2]
    
while(True):    
    print("\nchoose from menu:")
    print("1: sum ")
    print("2: sub")
    print("3: convert time to second")
    print("4: convert second to time")
    print("5: exit")
    n=int(input())

    if n==1:
        time1 = getTime()
        t1= Time(time1[0],time1[1],time1[2])
        t2= Time(time1[3],time1[4],time1[5])
        print('sum:', t1.sum(t2).show())
    if n==2:
        time1 = getTime()
        t1= Time(time1[0],time1[1],time1[2])
        t2= Time(time1[3],time1[4],time1[5])
        print('sub:', t1.sub(t2).show())

    if n==3:
        h=int(input("hour: "))
        m=int(input("minute: "))
        s=int(input("second: "))
        t=Time(h,m,s)
        print('convert to sec: ', t.convert_tosec())
        
       

    if n==4:
       
        x=int(input("enter the seconds: "))
        t=Time(0,0,x)
        print('convert to time:', t.convert_totime().show())

    if n==5:
        exit()     