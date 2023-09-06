#Translator slangu komputerowego
#Listy i slowniki

print("\tTranslator slangu komputerowego")
print("\nWybierz jedna z opcji")

terminy = ["piatek", "sobota", "niedziela", "poniedzialek"]
choice = None
while choice != "0":
    print(
    """
    Najlepsze wyniki 2.0

    0 - zakoncz
    1 - znajdz termin
    2 - dodaj nowy termin
    3 - zmien definicje terminu
    4 - usun termin
    """
    )

    choice = input("Wybierasz: ")
    print()

    if choice == "0":
        print("Do widzenia")

    elif choice == "1":
        print("Znajdz termin")
        print(terminy)

    elif choice == "2":
        add_termin = input("Dodaj termin: ")
        terminy.append(add_termin)
        terminy.sort(reverse=True)

    elif choice == "3":
        add_termin = input("Wprowadz nowy termin: ")
        

        
        
            





