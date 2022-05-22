from python_files.Constantes import *
from python_files.Film import Film
from python_files.Arbre import Arbre


class Tournois_Film:

    def __init__(self, isBot: bool) -> None:
        self.List_Films_En_Jeux: list[Film] = []
        self.List_Films_Pas_Vue: list[Film] = []
        self.List_Films_Elimines: list[list[Film]] = [[]]
        self.isBot: bool = isBot

        self.nb_match = 0

    def genere_list_films(self) -> list[Film]:
        print("Grande liste ou petite liste")
        return [Film(i, "Film n°" + str(i)) for i in range(nb_films)]
    
    def enleve_films_pas_vue(self):
        index = 0
        while index < len(self.List_Films_En_Jeux):

            if not(self.isBot):
                while(True):
                    print("As-tu vue le film suivant ? (1=>Oui, 2=>Non)")
                    self.List_Films_En_Jeux[index].affiche()
                    print()

                    val = input()
                    if (val!="" and int(val)>0 and int(val)<=2):
                        if int(val) == 2:
                            self.List_Films_Pas_Vue.append(self.List_Films_En_Jeux.pop(index))
                        else:
                            index += 1
            else:
                if self.List_Films_En_Jeux[index].id > nb_films*(1-(pourcentage_films_pas_vue)/100):
                    self.List_Films_Pas_Vue.append(self.List_Films_En_Jeux.pop(index))
                else:
                    index += 1
    
    def enleve_films_pas_vue_et_nul(self):
        index = 0
        while index < len(self.List_Films_En_Jeux):

            if not(self.isBot):
                while(True):
                    print("Le film suivant fait-il partie de ton top 100-200 meilleurs film ? (1=>Oui, 2=>Non, 3=>Pas Vue)")
                    self.List_Films_En_Jeux[index].affiche()
                    print()

                    val = input()
                    if (val!="" and int(val)>0 and int(val)<=2):
                        if int(val) == 1:
                            index += 1
                        if int(val) == 2:
                            self.List_Films_Elimines[0].append(self.List_Films_En_Jeux.pop(index))
                        if int(val) == 3:
                            self.List_Films_Pas_Vue.append(self.List_Films_En_Jeux.pop(index))
            else:
                if self.List_Films_En_Jeux[index].id > nb_films*(1-(pourcentage_films_pas_vue)/100):
                    self.List_Films_Pas_Vue.append(self.List_Films_En_Jeux.pop(index))
                elif self.List_Films_En_Jeux[index].id > nb_films*(1-(100-pourcentage_meilleurs_films)/100):
                    self.List_Films_Elimines[0].append(self.List_Films_En_Jeux.pop(index))
                else:
                    index += 1
    
    def start_tournois(self):

        self.List_Films_En_Jeux = self.genere_list_films()

        self.enleve_films_pas_vue_et_nul()

        arbre: Arbre = Arbre(self.List_Films_En_Jeux, 1, self.isBot)
        self.nb_match += arbre.nb_match
        arbre.joue_arbre()
        arbre.affichage()

        print("Nb match total :", self.nb_match)