from python_files.Match import *
from python_files.Resultat import *
from random import shuffle

class Arbre:
    def __init__(self, list_films: list[Film], nb_films_fin_max: int, isBot: bool):
        self.arbre: list[list[Film]] = []
        self.arbre.append(list_films)
        self.nb_films_fin_max: int = nb_films_fin_max
        self.isBot: bool = isBot

        self.id_film: int = 0
        self.id_tour: int = 0

        self.nb_match: int = 0

        self.melange_et_qualifie_film_si_nombre_impaire()

    def is_fini(self):
        return (self.id_film == 0) and (len(self.arbre[self.id_tour]) <= self.nb_films_fin_max)

    def melange_et_qualifie_film_si_nombre_impaire(self):
        shuffle(self.arbre[self.id_tour])
        self.arbre.append([])
        if len(self.arbre[self.id_tour])%2==1 and not(self.is_fini()):
            self.ajout_film_tour_suivant(len(self.arbre[self.id_tour])-1)

    def prochain_match(self):
        if ((self.id_film + 3) < len(self.arbre[self.id_tour])):
            self.id_film += 2
        else:
            self.id_film = 0
            self.id_tour += 1
            self.melange_et_qualifie_film_si_nombre_impaire()

    def ajout_film_tour_suivant(self, id_film: int):
        self.arbre[self.id_tour+1].append(self.arbre[self.id_tour][id_film])

    def joue_match(self):
        self.nb_match += 1
        
        film1 = self.arbre[self.id_tour][self.id_film]
        film2 = self.arbre[self.id_tour][self.id_film+1]
        resultat: Resultat = Match(film1, film2, self.isBot).joue_match()

        if resultat == Resultat.VICTOIRE:
            self.ajout_film_tour_suivant(self.id_film)
        else:
            self.ajout_film_tour_suivant(self.id_film+1)
    
    def joue_arbre(self):
        while not(self.is_fini()):
            self.joue_match()
            self.prochain_match()

    def affichage(self):
        for i in range(len(self.arbre)):
            print("TIER n°",i+1," -----------------")
            for film in self.arbre[i]:
                film.affichage()
