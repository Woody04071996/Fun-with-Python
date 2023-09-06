#Uczestnik funduszu powierniczego dobry
#Demonstruje blad logiczny

print(
"""
           Uczestnik funduszu powierniczego

Sumuje Twoje miesiczne wydatki, zeby Twoj fundusz powierniczy sie nie wyczerpal
(bo wtedy bedziesz musial isc do prawdziwej pracy).

Wprowadz swoje wymagane miesieczne koszty . Poniewaz jestes bogaty, zignoruj
grosze i podaj swoje kwoty w pelnych zlotych

"""
)



car = int(input("Serwis Mercedesa: "))
rent = int(input("Apartament w Srodmiesciu: "))
jet = int(input("Wynajem prywatnego samolotu: "))
gifts = int(input("Podarunki: "))
food = int(input("Obiady w restauracjach: "))
staff = int(input("Personel (sluzba domowa, kucharz, kierowca, asystent): "))
guru = int(input("Osobisty guru i coach: "))
game = int(input("Gry komputerowe: "))
entertiment = int(input("Rozrywka: "))

total = car + jet + rent + gifts + food + staff + guru + game + entertiment

print("\nOgolem", total)

input("\n\nAby zakonczyc program, nacisnij klawisz Enter.")
