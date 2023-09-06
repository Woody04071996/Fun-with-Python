#licznik klikniec
#Powiazuje zdarzenia z procedura obslugi zdarzen

from tkinter import *

class Application(Frame):
    """Inicjalizuje ramke"""
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.bttn_clicks = 0 #liczba klikniec
        self.create_widgets()

    def create_widgets(self):
        """przycisk ktory wyswietla klikniecia"""
        #pierwszy przycisk
        self.bttn = Button(self)
        self.bttn["text"] = "Liczba klikniec: 0"
        self.bttn["command"] = self.update_count
        self.bttn.grid()
    

    def update_count(self):
        """Zwieksza liczbe klikniec i wyswietla jego wartosc"""
        self.bttn_clicks += 2
        self.bttn["text"] = "Liczba klikniec: " + str(self.bttn_clicks)

root = Tk()
root.title("Leniwe przyciski 2")
root.geometry("1920x1080")
app = Application(root)
root.mainloop()
