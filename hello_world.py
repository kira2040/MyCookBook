from datetime import datetime
print("Hallo World")

name = input("what is your name: ")

number=int(input("When did you born : "))

age = datetime.today().year.__int__()


print(name + "you are " + str(age-number)+" year old")
