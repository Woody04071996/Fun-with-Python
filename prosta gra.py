#Prosta gra
#Demonstruje import modulow

import gry, random

print("Witaj w najprostrzej grze na swiecie")

again = None
while again != "n":
    players = []
    num = gry.ask_number(question = "Podaj liczbe graczy (2 - 5): ", low = 2, high = 5)

for i in range(num):
    name = input("Nazwa gracza: ")
    score = random.randrange(100) + 1
    player = gry.Player(name, score)
    players.append(player)

print("\nOto wynik gry:")
for player in players:
    print(player)


again = gry.ask_yes_no("\nCzy chcesz zagrac ponownie? (t/n):")

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
