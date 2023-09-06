#Metkownica
#Tworzenie Etykiety

from tkinter import *

# okno glowne
root = Tk()
root.title("Metkownica")
root.geometry("200x50")

#utworznie w oknie ramki jako pojemnik na inne widzety
app = Frame(root)

app.grid()

#tworze w ramce etykiete
lbl = Label(app, text = "Jestem etykieta!")

lbl.grid()

#uruchomienie petli zdarzen
root.mainloop()
