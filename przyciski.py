#leniwe przyciski
#Tworzenie przyciskow

from tkinter import *

# okno glowne
root = Tk()
root.title("Leniwe przyciski")
root.geometry("400x200")

#utworznie w oknie ramki jako pojemnik na inne widzety
app = Frame(root)

app.grid()

#tworze w ramce etykiete
bttn1 = Button(app, text = "nic nie robie")

bttn1.grid()

#drugi przycisk

bttn2 = Button(app)
bttn2.grid()
bttn2.configure(text = "Ja rowniez")


bttn3 = Button(app)
bttn3.grid()

bttn3["text"]= "To samo mnie dotyczy"







#uruchomienie petli zdarzen
root.mainloop()
