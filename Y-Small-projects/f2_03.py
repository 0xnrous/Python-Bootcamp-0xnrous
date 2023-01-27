from sympy import symbols, Eq

name = input ("Please Enter Your Name: ")
age = int (input ("How Old Are you? "))
tall= float(input ("How tall are you? "))
weight= float(input("How Weight are you? "))
eq1= int (tall / weight * age +10)
eq2= int ((eq1-age)+2023)
print ("===============")
print (f"Welcome, {name.title()}")
print (f'You will live until {eq2}, and you will be {eq1} years old ')

