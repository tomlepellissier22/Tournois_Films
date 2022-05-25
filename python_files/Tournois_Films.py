from random import shuffle
from python_files.Constantes import *
from python_files.Elimination_By_Def import Elimination_by_Def
from python_files.Film import Film
from python_files.Arbre import Arbre
from python_files.Groupe import Groupe
from python_files.Input_fonction import Input_fonction


class Tournois_Film:

    def __init__(self) -> None:
        self.List_Films_En_Jeux: list[Film] = []
        self.List_Films_Pas_Vue: list[Film] = []
        self.List_Films_Elimines: list[list[Film]] = []
        self.isBot: bool = True #if Input_fonction(["Es-tu un bot ? (1 => Oui, 2 => Non)"], 1, 2) == 1 else False

        self.nb_match = 0

    def genere_list_films(self, nb_films: int) -> list[Film]:
        return [Film(i+1, "Film n°" + str(i+1)) for i in range(nb_films)]

    def choix_base_de_donnees(self):

        if self.isBot == False:
            list_texte: list[str] = []
            list_texte.append("Choisis la base de données: 1=>Grande (1000 Films), 2=>Moyenne (500 Films), 3=>Petite (200 Films)")

            val = Input_fonction(list_texte, 1, 3)
        else:
            val = 1

        if val == 1:
            self.List_Films_En_Jeux = self.genere_list_films(100)
        elif val == 2:
            self.List_Films_En_Jeux = self.genere_list_films(50)
        else:
            self.List_Films_En_Jeux = self.genere_list_films(10)
        
        shuffle(self.List_Films_En_Jeux)
    
    def enleve_films_pas_vue(self):
        index = 0
        while index < len(self.List_Films_En_Jeux):

            if not(self.isBot):
                list_texte: list[str] = []
                list_texte.append("As-tu vue le film suivant ? (1=>Oui, 2=>Non)")
                list_texte.append(self.List_Films_En_Jeux[index].toString())

                val = Input_fonction(list_texte, 1, 3)

                if val == 1:
                    index += 1
                if val == 2:
                    self.List_Films_Pas_Vue.append(self.List_Films_En_Jeux.pop(index))

            else:
                if self.List_Films_En_Jeux[index].id > nb_films*(1-(pourcentage_films_pas_vue)/100):
                    self.List_Films_Pas_Vue.append(self.List_Films_En_Jeux.pop(index))
                else:
                    index += 1
    
    def enleve_films_pas_vue_et_nul(self):
        index = 0
        while index < len(self.List_Films_En_Jeux):

            if not(self.isBot):
                list_texte: list[str] = []
                list_texte.append("Le film suivant fait-il partie de ton top meilleurs film ou pas vue ? (1=>Oui, 2=>Non, 3=>Pas Vue)")
                list_texte.append(self.List_Films_En_Jeux[index].toString())

                val = Input_fonction(list_texte, 1, 3)

                if val == 1:
                    index += 1
                if val == 2:
                    self.List_Films_Elimines[0].append(self.List_Films_En_Jeux.pop(index))
                if val == 3:
                    self.List_Films_Pas_Vue.append(self.List_Films_En_Jeux.pop(index))

            else:
                if self.List_Films_En_Jeux[index].id > nb_films*(1-(pourcentage_films_pas_vue)/100):
                    self.List_Films_Pas_Vue.append(self.List_Films_En_Jeux.pop(index))
                elif self.List_Films_En_Jeux[index].id > nb_films*(1-(100-pourcentage_meilleurs_films)/100):
                    self.List_Films_Elimines[0].append(self.List_Films_En_Jeux.pop(index))
                else:
                    index += 1
    
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
            print("TIER n°",taille-i," -----------------")
            for film in self.List_Films_Elimines[i]:
                film.affichage()

        print("Liste films en jeux")
        for film in self.List_Films_En_Jeux:
            film.affichage()
    
    def lance_type(self, type, nb_films_fin: int, nb_equipes_par_groupe: int = 0, nb_match_par_films: int = -1):
        if nb_equipes_par_groupe == 0:
            list_type: type = type(self.List_Films_En_Jeux.copy(), nb_films_fin, self.isBot)
        else:
            list_type: type = type(self.List_Films_En_Jeux.copy(), nb_films_fin, self.isBot, nb_equipes_par_groupe, nb_match_par_films)
        list_type.joue()
        self.nb_match += list_type.nb_match
        self.List_Films_Elimines += list_type.tier_list[:-1]
        self.List_Films_En_Jeux = list_type.tier_list[-1]

    def start_tournois(self):

        self.choix_base_de_donnees()

        self.enleve_films_pas_vue_et_nul()

        #self.lance_type(Groupe, 100, 10)

        self.lance_type(Elimination_by_Def, 10)

        self.lance_type(Arbre, 1)
        self.affichage()

        #print("Nb match total Arbre :", arbre.nb_match)
        #print("Nb match total Groupe :", groupe.nb_match)
        #print("Nb match total Elimination :", elimination.nb_match)
        print("Nb match total :", self.nb_match)