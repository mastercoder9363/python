try:
    a = int(input("Birinchi sonni kiriting: "))
    b = int(input("Ikkinchi sonni kiriting: "))
    amal = input("amallardan birini kiriting: ")

    if amal == "+":
        print(a+b)
    elif amal == "-":
        print(a-b)
    elif amal == "*":
        print(a*b)
    elif amal == "/":
        print(a/b)
except ZeroDivisionError:
    print("sonni 0 ga bo'lib bo'lmaydi")
except:
    print("integerga stringni qo'shib bo'lmaydi")