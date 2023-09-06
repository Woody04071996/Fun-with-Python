#zgadywanie loiczb
#gra z komputerem

import random

print("\tWitaj w grze 'Jaka to liczba'!")
print("\nMam na myśli pewną liczbę z zakresu od 1 do 20.")
print("Komputer probuje ja odgadnąć w jak najmniejszej liczbie prób.\n")

#wartosci poczatkowe
number = int(input("wybierasz liczbe: "))
quess = random.randint (1, 20)
trie = 0

while guess != number:
    if guess > number:
        print("Za dużo")
        guess = random.randint(1, 20)
        tries += 1
        print("Zgaduję:", guess)
    else:
        print("Za mało")
        guess = random.randint(1, 20)
        tries += 1
        print("Zgadujęę:", guess)
print("Komputer zgadł za", tries,"razem.")
    
    
     
    
