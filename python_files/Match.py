from python_files.Film import Film
from python_files.Resultat import Resultat
from python_files.Constantes import *
import random

def match_film_humain(film1: Film,film2: Film):
  print()
  film1.affichage()
  film2.affichage()

  val = 0
  while(True):
    print("Que choisi tu ? (1=>V, 2=>D, 3=>E, 4=>GV, 5=>GD, 6=>PV1, 7=>PV2)")
    val = input()
    if (val!="" and int(val)>0 and int(val)<=7):
      break

  return Resultat(int(val))

def match_film_bot(film1: Film, film2: Film, nb_match_restant=0):

  id1 = film1.id
  id2 = film2.id
      
  if abs(id1-id2) < ecart_egalite * nb_match_restant:
    val = 3
  elif abs(id1-id2) > ecart_grande * nb_films:
    if id1 > id2:
      val = 5
    else:
      val = 4
  else:
    if id1>id2:
      val = 2
    else:
      val = 1
      
  if film1.nb_matchs == 0 and film2.nb_matchs == 0:
    number = random.randint(1,100)
    if number<pourcentage_film_pas_vue/2:
      val = 6
    if number>100-pourcentage_film_pas_vue/2:
      val = 7
      
  return Resultat(val)
