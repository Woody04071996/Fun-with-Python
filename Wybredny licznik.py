#Wybredny licznik
#Demonstruje instrukcje break i continue



count = 0

while True:
    count += 1
    #zakoncz petle,jesli wartosc zmiennej count jest wieksza niz 10
    if count > 100:
        break
    #Pomin liczbe 5
    if count == 6:
        continue
    print(count)
    
input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
