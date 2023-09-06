#jaka to liczba
#Gracz wybiera losowo liczbe od 1 do 100
#Gracz probuje ja odgadnac
#Za duza czy za mala
#prawidlowa

import random  

print("\tWitaj w grze 'Jaka to liczba'!")
print("\nMam na myśli pewną liczbę z zakresu od 1 do 20.")
print("Spróbuj ją odgadnąć w jak najmniejszej liczbie prób.\n")

# ustaw wartości początkowe
the_number = random.randint(1, 10)
guess = int(input("Ta liczba to: "))
tries = 0

# pętla zgadywania
while guess != the_number:
    if guess > the_number:
        print("Za duża...")
    elif tries > 4:
        print("Przegrałeś! Przekroczyłeś 5 prób!!! ")
        break
    else:
        print("Za mała...")
    
            
    guess = int(input("Ta liczba to: "))
    tries += 1
   
    

print("Odgadłeś! Ta liczba to", the_number)
print("Do osiągnięcia sukcesu potrzebowałeś tylko", tries, "prób!\n")
  
input("\n\nAby zakończyć program, naciśnij klawisz Enter.")

