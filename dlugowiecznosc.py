#Dlugowiecznosc
#tworzenie interfejsow GUI

from tkinter import *

class Application(Frame):
    """Aplikacja GUI, ktora moze ujawnic sekrety dlugowiecznosci."""
    def __init__(self, master):
        """Inicjalizuje ramke."""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Utworz obiekty typu button, Text i Entry."""
        #utworz etykiete z instrukcja
        self.inst_lbl = Label(self, text = "Wprowadz haslo do sekretu dlugowiecznosci")
        self.inst_lbl.grid(row = 0, column = 0, columnspan = 2, sticky = W)
        #Etykiete do hasla
        self.pw_lbl = Label(self, text = "Haslo: ")
        self.pw_lbl.grid(row = 1, column = 0, sticky = W)
        #utworz widzet Entry do przyjecia hasla
        self.pw_ent = Entry(self)
        self.pw_ent.grid(row = 1, column = 1, sticky = W)
        #tworzy przycisk akceptuj
        self.submit_bttn = Button(self, text = "Akceptuj", command = self.reveal)
        self.submit_bttn.grid(row = 2, column = 0, sticky = W)
        #tworzy widzet Text  do wywietlania komunikatu
        self.secret_txt = Text(self, width = 35, height = 5, wrap = WORD)
        self.secret_txt.grid(row = 3, column = 0, columnspan = 2, sticky = W)

    def reveal(self):
        """Wyswietl komunikat zalezny od poprawnosci hasla."""
        contents = self.pw_ent.get()
        if contents == "sekret":
            message = "OTo tajemniczy przepis na dozycie 100 lat: dozyj 99 lat", \
                        "a potem badz bardzo ostrozyny."
        else:
            message = "To nie jest poprawne haslo, wiec nie moge sie z Toba"\
                      "moim sekretem"
        self.secret_txt.delete(0.0, END)
        self.secret_txt.insert(0.0, message)

#czesc glowna
root = Tk()
root.title("Dlugowiecznosc")
root.geometry("300x150")

app = Application(root)

root.mainloop()
    
        
