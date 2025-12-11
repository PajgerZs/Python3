#10. feladat – OOP: Öröklődés
#Készíts egy Allat alaposztályt (név, életkor).
#Készíts két leszármazottat:
#Kutya (plusz: fajta)
#Macska (plusz: szín)
#Mindkettőnek legyen hang() metódusa, ami kiírja a saját hangját.
#Példányosítsd őket és hívd meg a metódust.

class Allat:
    def __init__(self, nev, kor):
        self.name = nev
        self.age = kor

class Kutya(Allat):
    def __init__(self, nev, kor, fajta):
        super().__init__(nev, kor)
        self.type = fajta

    def hang(self):
        print(f"{self.name} mondja vau-vau")

class Macska(Allat):
    def __init__(self, nev, kor, szin):
        super().__init__(nev, kor)
        self.color = szin

    def hang(self):
        print(f"{self.name} mondja miau-miau")

kutya = Kutya("Bodri", 10, "Labrador")
macska = Macska("Cirmos", 6, "Fekete")

kutya.hang()
macska.hang()