from python_files.Film import Film
from python_files.Resultat import Resultat
from python_files.Input_fonction import Input_fonction

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

        list_texte: list[str] = []
        list_texte.append("Match")
        list_texte.append(self.film1.toString())
        list_texte.append("contre")
        list_texte.append(self.film2.toString())
        list_texte.append("Que choisis-tu ? (1=>Victoire, 2=>Défaite)")

        return Resultat(Input_fonction(list_texte, 1, 2))

    def match_bot(self) -> Resultat:
            
        if self.film1.id>self.film2.id:
            return Resultat.DEFAITE
        else:
            return Resultat.VICTOIRE
