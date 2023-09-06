import random
orzeł = 0
reszka = 0
rzut = 0
 
while True:
    rzut += 1
    losowanie = random.randint(1, 2)
    if rzut > 100:
        break
    elif losowanie == 1:
        orzeł += 1
    else:
        reszka += 1
 
 
print("Stukrotne rzucenie monetą pozwoliło ci otrzymać następujące wyniki:")
print("Wynik orzeł otrzymano: ", orzeł, " razy,\n\
a wynik reszka: ", reszka, " razy.")
