a = [["name1", "name2", "name3"], ["surname1", "surname2", "surname3"]]
b = int(input("quyidagilardan birini tanlang: 1, 2, 3  "))

if b == 1:
    print(a[0][0], a[1][0])
elif b == 2:
    print(a[0][1], a[1][1])
elif b == 3:
    print(a[0][2], a[1][2])