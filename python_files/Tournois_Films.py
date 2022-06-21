from random import shuffle
from python_files.Constantes import *
from python_files.Display_fonction import choix_base_de_donnees, choix_question, display_one_films
from python_files.Elimination_By_Def import Elimination_by_Def
from python_files.Film import Film
from python_files.Arbre import Arbre
from python_files.Genere_Base_De_Donnee import genere_base_de_donne
from python_files.Resultat import Resultat
from python_files.Sauvegarde import charge_sauvegarde, charge_tier_liste, sauvegarde, sauvegarde_tier_liste, sauvegarde_tier_liste_humain


class Tournois_Film:

    def __init__(self) -> None:
        self.List_Films_Depart: list[Film] = []
        self.List_Films_Restants: list[Film] = []
        self.List_Films_Pas_Vue: list[Film] = []
        self.List_Films_Elimines: list[list[Film]] = [[]]
        self.tier_list = [[]]
        self.isBot: bool = ISBOT
        self.isSauvegarde = False

        self.nb_match = 0

    def genere_list_films(self, nb_films: int) -> list[Film]:
        return [Film(i+1, "Film n°" + str(i+1)) for i in range(nb_films)]

    def choix_base_de_donnees(self):

        if self.isBot == False:
            val = choix_base_de_donnees()
        else:
            val = 1

        if val == 1:
            self.List_Films_Depart = genere_base_de_donne(
                ID_LISTE_TOUS_LES_FILMS)
        elif val == 2:
            self.List_Films_Depart = genere_base_de_donne(
                ID_LISTE_MEILLEUR_FILMS_GRAND)
        else:
            self.List_Films_Depart = genere_base_de_donne(
                ID_LISTE_MEILLEUR_FILMS_PETIT)

        shuffle(self.List_Films_Depart)

    def enleve_films_pas_vue(self):
        index = 0
        while index < len(self.List_Films_Depart):
            self.nb_match += 1

            if not(self.isBot):
                val = display_one_films(self.List_Films_Depart[index], False)

                if val == Resultat.BIEN:
                    self.List_Films_Restants.append(
                        self.List_Films_Depart.pop(index))
                if val == Resultat.PAS_VUE:
                    self.List_Films_Pas_Vue.append(
                        self.List_Films_Depart.pop(index))
                if val == Resultat.SAUVEGARDE:
                    self.sauvegarde()
                    self.isSauvegarde = True
                if val == Resultat.FIN:
                    self.isSauvegarde = True
            else:
                if self.List_Films_Depart[index].id > nb_films*(1-(pourcentage_films_pas_vue)/100):
                    self.List_Films_Pas_Vue.append(
                        self.List_Films_Depart.pop(index))
                else:
                    self.List_Films_Restants.append(
                        self.List_Films_Depart.pop(index))

    def enleve_films_pas_vue_et_nul(self):
        index = 0
        while index < len(self.List_Films_Depart) and self.isSauvegarde == False:
            self.nb_match += 1

            if not(self.isBot):
                val = display_one_films(self.List_Films_Depart[index], True)

                if val == Resultat.BIEN:
                    self.List_Films_Restants.append(
                        self.List_Films_Depart.pop(index))
                if val == Resultat.PAS_VUE:
                    self.List_Films_Pas_Vue.append(
                        self.List_Films_Depart.pop(index))
                if val == Resultat.NUL:
                    self.List_Films_Elimines[0].append(
                        self.List_Films_Depart.pop(index))
                if val == Resultat.SAUVEGARDE:
                    self.sauvegarde()
                    self.isSauvegarde = True
                if val == Resultat.FIN:
                    self.isSauvegarde = True
            else:
                if self.List_Films_Depart[index].id > nb_films*(1-(pourcentage_films_pas_vue)/100):
                    self.List_Films_Pas_Vue.append(
                        self.List_Films_Depart.pop(index))
                elif self.List_Films_Depart[index].id > nb_films*(1-(100-pourcentage_meilleurs_films)/100):
                    self.List_Films_Elimines[0].append(
                        self.List_Films_Depart.pop(index))
                else:
                    self.List_Films_Restants.append(
                        self.List_Films_Depart.pop(index))

    def reset_all_data(list_films: list[Film]):
        for film in list_films:
            film.reset_data()

    def affichage(self):
        print("Liste films pas vues")
        for film in self.List_Films_Pas_Vue:
            film.affichage()

        print("Liste films éliminés")
        taille = len(self.List_Films_Elimines)
        for i in range(taille):
            print("TIER n°", taille-i, " -----------------")
            for film in self.List_Films_Elimines[i]:
                film.affichage()

        print("Liste films en jeux")
        for film in self.List_Films_Depart:
            film.affichage()

        print("Liste films Restants")
        for film in self.List_Films_Restants:
            film.affichage()

    def lance_type(self, type, nb_films_fin: int, isSauvegarde: bool, nb_equipes_par_groupe: int = 0, nb_match_par_films: int = -1):
        if nb_equipes_par_groupe == 0:
            list_type: type = type(self.List_Films_Restants.copy(
            ), nb_films_fin, self.isBot, isSauvegarde)
        else:
            list_type: type = type(self.List_Films_Restants.copy(
            ), nb_films_fin, self.isBot, isSauvegarde, nb_equipes_par_groupe, nb_match_par_films)
        self.isSauvegarde = list_type.joue()
        self.nb_match += list_type.nb_match

        if self.isSauvegarde == False:
            self.List_Films_Elimines += list_type.tier_list[:-1]
            self.List_Films_Restants = list_type.tier_list[-1]

    def sauvegarde(self):
        Liste_Info_General = [self.List_Films_Restants, self.List_Films_Pas_Vue,
                              self.List_Films_Elimines, self.List_Films_Depart]
        sauvegarde(Liste_Info_General)

    def display_tier_liste(self):
        self.tier_list: list[list[Film]] = [self.List_Films_Pas_Vue.copy()] + self.List_Films_Elimines.copy() + [self.List_Films_Restants.copy()]

        while True:
            try:
                self.tier_list.remove([])
            except ValueError:
                break

        sauvegarde_tier_liste(self.tier_list)
        sauvegarde_tier_liste_humain(self.tier_list)

        print("Tier Liste")
        taille = len(self.tier_list)
        for i in range(taille):
            print("TIER n°", taille-i, " -----------------")
            for film in self.tier_list[i]:
                film.affichage()

    def charger_sauvegarde(self):
        val = choix_question("Veux-tu charger la sauvegarde ?")

        if val == 1:
            self.List_Films_Restants, self.List_Films_Pas_Vue, self.List_Films_Elimines, self.List_Films_Depart = charge_sauvegarde()

        return val == 1
    
    def charger_and_display_tier_list(self):
        val = choix_question("Veux-tu afficher la tier_list sauvegardé ?")

        if val == 1:
            self.tier_list = charge_tier_liste()

        return val == 1

    def start_tournois(self):

        afficher_tier_list_sauvegarde = False
        try:
            fichier = open("Sauvegarde/Tier_liste", "rb")
            fichier.close()
            afficher_tier_list_sauvegarde = self.charger_and_display_tier_list()

            if afficher_tier_list_sauvegarde:
                self.display_tier_liste()
        except:
            print("Pas de tier_list existante")

        if afficher_tier_list_sauvegarde == False:
            sauvegarde_existante = False
            try:
                fichier = open("Sauvegarde/Liste_info_General", 'rb')
                fichier.close()
                sauvegarde_existante = self.charger_sauvegarde()
            except:
                print("Pas de sauvegarde existante")

            if sauvegarde_existante:
                if len(self.List_Films_Depart) > 0:
                    sauvegarde_existante = False
            else:
                self.choix_base_de_donnees()

            if sauvegarde_existante == False:
                enleve_films = choix_question(
                    "Veux-tu enlever les films que tu n'as pas vue de la base de donnée ?")
                if enleve_films == 1:
                    self.enleve_films_pas_vue_et_nul()
                else:
                    self.List_Films_Restants = self.List_Films_Depart.copy()
                    self.List_Films_Depart = []

            if self.isSauvegarde == False and len(self.List_Films_Restants) > NB_FILMS_AFTER_ELIMINATION:
                print("Debut Elimination")
                self.lance_type(Elimination_by_Def, NB_FILMS_AFTER_ELIMINATION, sauvegarde_existante)

            if self.isSauvegarde == False and len(self.List_Films_Restants) > NB_FILMS_AFTER_ARBRE :#and len(self.List_Films_Restants) <= NB_FILMS_AFTER_ELIMINATION:
                print("Debut Arbre")
                self.lance_type(Arbre, NB_FILMS_AFTER_ARBRE, sauvegarde_existante)

            if self.isSauvegarde:
                self.sauvegarde()

            if self.isSauvegarde == False and len(self.List_Films_Restants) > 0:
                print("Nb match total :", self.nb_match)
                self.display_tier_liste()
