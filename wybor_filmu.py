#wybor filmu
#Demonstruje pola wyboru

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
              text = "Wybierz swoje ulubione gatunki filmow."
              ).grid(row = 0, column = 0, sticky = W)
        #tworze etykiete z instrukcja
        Label(self,
              text = "Zaznacz wszystkie, ktore chcialbys wybrac:"
              ).grid(row = 1, column = 0, sticky = W)
    #tworze pole wyboru rodzaju filmu
        self.likes_comedy = BooleanVar()
        Checkbutton(self,
                    text = "Komedia",
                    variable = self.likes_comedy,
                    command = self.update_text
                    ).grid(row = 2, column = 0, sticky = W)

        self.likes_drama = BooleanVar()
        Checkbutton(self,
                    text = "Drama",
                    variable = self.likes_drama,
                    command = self.update_text
                    ).grid(row = 3, column = 0, sticky = W)

        self.likes_romance = BooleanVar()
        Checkbutton(self,
                    text = "Komedia",
                    variable = self.likes_romance,
                    command = self.update_text
                    ).grid(row = 4, column = 0, sticky = W)

        #tworze pole tekstowe do wyswietlenia wynikow
        self.results_txt = Text(self, width = 80, height = 10, wrap = WORD)
        self.results_txt.grid(row = 5, column = 0, columnspan = 3)

    def update_text(self):
        """Zaktualizuj pole tekstowe i wyswietl ulubione gatunki filow uzytkownika."""
        likes = ""

        if self.likes_comedy.get():
            likes += "Lubisz filmy komediowe.\n"
        if self.likes_drama.get():
            likes += "Lubisz dramaty filmowe.\n"
        if self.likes_romance.get():
            likes += "lubisz filmy romantyczne.\n"
        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0,likes)
            




#czesc glowna
root = Tk()
root.title("Dlugowiecznosc")
root.geometry("300x150")

app = Application(root)

root.mainloop()
    
        
        

    
