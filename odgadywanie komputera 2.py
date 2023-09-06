from random  import randint

start = 1
end = 100
number = int(input("Podaj liczbę, którą ma zgadnąć komputer: "))

guess = randint(start, end)
tries = 1
print("Pierwsza zgadywana liczba przez komputer to:", guess)
print("Liczba do zgadnięcia to:", number)

while guess != number:
    if guess > number:
        print("Zgaduję:", guess)
        print("Za dużo")
        end = guess - 1
        guess = randint(start, end)
        tries += 1

    else:
        print("Zgaduję:", guess)
        print("Za mało")
        start = guess + 1
        guess = randint(start, end)
        tries += 1

print("Komputer zgadł za", tries,"razem.")
