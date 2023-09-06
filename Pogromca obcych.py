#Programowanie obiektowe
#Pogromca obcych
#Demonstruje wspoldxialanie obiektow

class Player(object):
    """Gracz w grze strzelance"""
    def blast(self, enemy):
        print("Gracz razi wroga.\n")
        enemy.die()

class Alien(object):
    """Obcy w grze strzelance."""
    def die(self):
        print("Obcy z trudem lapie oddech, 'To juz koniec. Ale wielki koniec...\n" \
              "Tak juz robi sie ciemno. Powiedz moim dwom milionom larw, ze je kochalem...\n" \
              "Zegnaj okrutny wszechswiecie.'")

#main
print("\t\tSmierc Obcego\n")

hero = Player()
invader = Alien()
hero.blast(invader)

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
