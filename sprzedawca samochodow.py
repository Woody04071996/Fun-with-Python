#sprzedawca samochodu
#cena samochodu

print("Witaj w konfiguracji dla sprzedawcy")

car = int(input("\nWpisz cene samochodu"))
insurance = int(input("\nwpisz cene ubezpieczenia"))
registration = int(input("\nwpisz koszta rejstracji samochodu"))

tax = car / 10

total  = car + insurance + registration + tax

print("\nRazem z oplatami za Twoj samochod wyszlo" , total , "zl")
          






