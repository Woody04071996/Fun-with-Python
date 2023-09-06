#leniwe przyciski 2
#Klasy przy tworzeniu programow GUI

from tkinter import *

class Application(Frame):
    """Inicjalizuje ramke"""
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    

    def create_widgets(self):
        """Utworz trzy przyciski, ktore nic nie robia"""
        #pierwszy przycisk
        self.bttn1 = Button(self, text = "nic nie robie")
        self.bttn1.grid()

        #drugi przycisk
        self.bttn2 = Button(self)
        self.bttn2.grid()
        self.bttn2.configure(text = "Ja rowniez")

        #trzeci przycisk
        self.bttn3 = Button(self)
        self.bttn3.grid()
        self.bttn3["text"] = "To samo mnie dotyczy"


root = Tk()
root.title("Leniwe przyciski 2")
root.geometry("400x200")
app = Application(root)
root.mainloop()
