try:
    ism = input("ismingizni kiriting: ")
    familiya = input("familiyangizni kiriting: ")
    parol = int(input("parol kiriting: "))

    if parol == 1234:
        print("siz dasturga kirdingiz")
    if parol != 1234:
        print("parol xato")
except ValueError:
    print("siz string qiymat kiritdingiz")