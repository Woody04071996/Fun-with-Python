#Uczestnik funduszu powierniczego
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
car = input("Serwis Mercedesa: ")
rent = input("Apartament w Srodmiesciu: ")
jet = input("Wynajem prywatnego samolotu: ")
gifts = input("Podarunki: ")
food = input("Obiady w restauracjach: ")
staff = input("Personel (sluzba domowa, kucharz, kierowca, asystent): ")
guru = input("Osobisty guru i coach: ")
game = input("Gry komputerowe: ")
entertiment = input("Rozrywka: ")

total = car + jet + rent + gifts + food + staff + guru + game + entertiment

print("\nOgolem", total)

input("\n\nAby zakonczyc program, nacisnij klawisz Enter.")
