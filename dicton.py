a = int(input('quyidagilardan birini tanlang: 1, 2  '))
lugat = {
    "O'zbekiston1":{
        "poytaxt": "Toshkent",
        "eng katta shahar": "Toshkent"
    },
    "O'zbekiston2":{
        "maydon": "44897kmkv",
        "o'rin": "56"
    }
}

if a == 1:
    print(lugat["O'zbekiston1"])
elif a == 2:
    print(lugat["O'zbekiston2"])