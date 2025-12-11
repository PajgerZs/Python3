#9. feladat – OOP + lista: Tanulók kezelése
#Student osztály: név, életkor, átlag.
#Kérj be 3 tanulót, tedd őket listába, majd írd ki annak a nevét, akinek a legjobb az átlaga.

class Student():
    Students= []

    def __init__(self, nev, eletkor, atlag):
        self.name = nev
        self.age = eletkor
        self.avg = atlag
        Student.Students.append(self)

        max = self.Students[0].avg
        id = 0
        
        for i in range(len(self.Students)):
            if self.Students[i].avg > max:
                max = i
                id = i
        print(self.Students[id].name)

for i in range(3):
    nev = input(f"Kérem a(z) {i}. nevet: ")
    eletkor = int(input(f" Kérem a(z) {i}. életkort: "))
    atlag = float(input(f"Kérem a(z) {i}. átlagot: "))
    Student(nev,eletkor,atlag)