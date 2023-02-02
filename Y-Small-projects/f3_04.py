print ("================================")
print("Welcome to $$ EXCHANGE STORE $$")
print ("================================")

CUR_exf = input ("Exchage From (USD, EUR, SAR): ").upper() 
amount_ex = float (input ("How much? "))
CUR_ext = input ("Exchage to (USD, EUR, SAR): ").upper()

USD=1 
EUR = .99
SAR = 3.75 

NewAmount = 0 

if CUR_exf == CUR_ext :
    print(f" You will keep your amout as it is,{amount_ex} {CUR_exf} ")
elif CUR_exf == "USD" and CUR_ext == "EUR":
    NewAmount = amount_ex * EUR
    print (f"the amout exchanged is: {NewAmount} EUR ")
elif CUR_exf == "USD" and CUR_ext == "SAR":
    NewAmount = amount_ex * SAR
    print (f"the amout exchanged is: {NewAmount} SAR ")
elif CUR_exf == "EUR" and CUR_ext == "USD":
    NewAmount = amount_ex / EUR
    print (f"the amout exchanged is: {NewAmount} USD ")
elif CUR_exf == "EUR" and CUR_ext == "SAR":
    NewAmount = amount_ex * EUR / SAR 
    print (f"the amout exchanged is: {NewAmount} SAR ")
elif CUR_exf == "SAR" and CUR_ext == "USD":
    NewAmount = amount_ex / SAR
    print (f"the amout exchanged is: {NewAmount} USD ")
elif CUR_exf == "SAR" and CUR_ext == "EUR":
    NewAmount = amount_ex / SAR * EUR
    print (f"the amout exchanged is: {NewAmount} EUR ")
else : 
    print ("you write wrong currency")

