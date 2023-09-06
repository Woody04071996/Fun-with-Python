#Marynowanie danych
#Demonstruje marynowanie i odkladnaie danych na polke

import pickle, shelve

print("Marynowanie list.")
variety = ["lagodny", "pikantny", "kwaszony"]
shape = ["caly", "krojony wzdluz", "w plasterkach"]
brand = ["Dawtona", "Klimex", "Vortomnus"]
f = open("pikle1.dat", "wb")
pickle.dump(variety, f)
pickle.dump(shape, f)
pickle.dump(brand, f)
f.close()

print("\nOdmarynowanie list.")
f = open("pikle1.dat", "rb")
variety = pickle.load(f)
shape = pickle.load(f)
brand = pickle.load(f)

print(variety)
print(shape)
print(brand)
f.close()

print("\nOdkladanie listy na polkach.")
s = shelve.open("pikle2.dat")

s["odmiana"] = ["lagodny", "pikantny", "kwaszony"]
s["ksztalt"] = ["caly", "krojony wzdluz", "w plasterkach"]
s["marka"] = ["Dawtona", "Klimex", "Vortomnus"]

s.sync()

print("\nPobieranie listy z pliku polki:")
print("marka -", s["marka"])
print("ksztalt -", s["ksztalt"])
print("odmiana -", s["odmiana"])

s.close()

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
