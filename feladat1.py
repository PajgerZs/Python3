#8. feladat – OOP: BankAccount osztály
#Készíts egy BankAccount osztályt:
#attribútumok: név, egyenleg
#metódusok: deposit(), withdraw(), get_balance()
#Hozz létre két bankszámla objektumot, és teszteld.

class BankAccount:
    def __init__(self, nev, egyenleg=0):
        self.name = nev
        self.balance = egyenleg

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
        else:
            print("Nincs elég fedezet.")

    def get_balance(self):
        return self.balance

account1 = BankAccount("Zoli")
account2 = BankAccount("Kata")

account1.deposit(7200)
account1.withdraw(200)
print(account1.get_balance())

account2.deposit(56000)
account1.withdraw(60000)
print(account2.get_balance())