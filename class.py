class Odam:
    def __init__(self, ism, familiya, yosh):
        self.ism = ism
        self.familiya=familiya
        self.yosh = yosh
    def __str__(self):
        return f"{self.ism} {self.familiya} {self.yosh}"

o1 = Odam("Dilshoda", "Akbarova", 18)
o2 = Odam("Dilshod", "Akbarov", 18)

print(o1)
print(o2)