from python_files.Match import Match
from python_files.Film import Film
from python_files.Resultat import Resultat
from python_files.Constantes import NB_DEF_MAX
from random import shuffle

from python_files.Sauvegarde import charge_sauvegarde_elimination, sauvegarde_elimination


class Elimination_by_Def:
    def __init__(self, list_films: list[Film], nb_films_fin_max: int, isBot: bool, isSauvegarde: bool):
        self.list_etape_elimination: list[list[Film]] = [list_films]
        self.list_etape_elimination.append([])
        self.tier_list: list[list[Film]] = [[]]

        self.nb_films_fin_max: int = nb_films_fin_max
        self.isBot: bool = isBot

        self.isSauvegarde = isSauvegarde
        self.isFini = False

        self.id_tour: int = 0
        self.nb_match: int = 0

        self.melange_list(self.list_etape_elimination[self.id_tour])

    def melange_list(self, list_films):
        shuffle(list_films)

    def is_fini(self):
        if (len(self.list_etape_elimination[self.id_tour]) <= 1):
            nb_films = len(self.list_etape_elimination[self.id_tour+0]) + len(
                self.list_etape_elimination[self.id_tour+1])
            if nb_films <= self.nb_films_fin_max:
                if (len(self.list_etape_elimination[self.id_tour]) == 1):
                    film = self.list_etape_elimination[self.id_tour].pop()
                    self.list_etape_elimination[self.id_tour+1].append(film)
                return True
        return False

    def prochain_match(self):
        if len(self.list_etape_elimination[self.id_tour]) == 0:
            self.list_etape_elimination.append([])
            self.id_tour += 1
            self.melange_list(self.list_etape_elimination[self.id_tour])

            self.prochain_match()

        elif len(self.list_etape_elimination[self.id_tour]) == 1:
            film1 = self.list_etape_elimination[self.id_tour].pop()

            self.list_etape_elimination.append([])
            self.id_tour += 1
            self.melange_list(self.list_etape_elimination[self.id_tour])

            if len(self.list_etape_elimination[self.id_tour]) >= 1:
                film2 = self.list_etape_elimination[self.id_tour].pop()
                self.joue_match(film1, film2, True)

        elif len(self.list_etape_elimination[self.id_tour]) >= 2:
            film1 = self.list_etape_elimination[self.id_tour].pop()
            film2 = self.list_etape_elimination[self.id_tour].pop()
            self.joue_match(film1, film2, False)

    def joue_match(self, film1: Film, film2: Film, isOld: bool):
        self.nb_match += 1

        resultat: Resultat = Match(film1, film2, self.isBot).joue_match()

        if resultat == Resultat.VICTOIRE:
            self.film_victoire(film1, isOld)
            self.film_defaite(film2, False)
        elif resultat == Resultat.DEFAITE:
            self.film_defaite(film1, isOld)
            self.film_victoire(film2, False)
        elif resultat == Resultat.EGALITE_VICTOIRE:
            self.film_victoire(film1, isOld)
            self.film_victoire(film2, False)
        elif resultat == Resultat.EGALITE_DEFAITE:
            self.film_defaite(film1, isOld)
            self.film_defaite(film2, False)
        elif resultat == Resultat.EGALITE:
            self.list_etape_elimination[self.id_tour].append(film1)
            self.list_etape_elimination[self.id_tour].append(film2)
        elif resultat == Resultat.SAUVEGARDE:
            self.isSauvegarde = True
            self.list_etape_elimination[self.id_tour].append(film1)
            self.list_etape_elimination[self.id_tour].append(film2)
        elif resultat == Resultat.FIN:
            self.isFini = True

    def film_victoire(self, film: Film, isOld: bool):
        film.nb_vic += 1
        if isOld:
            self.list_etape_elimination[self.id_tour].append(film)
        else:
            self.list_etape_elimination[self.id_tour+1].append(film)

    def film_defaite(self, film: Film, isOld: bool):
        film.nb_def += 1
        if film.nb_def >= NB_DEF_MAX:
            if isOld:
                self.list_etape_elimination[self.id_tour-2].append(film)
            else:
                self.list_etape_elimination[self.id_tour-1].append(film)
        else:
            if isOld:
                self.list_etape_elimination[self.id_tour].append(film)
            else:
                self.list_etape_elimination[self.id_tour+1].append(film)

    def joue(self):
        print(self.isFini, self.isSauvegarde)
        if self.isSauvegarde:
            self.charge_sauvegarde()
            self.isSauvegarde = False

        while self.is_fini() == False and self.isSauvegarde == False and self.isFini == False:
            self.prochain_match()

        if self.isSauvegarde:
            self.sauvegarde()
        else:
            if not(self.isFini):
                self.genere_tier_list()

        return self.isSauvegarde

    def genere_tier_list(self):
        self.tier_list = self.list_etape_elimination.copy()

        while True:
            try:
                self.tier_list.remove([])
            except ValueError:
                break

    def sauvegarde(self):
        list_info_elimination = [self.id_tour,
                                 self.nb_match, self.list_etape_elimination]
        sauvegarde_elimination(list_info_elimination)

    def charge_sauvegarde(self):
        try:
            fichier = open("Sauvegarde/list_info_elimination", 'rb')
            fichier.close()
            self.id_tour, self.nb_match, self.list_etape_elimination = charge_sauvegarde_elimination()
        except:
            print("Pas de sauvegarde Elimination by def")

    def affichage(self):
        taille = len(self.list_etape_elimination)
        for i in range(taille):
            print("TIER n°", taille-i, " -----------------")
            for film in self.list_etape_elimination[i]:
                film.affichage()
