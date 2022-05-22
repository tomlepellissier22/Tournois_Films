from python_files.Match import *
from python_files.Resultat import *
from random import shuffle

class Groupe:
    def __init__(self, list_films: list[Film], nb_groupes: int, isBot: bool, nb_match_par_film: int = -1):
        self.list_groupe: list[list[Film]] = [[] for _ in range(nb_groupes)]
        self.isBot: bool = isBot

        self.id_film1: int = 0
        self.id_film2: int = 1
        self.id_groupe: int = 0
        self.id_tour: int = 0

        self.nb_groupes: int = nb_groupes

        self.nb_match: int = 0

        self.initialisation_groupe(list_films)
        self.nb_match_par_film: int = len(self.list_groupe[0])-1 if (nb_match_par_film == -1) else nb_match_par_film

    def initialisation_groupe(self, list_films: list[Film]):
        shuffle(list_films)
        id_groupe = 0
        while len(list_films) > 0:
            self.list_groupe[id_groupe].append(list_films.pop())

            id_groupe += 1
            if id_groupe >= self.nb_groupes:
                id_groupe = 0

    def prochain_match(self):
        self.id_groupe += 1

        if self.id_groupe >= self.nb_groupes:
            self.id_groupe = 0

            self.match_suivant()
    
    def match_suivant(self):
        self.id_film1 = 0
        self.id_film2 = 1
    

    def joue_match(self):
        if (self.id_film1 < len(self.list_groupe[self.id_groupe])) and (self.id_film2 < len(self.list_groupe[self.id_groupe])):
            film1 = self.list_groupe[self.id_groupe][self.id_film1]
            film2 = self.list_groupe[self.id_groupe][self.id_film2]
            resultat: Resultat = Match(film1, film2, self.isBot).joue_match()

            if resultat == Resultat.VICTOIRE:
                self.list_groupe[self.id_groupe][self.id_film1].nb_vic += 1
                self.list_groupe[self.id_groupe][self.id_film2].nb_def += 1
            else:
                self.list_groupe[self.id_groupe][self.id_film1].nb_def += 1
                self.list_groupe[self.id_groupe][self.id_film2].nb_vic += 1
    
    def is_fini(self):
        return self.nb_match_par_film <= self.id_tour

    def joue_groupe(self):
        while not(self.is_fini()):
            self.nb_match += 1
            self.joue_match()
            self.prochain_match()
        
        self.genere_classement()
    
    def genere_classement(self):
        return True

    def affichage(self):
        for i in range(len(self.list_groupe)):
            print("TIER n°",i+1," -----------------")
            for film in self.arbre[i]:
                film.affichage()
