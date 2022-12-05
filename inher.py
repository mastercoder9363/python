class Odam:
    def __init__(self, ism, familiya, yil):
        self.ism = ism
        self.familiya = familiya
        self.yil = yil
    def __str__(self):
        return f"{self.ism} {self.familiya} {self.yosh}"


class Student(Odam):
    def __init__(self, ism, familiya, yil, yosh):
        super(). __init__(ism, familiya, yil)
        self.yosh = yosh
    def student(self):
        print(self.ism, self.familiya, self.yil, self.yosh)


s1 = Student("Dilshod", "Akbarov", 2000, 22)
s2 = Student("Dilshoda", "Akbarova", 2001, 21)

print(s1.student())
print(s2.student())