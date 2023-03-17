class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, najete_km):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = True
    def pujc_auto(self):
        if self.dostupne is True:
            print("Potvrzuji zapůjčení vozidla")
            self.dostupne = False
        else: 
            print("Vozidlo není k dispozici")
    def get_info(self):
        print(f"registracni_znacka = {self.registracni_znacka}, typ_vozidla = {self.typ_vozidla}")

car1 = Auto(registracni_znacka = "4A2 3020", typ_vozidla = "Peugeot 403 Cabrio", najete_km = 47534)
car2 = Auto(registracni_znacka = "1P3 4747", typ_vozidla = "Škoda Octavia", najete_km = 41253)

help_needed = True
while help_needed is True:
    repeat = True
    while repeat is True:    
        answer = input("Jakou si prejete znacku auta? Škoda nebo Peugeot? ")
        if answer == "Škoda":
            chosen_car = car2
            repeat = False
        elif answer == "Peugeot":
            chosen_car = car1
            repeat = False
        else:
            print("Pozadovanou znacku nemame, vyberte prosim Škoda nebo Peugeot")

    chosen_car.get_info()
    repeat = True
    while repeat is True:
        answer = input("Prejete si auto zapujcit? Ano nebo ne? ")
        if answer == "Ano":
            chosen_car.pujc_auto()
            repeat = False
        elif answer == "Ne":
            print("Dekujeme, hezky den.")
            repeat = False
        else: 
            print("Nerozumel jsem Vasi odpovedi, zadejte prosim Ano nebo Ne.")
    answer = input("Mohu Vam pomoci s necim dalsim? Ano nebo ne? ")
    if answer == "Ne":
        help_needed = False 
3