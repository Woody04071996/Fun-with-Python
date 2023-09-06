#Nieistotne fakty
#
#Uzyskuje dane osobiste od uzytkownika, a potem
#wpisuje prawdziwe, lecz bezuzyteczne informacje o nim


name = input("Czesc jak masz na imie?")

age = input("Ile masz lat")
age = int(age)

weight = int(input("Dobrze ostanie pytanie. Ile kilogramow wazysz?"))

print("\nJesli poeta ee cummings wyslalby do Ciebie wiadomosc e-mail,\nzwrocilby sie do Ciebie",
      name.lower())
print("Ale jesli bylby wsciekly, nazwalby Cie", name.upper())

called = name * 5
print("\nJesli male dziecko probowaloby zwrocic na siebie Twoja uwage,",)
print("Twoje imie przybralo forme:")
print(called)

seconds = age * 365 * 24 * 60 * 60
print("\nZyjesz juz ponad" , seconds, "sekund")

moon_weight = weight / 6
print("\nCzy wiesz , ze na Ksiezycu Twoja waga wynosilaby", moon_weight, "kg")

sun_weight = weight / 27.1
print("\nNa Sloncu wazylbys ", sun_weight, "kg (ale niestety nie dlugo)." )

input("\n\nAby zakonczyc program, nacisnij Enter.")

