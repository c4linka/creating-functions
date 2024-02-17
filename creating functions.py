"""def hello_msg():
    print("Hello there")
    print("How are you?")


hello_msg()
#--------------------------------------------
name = input("Hey, what is your name? ")


def hello_msg():
    print("Hello there",name,":)")
    print("How are you?")



hello_msg()
#---------------------------------------------
def bye_msg(name):
    print("Bye bye",name+"!")
    print("Was nice to meeting you")

bye_msg("Alu")
bye_msg("Ewo")

#---------------------------------------------"""
names = ["Alu", "Ewo", "Elu", "Olu"]

def hi_msg(name):
    print("Hi", name)
    print("Have a nice day")
    print()
    
for name in names:
    hi_msg(name)
