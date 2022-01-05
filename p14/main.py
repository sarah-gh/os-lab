from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *

import sys
from math import *

ScW = 400
ScH = 600

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Calculator')
        self.setGeometry(100, 100, ScW, ScH)
        self.setStyleSheet("background-color : #292929;") 
        self.UiComponents() 

        self.show()

    def UiComponents(self):
        self.label = QLabel(self)
        self.label.setGeometry(0, 0, ScW, ScH/5) 
        self.label.setWordWrap(True)
        self.label.setStyleSheet("background-color : #292929; color: white; margin: 5px; font-size:40px") 
        self.label.setAlignment(Qt.AlignVCenter | Qt.AlignRight) 
        self.label.setFont(QFont('Arial', 15))

        clear = QPushButton("AC", self) 
        clear.setGeometry(0, ScH/5, ScW/4, ScH/10)
        clear.setStyleSheet("background-color: #191a19; color: white; outline: none; border: none; margin: 1px; font-size: 30px")

        sign = QPushButton("+/-", self) 
        sign.setGeometry(ScW/4, ScH*2/10, ScW/4, ScH/10)
        sign.setStyleSheet("background-color: #191a19; color: white; outline: none; border: none; margin: 1px; font-size: 30px")

        per = QPushButton("%", self) 
        per.setGeometry(ScW*2/4, ScH*2/10, ScW/4, ScH/10)
        per.setStyleSheet("background-color: #191a19; color: white; outline: none; border: none; margin: 1px; font-size: 30px")

        div = QPushButton("/", self) 
        div.setGeometry(ScW*3/4, ScH*2/10, ScW/4, ScH/10)
        div.setStyleSheet("background-color: #00cf00; color: white; outline: none; border: none; margin: 1px; font-size: 30px")

        n7 = QPushButton("7", self) 
        n7.setGeometry(0, ScH*3/10, ScW/4, ScH/10)
        n7.setStyleSheet("background-color: #6b6b6b; color: white; outline: none; border: none; margin: 1px; font-size: 30px")

        n8 = QPushButton("8", self) 
        n8.setGeometry(ScW/4, ScH*3/10, ScW/4, ScH/10)
        n8.setStyleSheet("background-color: #6b6b6b; color: white; outline: none; border: none; margin: 1px; font-size: 30px")

        n9 = QPushButton("9", self) 
        n9.setGeometry(ScW*2/4, ScH*3/10, ScW/4, ScH/10)
        n9.setStyleSheet("background-color: #6b6b6b; color: white; outline: none; border: none; margin: 1px; font-size: 30px")

        mul = QPushButton("*", self) 
        mul.setGeometry(ScW*3/4, ScH*3/10, ScW/4, ScH/10)
        mul.setStyleSheet("background-color: #00cf00; color: white; outline: none; border: none; margin: 1px; font-size: 30px")

        n4 = QPushButton("4", self) 
        n4.setGeometry(0, ScH*4/10, ScW/4, ScH/10)
        n4.setStyleSheet("background-color: #6b6b6b; color: white; outline: none; border: none; margin: 1px; font-size: 30px")

        n5 = QPushButton("5", self) 
        n5.setGeometry(ScW/4, ScH*4/10, ScW/4, ScH/10)
        n5.setStyleSheet("background-color: #6b6b6b; color: white; outline: none; border: none; margin: 1px; font-size: 30px")

        n6 = QPushButton("6", self) 
        n6.setGeometry(ScW*2/4, ScH*4/10, ScW/4, ScH/10)
        n6.setStyleSheet("background-color: #6b6b6b; color: white; outline: none; border: none; margin: 1px; font-size: 30px")

        minu = QPushButton("-", self) 
        minu.setGeometry(ScW*3/4, ScH*4/10, ScW/4, ScH/10)
        minu.setStyleSheet("background-color: #00cf00; color: white; outline: none; border: none; margin: 1px; font-size: 30px")

        n1 = QPushButton("1", self) 
        n1.setGeometry(0, ScH*5/10, ScW/4, ScH/10)
        n1.setStyleSheet("background-color: #6b6b6b; color: white; outline: none; border: none; margin: 1px; font-size: 30px")

        n2 = QPushButton("2", self) 
        n2.setGeometry(ScW/4, ScH*5/10, ScW/4, ScH/10)
        n2.setStyleSheet("background-color: #6b6b6b; color: white; outline: none; border: none; margin: 1px; font-size: 30px")

        n3 = QPushButton("3", self) 
        n3.setGeometry(ScW*2/4, ScH*5/10, ScW/4, ScH/10)
        n3.setStyleSheet("background-color: #6b6b6b; color: white; outline: none; border: none; margin: 1px; font-size: 30px")

        plus = QPushButton("+", self) 
        plus.setGeometry(ScW*3/4, ScH*5/10, ScW/4, ScH/10)
        plus.setStyleSheet("background-color: #00cf00; color: white; outline: none; border: none; margin: 1px; font-size: 30px")

        n0 = QPushButton("0", self) 
        n0.setGeometry(0, ScH*6/10, ScW*2/4, ScH/10)
        n0.setStyleSheet("background-color: #6b6b6b; color: white; outline: none; border: none; margin: 1px; font-size: 30px")

        dot = QPushButton(".", self) 
        dot.setGeometry(ScW*2/4, ScH*6/10, ScW/4, ScH/10)
        dot.setStyleSheet("background-color: #6b6b6b; color: white; outline: none; border: none; margin: 1px; font-size: 30px")

        eq = QPushButton("=", self) 
        eq.setGeometry(ScW*3/4, ScH*6/10, ScW/4, ScH/10)
        eq.setStyleSheet("background-color: #00cf00; color: white; outline: none; border: none; margin: 1px; font-size: 30px")

        sin = QPushButton("sin", self) 
        sin.setGeometry(0, ScH*7/10, ScW/4, ScH/10)
        sin.setStyleSheet("background-color: #00cf00; color: white; outline: none; border: none; margin: 1px; font-size: 30px")

        cos = QPushButton("cos", self) 
        cos.setGeometry(ScW/4, ScH*7/10, ScW/4, ScH/10)
        cos.setStyleSheet("background-color: #00cf00; color: white; outline: none; border: none; margin: 1px; font-size: 30px")

        tan = QPushButton("tan", self) 
        tan.setGeometry(ScW*2/4, ScH*7/10, ScW/4, ScH/10)
        tan.setStyleSheet("background-color: #00cf00; color: white; outline: none; border: none; margin: 1px; font-size: 30px")

        cot = QPushButton("cot", self) 
        cot.setGeometry(ScW*3/4, ScH*7/10, ScW/4, ScH/10)
        cot.setStyleSheet("background-color: #00cf00; color: white; outline: none; border: none; margin: 1px; font-size: 30px")

        log = QPushButton("log", self) 
        log.setGeometry(0, ScH*8/10, ScW/4, ScH/10)
        log.setStyleSheet("background-color: #00cf00; color: white; outline: none; border: none; margin: 1px; font-size: 30px")

        sq = QPushButton("sqrt", self) 
        sq.setGeometry(ScW/4, ScH*8/10, ScW/4, ScH/10)
        sq.setStyleSheet("background-color: #00cf00; color: white; outline: none; border: none; margin: 1px; font-size: 30px")

        pl = QPushButton("(", self) 
        pl.setGeometry(ScW*2/4, ScH*8/10, ScW/4, ScH/10)
        pl.setStyleSheet("background-color: #00cf00; color: white; outline: none; border: none; margin: 1px; font-size: 30px")

        pr = QPushButton(")", self) 
        pr.setGeometry(ScW*3/4, ScH*8/10, ScW/4, ScH/10)
        pr.setStyleSheet("background-color: #00cf00; color: white; outline: none; border: none; margin: 1px; font-size: 30px")

        rem = QPushButton("Del", self) 
        rem.setGeometry(0, ScH*9/10, ScW, ScH/10)
        rem.setStyleSheet("background-color: red; color: white; outline: none; border: none; margin: 1px; font-size: 30px")

        clear.clicked.connect(self.clear)
        rem.clicked.connect(self.rem)
        n0.clicked.connect(self.n0)
        n1.clicked.connect(self.n1)
        n2.clicked.connect(self.n2)
        n3.clicked.connect(self.n3)
        n4.clicked.connect(self.n4)
        n5.clicked.connect(self.n5)
        n6.clicked.connect(self.n6)
        n7.clicked.connect(self.n7)
        n8.clicked.connect(self.n8)
        n9.clicked.connect(self.n9)
        plus.clicked.connect(self.plus)
        div.clicked.connect(self.div)
        minu.clicked.connect(self.minu)
        per.clicked.connect(self.per)
        sign.clicked.connect(self.sign)
        mul.clicked.connect(self.mul)
        eq.clicked.connect(self.eq)
        sin.clicked.connect(self.sin)
        cos.clicked.connect(self.cos)
        tan.clicked.connect(self.tan)
        cot.clicked.connect(self.cot)
        log.clicked.connect(self.log)
        sq.clicked.connect(self.sq)
        dot.clicked.connect(self.dot)
        pl.clicked.connect(self.pl)
        pr.clicked.connect(self.pr)

    def clear(self):
        print('clear')
        self.label.setText("") 

    def rem(self):
        print('rem')
        text = self.label.text()  
        self.label.setText(text[:len(text)-1]) 
    
    def n0(self):
        print('n0')
        text = self.label.text() 
        self.label.setText(text + "0") 
    
    def n1(self):
        print('n1')
        text = self.label.text() 
        self.label.setText(text + "1")
    
    def n2(self):
        print('n2')
        text = self.label.text() 
        self.label.setText(text + "2")
    
    def n3(self):
        print('n3')
        text = self.label.text() 
        self.label.setText(text + "3")

    def n4(self):
        print('n4')
        text = self.label.text() 
        self.label.setText(text + "4")
    
    def n5(self):
        print('n5')
        text = self.label.text() 
        self.label.setText(text + "5")
    
    def n6(self):
        print('n6')
        text = self.label.text() 
        self.label.setText(text + "6")
    
    def n7(self):
        print('n7')
        text = self.label.text() 
        self.label.setText(text + "7")

    def n8(self):
        print('n8')
        text = self.label.text() 
        self.label.setText(text + "8")

    def n9(self):
        print('n9')
        text = self.label.text() 
        self.label.setText(text + "9")
    
    def plus(self):
        print('plus')
        text = self.label.text() 
        self.label.setText(text + "+")
    
    def div(self):
        print('div')
        text = self.label.text() 
        self.label.setText(text + "/") 
    
    def minu(self):
        print('minu')
        text = self.label.text() 
        self.label.setText(text + "-") 

    def per(self):
        print('per')
        text = self.label.text() 
        self.label.setText(text + "%") 

    def sign(self):
        print('sign')
        text = self.label.text() 
        if text[0] != '-':
            self.label.setText("-" + text) 
    
    def mul(self):
        print('mul')
        text = self.label.text() 
        self.label.setText(text + "*") 
    
    def eq(self):
        print('eq')
        equation = self.label.text().replace('%', '*0.01') 
        try: 
            ans = eval(equation) 
            self.label.setText(str(round(ans, 4))) 
        except: 
            self.label.setText("Wrong Input")

    def sin(self):
        print('sin')
        text = self.label.text() 
        self.label.setText(text + "sin") 

    def cos(self):
        print('cos')
        text = self.label.text() 
        self.label.setText(text + "cos") 

    def tan(self):
        print('tan')
        text = self.label.text() 
        self.label.setText(text + "tan") 
    
    def cot(self):
        print('cot')
        text = self.label.text() 
        self.label.setText(text + "cot") 
    
    def log(self):
        print('log')
        text = self.label.text() 
        self.label.setText(text + "log") 
    
    def sq(self):
        print('sq')
        text = self.label.text() 
        self.label.setText(text + "sqrt") 
    
    def pl(self):
        print('pl')
        text = self.label.text() 
        self.label.setText(text + "(") 
    
    def pr(self):
        print('pr')
        text = self.label.text() 
        self.label.setText(text + ")") 

    def dot(self):
        print('dot')
        text = self.label.text() 
        self.label.setText(text + ".") 

App = QApplication(sys.argv) 
window = Calculator() 
sys.exit(App.exec()) 