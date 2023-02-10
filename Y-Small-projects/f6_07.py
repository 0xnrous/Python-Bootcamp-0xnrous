## this  SMALL project for NATO PHONETICS ALPHAPET 
print("========================")
print ("NATO PHONETIC ALPHABET ")
print("========================")

names= {"A":"Alpha" ,"B":"Bravo", "C" :"Charlie","D":"Delta" ,"E": "Echo", "F":"Foxtrot","G": "Golf","H": "Hotel","I": "India","J":" Juliett","K": "Kilo","L": "Lima","M": "Mike","N":"November","O": "Oscar","P": "Papa","Q": "Quebec","R": "Romeo","S": "Sierra","T": "Tango","U": "Uniform","V": "Victor","W":" Whiskey","X": "X-ray","Y": "Yankee","Z": "Zulu"}

name = input("Please enter your name: ").upper()
print ("The spilling of your name phonetically is:  ")

for n in name :
    if n == " ":
        print("----")
    elif n == "-" or n == "*" or n == "&" or n == "." or n == "|" or n == "/" or n == ",":
        print (f"{n}: {n} ")
    else :
        print (f"{n}:{names[n]}")

    
