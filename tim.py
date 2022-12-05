import time
a = int(input("kodni kiriting: "))
b = 0

if a == 1234:
    print("kod to'g'ri")
elif a != 1234:
    print("kod xato 4 sekund kuting")
    while b<4:
        b += 1
        time.sleep(0.2)
        print(b)