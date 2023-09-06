import pickle, shelve

print("How create list module 'dat'")

brands = ["Ford", "Chevrolet", "BMW", "Audi", "VW"]
models = ["Focus", "Aveo", "F90", "A8", "Polo"]
types = ["Combi", "Cabrio", "Sedan", "Hatchback", "Limusine"]
f = open("Cars.dat", "wb")
pickle.dump(brands, f)
pickle.dump(models, f)
pickle.dump(types, f)
f.close()

print("Opening lists module")
f = open("Cars.dat", "rb")
brands = pickle.load(f)
models = pickle.load(f)
types = pickle.load(f)
print(brands)
print(models)
print(types)
f.close()

