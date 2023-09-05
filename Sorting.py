from operator import attrgetter

class Person:

    def __init__(self, name, money=0, age=0):
        self.name = name
        self.money = money
        self.age = age

    def __repr__(self):
        return "Person({0!r}, {1}, {2})".format(self.name, self.money, self.age)

persons = []
persons.append(Person("Maciej", 50000000, 20,))
persons.append(Person("Bartek", 100000, 25))
persons.append(Person("Gosia", 200000, 28))
persons.append(Person("Jhonny", 100000, 31))


persons.sort(key=lambda x: x.name)   
persons.sort(key=lambda x: getattr(x, "name"))   
persons.sort(key=attrgetter("name"))


persons.sort(key=lambda x: x.money)
persons.sort(key=lambda x: getattr(x, "money"))
persons.sort(key=attrgetter("money"))


persons.sort(key=lambda x: x.age)
persons.sort(key=lambda x: getattr(x, "age"))
persons.sort(key=attrgetter("age"))

persons.sort(key=lambda x: (x.money, x.name))
persons.sort(key=lambda x: (getattr(x, "money"), getattr(x, "name")))
persons.sort(key=attrgetter("money", "name", "age"))


print(persons)
