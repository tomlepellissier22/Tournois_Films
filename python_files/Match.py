from python_files.Film import Film
from python_files.Resultat import Resultat

class Match:
    def __init__(self, film1: Film, film2: Film, isBot: bool) -> None:
        self.film1: Film = film1
        self.film2: Film = film2
        self.isBot: bool = isBot
    
    def joue_match(self) -> Resultat:
        if self.isBot:
            return self.match_bot()
        else:
            return self.match_joueur()
    
    def match_joueur(self) -> Resultat:

        while(True):
            self.film1.affichage()
            print("contre")
            self.film2.affichage()
            print()

            print("Que choisis-tu ? (1=>Victoire, 2=>Défaite)")
            val = input()
            if (val!="" and int(val)>0 and int(val)<=2):
                return Resultat(val)

    def match_bot(self) -> Resultat:
            
        if self.film1.id>self.film2.id:
            return Resultat.DEFAITE
        else:
            return Resultat.VICTOIRE
