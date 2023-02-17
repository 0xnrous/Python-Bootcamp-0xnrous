#Calculator that take two inputs and return sum and Multiblication etc   

class Calcu:
    def __init__(self , Num1 , Num2):
        self.Num1= Num1
        self.Num2= Num2
    def Sum(self):
        print (f'the Sumation of two numbers is: {self.Num1 + self.Num2 }')
    def Subs(self):
        print (f'the Substruction of two numbers is: {self.Num1 - self.Num2 }')
    def Mull(self):
        print (f'the Multiblication of two numbers is: {self.Num1 * self.Num2 }')
    def Div(self):
        print (f'the Division of two numbers is: {int(self.Num1 / self.Num2) }')
        
c= Calcu(60,30)
c.Sum()
c.Subs()
c.Mull()
c.Div()