from fractions import  Fraction
import math

class Fraction:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y
        
    def sum(self, second):
        result = Fraction()
        result.x = self.x*second.y + self.y*second.x
        result.y = self.y*second.y
        return result


    def sub(self, second):
        result = Fraction()
        result.x = self.x*second.y - self.y*second.x
        result.y = self.y*second.y
        return result

    def multiple(self, second):
        result = Fraction()
        result.x = self.x*second.x
        result.y = self.y*second.y
        return result

    def divide(self, second):
        result = Fraction()
        result.x = self.x*second.y
        result.y = self.y*second.x
        return result

    def show(self):
        numerator = int(self.x)
        denominator = int(self.y)
        common = math.gcd(numerator, denominator)
        numerator //= common
        denominator //= common
        return f"{numerator}/{denominator}"


while(True):
    fraction1 = list(map(int, input('\nenter fraction1: (x/y) \n').split('/')))
    fraction2 = list(map(int, input('enter fraction2: (x/y) \n').split('/')))
    a = Fraction(fraction1[0], fraction1[1])
    b = Fraction(fraction2[0], fraction2[1])
    print('1.sum\n2.sub\n3.multiple\n4.divide')
    func = input()
    if func=='1':
        print('\nsum: '+((a.sum(b)).show()))
    elif func=='2':
        print('\nsub: '+((a.sub(b)).show()))
    elif func=='3':
        print('\multiple: '+((a.multiple(b)).show()))
    elif func=='4':
        print('\divide: '+((a.divide(b)).show()))
    else: 
        print('incorrect input!!!')

    print('\nexit? (y/n)')
    exit = input()
    if exit == 'y':
        break