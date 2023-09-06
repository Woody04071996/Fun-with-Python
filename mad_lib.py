#Mad Lib
#Tworzy opowiadanie oparte na szczegolach wprowadzonych przez uzytkownika

from tkinter import *


class Application(Frame):
    """
    Aplikacja z GUI, ktora tworzy opowiadanie oparte na danych
    """

    def __init__(self, master):
        """Inicjalizuje ramke"""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """
        tworzy widzety potrzebne do pobrania informacji podanych przez
        uzytkownika i wyswietlenia opowiadania.
        """
        #utworz etykiete z instrukcja
        Label(self,
              text = "Wprowadz informacje do nowego opowiadnia"
              ).grid(row = 0, column = 0, columnspan = 2, sticky = W)

        #tworze etykiete i pole znakowe do wpisania imienia osoby
        Label(self,
              text = "Osoba: "
              ).grid(row = 1, column = 0, sticky = W)
        self.person_ent = Entry(self)
        self.person_ent.grid(row = 1, column = 1, sticky = W)

        #tworze etykiete i pole znakowe do wpisania rzeczownika w liczbie mnogiej
        Label(self,
              text = "Rzeczownik w liczbie mnogiej:"
              ).grid(row = 2, column = 0, sticky = W)
        self.noun_ent = Entry(self)
        self.noun_ent.grid(row = 2, column = 1, sticky = W)

        #tworze etykiete i pole znakowe sluzace do wpisania czasownika
        Label(self,
              text = "Czasownik:"
              ).grid(row = 3, column = 0, sticky = W)
        self.verb_ent = Entry(self)
        self.verb_ent.grid(row = 3, column = 1, sticky = W)

        #tworze etykiete do pol wyboru przymiotnikow
        Label(self,
              text = "Przymiotnik(i):"
              ).grid(row = 4, column = 0, sticky = W)

        #tworze pole wyboru przymiotnika 'naglace'
        self.is_itchy = BooleanVar()
        Checkbutton(self,
                    text = "naglace",
                    variable = self.is_itchy
                    ).grid(row = 4, column = 1, sticky = W)

        #tworze pole wyboru przymiotnika 'radosne'
        self.is_joyous = BooleanVar()
        Checkbutton(self,
                    text = "radosne",
                    variable = self.is_joyous
                    ).grid(row = 4, column = 2, sticky = W)

        #tworze pole wyboru przymiotnika 'elektryzujace'
        self.is_electric = BooleanVar()
        Checkbutton(self,
                    text = "Elektryzujace",
                    variable = self.is_electric
                    ).grid(row = 4, column = 3, sticky = W)
        #tworze etykiete do przyciskow opcji odnoszacych sie do czesci ciala
        Label(self,
              text = "Czesc ciala: "
              ).grid(row = 5, column = 0, sticky = W)

        #tworze zmienna na pojedyncze czesci ciala
        self.body_part = StringVar()
        self.body_part.set(None)

        #tworze przyciski opcji odnoszacych sie do czesci ciala
        body_parts = ["pepek", "duzy palec u nogi", "rdzen przedluzony" ]
        column = 1
        for part in body_parts:
            Radiobutton(self,
                        text = part,
                        variable = self.body_part,
                        value = part
                        ).grid(row = 5, column = column, sticky = W)
            column += 1

        #tworze przycisk akceptujacy dane
        Button(self,
               text = "Kliknij, aby wyswietlic opwiadanie",
               command = self.tell_story
               ).grid(row = 6, column = 0, sticky = W)

        self.story_txt = Text(self, width = 75, height = 10, wrap = WORD)
        self.story_txt.grid(row = 7, column = 0, columnspan = 4)

    def tell_story(self):
        """Wpisz pole tekstowe nowe opowiadanie oparte na danych uzytkownika."""
        #pobierz wartosc z interfejsu GUI
        person = self.person_ent.get()
        noun = self.noun_ent.get()
        verb = self.verb_ent.get()
        adjectives = ""
        if self.is_itchy.get():
            adjectives += "naglace, "
        if self.is_joyous.get():
            adjectives += "radosne, "
        if self.is_electric.get():
            adjectives += "elektryzujace, "
        body_part = self.body_part.get()

        #create the story
        story = "Slawny badacz i odkrywca"
        story += person
        story += " o malo co nie zrezygnowal z zyciowej misji poszukiwania"
        story += "zaginionego miasta, ktore zamieszkiwal "
        story += noun
        story += ", gdy pewnego dnia "
        story += noun
        story += " znalazl "
        story += person + "a. "
        story += "Silne, "
        story += adjectives
        story += "osobliwe uczucie owladnelo badaczem"
        story += "Po tak dlugim czasie poszukiwania wreszcie sie zakonczylo. W oku "
        story += person + "a pojawila sie lza, ktora spadla na niego"
        story += body_part + ". "
        story += "A wtedy "
        story += noun
        story += " szybko pozarly "
        story += person + "a. "
        story += "Jaki moral plynie z tego opowiadnia? Pomysl, zanim zaczniesz cos "
        story += verb
        story += "."

        #wyswietl opowiadnie
        self.story_txt.delete(0.0, END)
        self.story_txt.insert(0.0, story)


#czesc glowna
root = Tk()
root.title("MadLib")

app = Application(root)

root.mainloop()
            
            
                
            
        
