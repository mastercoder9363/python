a = int(input("Birinchi sonni kiriting: "))
b = int(input("Ikkinchi sonni kiriting: "))
amal = input("amallardan birini kiriting: ")

def kalkulyator(a, b):
    if amal == "+":
        print(a+b)
    elif amal == "-":
        print(a-b)
    elif amal == "*":
        print(a*b)
    elif amal == "/":
        print(a/b)
kalkulyator(a, b)