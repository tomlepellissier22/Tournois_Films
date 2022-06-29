from python_files.Constantes import *
from python_files.Genere_Base_De_Donnee import ajout_list_in_list, ajout_most_popular_film_to_list
from python_files.Request import getAllIdFromList, getAllMoviesFromList, getFilmFromListWithPage
from python_files.Tournois_Films import Tournois_Film

#Tournois_Film().start_tournois()

#ajout_list_in_list(ID_LISTE_TOUS_LES_FILMS_GASPARD, ID_LISTE_TOUS_LES_FILMS, False)

#ajout_most_popular_film_to_list(ID_LISTE_TOUS_LES_FILMS_GASPARD, ID_LISTE_FILMS_ELIMINE_GASPARD)

#ajout_most_popular_film_to_list(ID_LISTE_TOUS_LES_FILMS, ID_LISTE_FILMS_ELIMINE_PERSO)

liste = getAllMoviesFromList(ID_LISTE_TOUS_LES_FILMS)
print(len(liste))
