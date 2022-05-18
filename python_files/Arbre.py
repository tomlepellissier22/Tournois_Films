from python_files.Match import *
from python_files.Resultat import *

class Arbre:
  def __init__(self, list_films: list[Film]):
    self.arbre = []
    self.arbre.append(list_films)
    if len(self.arbre[0])%2!=0:
      qualifie = self.arbre[0].pop()
      self.arbre.append([qualifie])
    else:
      self.arbre.append([])
    self.indice_film = 0
    self.indice_round = 0
    self.film1 = self.arbre[self.indice_round][self.indice_film]
    self.film2 = self.arbre[self.indice_round][self.indice_film+1]

  def next_match(self):
    if self.fini() == False:
      if self.indice_film+1 < len(self.arbre[self.indice_round]):
        self.film1 = self.arbre[self.indice_round][self.indice_film]
        self.film2 = self.arbre[self.indice_round][self.indice_film+1]
      else:
        self.indice_film = 0
        self.indice_round += 1
        if len(self.arbre[self.indice_round])%2!=0:
          qualifie = self.arbre[self.indice_round].pop()
          self.arbre.append([qualifie])
        else:
          self.arbre.append([])
        self.film1 = self.arbre[self.indice_round][self.indice_film]
        self.film2 = self.arbre[self.indice_round][self.indice_film+1]
  
  def match_bot(self):
    if not(self.fini()):
      
      val = match_film_bot(self.film1, self.film2)
      self.resolution_match(Resultat(val))
      self.next_match()

  def fini(self) -> bool:
    return len(self.arbre[self.indice_round]) == 1

  def resolution_match(self, resultat):
    indice_film = -1
    if resultat == Resultat.VICTOIRE or resultat == Resultat.GRANDE_DEFAITE or resultat == Resultat.PAS_VUE1:
      indice_film = self.indice_film
    elif resultat == Resultat.DEFAITE or resultat == Resultat.GRANDE_DEFAITE or resultat == Resultat.PAS_VUE2:
      indice_film = self.indice_film+1
    else:
      print("Mauvais choix")

    if indice_film!=-1:
      qualifie = self.arbre[self.indice_round].pop(indice_film)
      self.arbre[self.indice_round+1].append(qualifie)
      self.indice_film += 2
      self.next_match()

  def classement(self):
    return self.arbre

  def affichage(self):
    for i in range(len(self.arbre)):
      print("TIER n°",i+1," -----------------")
      for y in self.arbre[i]:
        y.affichage()