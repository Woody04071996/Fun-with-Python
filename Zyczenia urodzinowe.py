#Zyczenia urodzinowe
#Demonstruje argumenty nazwane

#prametry pozycyjne
def birthday1(name,age):
    print("Szczesliwych urodzin,", name, "Masz juz", age, "lat.\n")

def birthday2(name= "Maciej", age = 25):
    print("Szczesliwych urodzin ", name, "Masz juz", age, "lat.\n")

birthday1("Maciej", 25)
birthday1(25, "Maciej")
birthday1(name = "Maciej", age = 25)
birthday1(age = 25, name = "Maciej")

birthday2()
birthday2(name = "Katarzyna")
birthday2(age = 17)
birthday2(name = "Katarzyna", age = 19)
birthday2("Katarzyna", 17)
