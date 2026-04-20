class Vazifa:
    def __init__(self, nom, prioritet, muddat):
        self.nom = nom
        self.prioritet = prioritet
        self.muddat = muddat

class ToDoList:
    def __init__(self):
        self.vazifalar = []

    def qo'sh(self, vazifa):
        self.vazifalar.append(vazifa)

    def ko'rsat(self):
        bugungi_muddat = datetime.date.today()
        o'tgan_vazifalar = [vazifa for vazifa in self.vazifalar if (bugungi_muddat - vazifa.muddat).days > 0]
        mavjud_vazifalar = [vazifa for vazifa in self.vazifalar if (bugungi_muddat - vazifa.muddat).days == 0]
        o'tgan_vazifalar.sort(key=lambda x: (x.muddat, x.prioritet))
        mavjud_vazifalar.sort(key=lambda x: (x.muddat, x.prioritet))
        print("O'tgan vazifalar:")
        for vazifa in o'tgan_vazifalar:
            print(f"{vazifa.nom} - {vazifa.prioritet} - {vazifa.muddat}")
        print("\nMavjud vazifalar:")
        for vazifa in mavjud_vazifalar:
            print(f"{vazifa.nom} - {vazifa.prioritet} - {vazifa.muddat}")

import datetime

todo_list = ToDoList()
while True:
    print("\n1. Vazifa qo'shish")
    print("2. Vazifalar ko'rsatish")
    print("3. Chiqish")
    tanlov = input("Tanlovni kiriting: ")
    if tanlov == "1":
        nom = input("Vazifa nomini kiriting: ")
        prioritet = input("Vazifa prioritetini kiriting (high/medium/low): ")
        muddat = datetime.date.fromisoformat(input("Vazifa muddatini kiriting (yil-mojava-yil): "))
        vazifa = Vazifa(nom, prioritet, muddat)
        todo_list.qo'sh(vazifa)
    elif tanlov == "2":
        todo_list.ko'rsat()
    elif tanlov == "3":
        break
    else:
        print("To'g'ri tanlovni kiriting!")
```

Bu kodda biz vazifalar ro'yxatini saqlash uchun `ToDoList` klassi va vazifa ma'lumotlarini saqlash uchun `Vazifa` klassi yaratdik. `ToDoList` klassida vazifalar qo'shish va ko'rsatish uchun metodlar mavjud. Vazifalar ko'rsatish metodida biz bugungi muddat o'tganlarni alohida ko'rsatish uchun `datetime` modulidan foydalanamiz.
