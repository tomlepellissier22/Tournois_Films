import random
from python_files.Arbre import Arbre
from python_files.Films import Films
from python_files.Constantes import *
from python_files.Score import *

def initialisation_films() -> Films:
  Listes_Films = [i+1 for i in range(nb_films)]
  return Films(Listes_Films)

def initialisation_arbres() -> Arbre:
  Listes_Films = [i+1 for i in range(nb_films)]
  random.shuffle(Listes_Films)
  return Arbre(Films(Listes_Films).films)

def jouer_x_match(x, films: Films):
  i = 0
  match_restant = films.nb_match_restant()
  while (i<x and match_restant>1):
    films.match_bot()
    match_restant = films.nb_match_restant()
    i += 1
  
  print("Nb match effectué =", i)
  
def jouer_tous_les_matchs_films(films: Films) -> int:
  nb_match = 0
  match_restant = films.nb_match_restant()
  while (match_restant>nb_meilleurs_films):
    films.match_bot()
    match_restant = films.nb_match_restant()
    nb_match += 1
  
  return nb_match

def jouer_tous_les_matchs_arbre(arbre: Arbre) -> int:
  nb_match = 0
  fini = arbre.fini()
  while not(fini):
    arbre.match_bot()
    fini = arbre.fini()
    nb_match += 1
  
  return nb_match

def meilleur_val(nb_tournois):
  liste=[]
  val=0
  nb_match_moy = 0
  for _ in range(nb_tournois):
    Listes_Films = initialisation_films()
    arbre = initialisation_arbres()
    nb_match = jouer_tous_les_matchs_films(Listes_Films)
    score=score_classement(Listes_Films.classement,1)
    liste.append(score)
    val+=score
    nb_match_moy += nb_match
    print("Il y a eu",nb_match," matchs pour un score de", round(score,2))
    Listes_Films.affichage_classement()
  

  return liste,round(val/nb_tournois,2),round(nb_match_moy/nb_tournois,2)

def main():

  #initialisation_films()
  #affichage_liste_films()
  #match_film_humain()
  #print()
  #affichage_liste_films()
  #match_film_bot()
  #jouer_x_match(1000)
  #jouer_tous_les_matchs()

  #print("Nb match restant = ", nb_match_restant())
  #classement = creation_classement()
  #affichage_classement(classement)
  #score_classement(classement,1)
  liste,val,nb_match = meilleur_val(1)
  #print(liste)
  print("Score moyen :",val)
  print("Nombre de match moyen :",nb_match)


main()

































