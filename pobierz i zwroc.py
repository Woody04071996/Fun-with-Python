#Pobierz i zwroc
#demonstruje parametry i wartosci zwrotne
def display(message):
    print(message)

def give_me_five():
    five = 5
    return five

def ask_yes_no(question):
    """Zadaj pytanie, na ktore mozna odpowiedziec tak lub nie ."""
    response = None
    while response not in ("t", "n"):
        response = input(question).lower()
    return response
#main
display("To wiadomosc do Ciebie.\n")
number = give_me_five()
print("Oto co otrzymalem z funkcji give_me_five():", number)
answer = ask_yes_no("\nProsze wprowadzic  't' lub 'n': ")
print("Dziekuje za wprowadzenie:", answer)

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
