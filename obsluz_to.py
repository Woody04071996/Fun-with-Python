#Obsluz to
#Demonstruje obsluge wyjatkow

#try/except
try:
    num = float(input("Wprowadz liczbe: "))
except:
    print("Wystapil jakis blad!")

#specyfikacja trypu wyjatku

try:
    num = float(input("Wprowadz liczbe: "))
except ValueError:
    print("To nie byla liczba")

#obsluz kilka typow wyjatkow
print()
for value in (None, "Hej!"):
    try:
        print("Proba konwersji:", value, "-->", end=" ")
        print(float(value))
    except (TypeError, ValueError):
        print("Wystapil jakis blad!")


print()
for value in (None, "Hej!"):
    try:
        print("Proba konwersji:", value, "-->", end=" ")
        print(float(value))
    except TypeError:
        print("Mozliwa jest tylko konwersja lancucha lub liczby!")
    except ValueError:
        print("Mozliwa jest tylko konwersja lancucha cyfr!")

#pobierz argument wyjatku
try:
    num = float(input("Wprowadz liczbe: "))
except ValueError as e:
    print("To nie byla liczba! Lub wyrazajaca to na sposob Pythona...")
    print(e)


#try/except/else
try:
    num = float(input("Wprowadz liczbe: "))
except ValueError:
    print("To nie byla liczba!")
else:
    print("Wprowadziles liczbe", num)

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")

