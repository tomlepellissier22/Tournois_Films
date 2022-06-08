from python_files.Match import Match
from python_files.Film import Film
from python_files.Resultat import Resultat
from random import shuffle

class Groupe:
    def __init__(self, list_films: list[Film], nb_films_fin: int, isBot: bool, isSauvegarde: bool, nb_equipes_par_groupe: int, nb_match_par_film: int = -1):
        self.nb_equipe_par_groupe: int = 4 if (nb_equipes_par_groupe <= 4) else nb_equipes_par_groupe
        self.nb_groupes: int = len(list_films)//nb_equipes_par_groupe if ((len(list_films)//nb_equipes_par_groupe)*nb_equipes_par_groupe == len(list_films)) else (len(list_films)//nb_equipes_par_groupe)+1

        self.tier_list: list[list[Film]] = [[]]
        self.list_groupe: list[list[Film]] = [[] for _ in range(self.nb_groupes)]
        self.isBot: bool = isBot

        self.id_groupe: int = 0
        self.id_tour: int = 0
        self.num_match: int = 0

        self.nb_match: int = 0
        self.nb_films_fin: int = nb_films_fin

        self.initialisation_groupe(list_films)

        self.nb_match_par_film: int = self.nb_equipe_par_groupe-1 if (nb_match_par_film == -1) else nb_match_par_film

        self.list_id_top: list[int] = []
        self.list_id_bot: list[int] = []
        self.initialisation_id_match()

        self.id_film1: int = self.list_id_top[self.num_match]
        self.id_film2: int = self.list_id_bot[self.num_match]

    def initialisation_groupe(self, list_films: list[Film]):
        shuffle(list_films)
        id_groupe = 0
        while len(list_films) > 0:
            self.list_groupe[id_groupe].append(list_films.pop())

            id_groupe += 1
            if id_groupe >= self.nb_groupes:
                id_groupe = 0

    def initialisation_id_match(self):
        if self.nb_equipe_par_groupe%2 == 1:
            self.nb_equipe_par_groupe += 1
        
        self.list_id_top = [i for i in range(self.nb_equipe_par_groupe//2)]
        self.list_id_bot = [self.nb_equipe_par_groupe-i-1 for i in range(self.nb_equipe_par_groupe//2)]

    def prochain_match(self):
        self.id_groupe += 1

        if self.id_groupe >= self.nb_groupes:
            self.id_groupe = 0

            self.match_suivant()
    
    def match_suivant(self):
        self.num_match += 1
        if self.num_match >= self.nb_equipe_par_groupe//2:
            self.num_match = 0
            self.rotation_id_match()
        
        self.id_film1 = self.list_id_top[self.num_match]
        self.id_film2 = self.list_id_bot[self.num_match]
    
    def rotation_id_match(self):
        self.id_tour += 1

        last = self.list_id_top.pop()
        first = self.list_id_bot.pop(0)

        self.list_id_bot.append(last)

        if len(self.list_id_top) >= 2:
            self.list_id_top = [self.list_id_top[0]] + [first] + self.list_id_top[1:]
        else:
            self.list_id_top = [self.list_id_top[0]] + [first]

    def joue_match(self):
        if (self.id_film1 < len(self.list_groupe[self.id_groupe])) and (self.id_film2 < len(self.list_groupe[self.id_groupe])):
            self.nb_match += 1
            
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

    def joue(self):
        while not(self.is_fini()):
            self.joue_match()
            self.prochain_match()
        
        self.trie_groupe()
        self.genere_tier_list()

        return False
    
    def trie_groupe(self):
        for groupe in self.list_groupe:
            groupe.sort(key=lambda film: film.nb_vic, reverse=True)

    def genere_tier_list(self):
        list_groupe_copy = self.list_groupe.copy()
        nb_equipe: int = len(list_groupe_copy[0])
        num_tier_list: int = 0
        while self.nb_groupes * nb_equipe > self.nb_films_fin:
            for groupe in list_groupe_copy:
                if len(groupe) == nb_equipe:
                    self.tier_list[num_tier_list].append(groupe.pop())
            
            num_tier_list += 1
            self.tier_list.append([])
            nb_equipe= len(list_groupe_copy[0])
        
        if len(list_groupe_copy[0]) == 0:
            self.tier_list.remove([])
        else:
            for groupe in list_groupe_copy:
                self.tier_list[num_tier_list] += groupe

    def affichage_groupe(self):
        for i in range(len(self.list_groupe)):
            print(f"GROUPE n°{i+1} -----------------")
            for film in self.list_groupe[i]:
                film.affichage()

    def affichage(self):
        taille = len(self.tier_list)
        for i in range(taille):
            print(f"TIER n°{taille-i} -----------------")
            for film in self.tier_list[i]:
                film.affichage()
