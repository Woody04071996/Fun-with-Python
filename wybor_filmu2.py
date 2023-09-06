#wybor filmu 2
#Demonstruje przycisk opcji

from tkinter import *

class Application(Frame):
    """Aplikacja GUI, ktora moze ujawnic sekrety dlugowiecznosci."""
    def __init__(self, master):
        """Inicjalizuje ramke."""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Tworze widzety sluzace do wyboru gatunkow filmu"""
        #tworze etykiete z opisem
        Label(self,
              text = "Wybierz jeden gatunek filmu."
              ).grid(row = 0, column = 0, sticky = W)
        #tworze etykiete z instrukcja
        Label(self,
              text = "Wybierz jeden gatunek"
              ).grid(row = 1, column = 0, sticky = W)

        self.favorite = StringVar()
        self.favorite.set(None)

        #przycisk wyboru rodzaju filmu
        
        Radiobutton(self,
                    text = " Komedia",
                    variable = self.favorite,
                    value = " Komedia.",
                    command = self.update_text
                    ).grid(row = 2, column = 0, sticky = W)

        
        Radiobutton(self,
                    text = " Drama",
                    variable = self.favorite,
                    value = " Drama.",
                    command = self.update_text
                    ).grid(row = 3, column = 0, sticky = W)

        
        Radiobutton(self,
                    text = " Romans",
                    variable = self.favorite,
                    value = " Romans.",
                    command = self.update_text
                    
                    ).grid(row = 4, column = 0, sticky = W)

        #tworze pole tekstowe do wyswietlenia wynikow
        self.results_txt = Text(self, width = 80, height = 10, wrap = WORD)
        self.results_txt.grid(row = 5, column = 0, columnspan = 3)

    def update_text(self):
        """Zaktualizuj pole tekstowe i wyswietl ulubione gatunki filow uzytkownika."""
        message = "Twoim ulubionym gatunkiem filmu jest"
        message += self.favorite.get()

        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, message)

      
            




#czesc glowna
root = Tk()
root.title("Wybor filmu 2")
root.geometry("300x150")

app = Application(root)

root.mainloop()
    
        
        

    
