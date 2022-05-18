from python_files.Film import *
from python_files.Match import *
from python_files.Resultat import *
from python_files.Constantes import *
import random

class Films:
  def __init__(self, list_films: list[int]):
    self.films = []
    self.classement = [[],[]]
    for i in range(len(list_films)):
      self.films.append(Film(i+1,list_films[i],0,0,True))

  def affichage(self):
    for x in self.films:
        x.affichage()

  def nb_match_restant(self) -> int:
    return len(self.films)

  def prochain_match(self) -> tuple[Film, Film]:
    if self.films !=[]:
      if self.nb_match_restant()<nb_films_par_match:
        print("Il n/'y a plus de match")
      else:
        min_match=self.films[0].nb_matchs
        for x in self.films:
          if x.nb_def<nb_def_max and x.nb_matchs<min_match and x.vue == True:
            min_match=x.nb_matchs

        films=[]
        while len(films)<2:
          for x in self.films:
            if x.nb_def<nb_def_max and x.nb_matchs==min_match and x.vue == True:
              films.append(x)
          min_match+=1

        film1, film2 = random.sample(films, nb_films_par_match)
        return film1, film2
    else:
        print("La liste de films est vide")
    
  def transformation_film(self, film: Film, nb_def: int, nb_matchs: int, pasVue: bool):
    suppression = False
    for i in range(len(self.films)):
      if self.films[i]==film:
        self.films[i].nb_def += nb_def
        self.films[i].nb_matchs += nb_matchs
        self.films[i].vue = not(pasVue)
        if self.films[i].nb_def >= nb_def_max or self.films[i].vue == False:
          suppression = True
          index = i
          film = self.films[i]
          break
    
    if suppression:
      self.ajout_classement(film, index)

  def transformation_film1_film2(self,film1: Film,nb_def1: int,nb_matchs1: int,pasVue1: bool,film2: Film,nb_def2: int,nb_matchs2: int,pasVue2: bool):
    suppression = 0
    index = -1
    for i in range(len(self.films)):
      if self.films[i]==film1:
        self.films[i].nb_def += nb_def1
        self.films[i].nb_matchs += nb_matchs1
        self.films[i].vue = not(pasVue1)
        if self.films[i].nb_def >= nb_def_max or self.films[i].vue == False:
          suppression = 1
          index = i
          film1 = self.films[i]
      if self.films[i]==film2:
        self.films[i].nb_def += nb_def2
        self.films[i].nb_matchs += nb_matchs2
        self.films[i].vue = not(pasVue2)
        if self.films[i].nb_def >= nb_def_max or self.films[i].vue == False:
          suppression = 2
          index = i
          film2 = self.films[i]
    
    if suppression == 1:
      self.ajout_classement(film1, index)
    elif suppression == 2:
      self.ajout_classement(film2, index)

  def transformation_match(self, film1: Film, film2: Film, resultat: Resultat):
    if (resultat == Resultat.VICTOIRE):
      self.transformation_film1_film2(film1,0,1,False,film2,1,1,False)
    if (resultat == Resultat.DEFAITE):
      self.transformation_film1_film2(film1,1,1,False,film2,0,1,False)
    if (resultat == Resultat.EGALITE):
      self.transformation_film1_film2(film1,0,1,False,film2,0,1,False)
    if (resultat == Resultat.GRANDE_VICTOIRE):
      self.transformation_film1_film2(film1,0,val_grand_ecart,False,film2,val_grand_ecart,val_grand_ecart,False)
    if (resultat == Resultat.GRANDE_DEFAITE):
      self.transformation_film1_film2(film1,val_grand_ecart,val_grand_ecart,False,film2,0,val_grand_ecart,False)
    if (resultat == Resultat.PAS_VUE1):
      self.transformation_film(film1,0,0,True)
    if (resultat == Resultat.PAS_VUE2):
      self.transformation_film(film2,0,0,True)

  def match_humain(self):
    if self.nb_match_restant()>2:
      film1, film2 = self.prochain_match()
      
      val = match_film_humain(film1, film2)

      self.transformation_match(film1, film2, val)
    else:
      print("Plus de match")

  def match_bot(self):
    if self.nb_match_restant()>2:
      film1, film2 = self.prochain_match()
      
      val = match_film_bot(film1, film2, self.nb_match_restant())
      
      self.transformation_match(film1,film2,Resultat(val))

  def ajout_classement(self, film: Film, index: int):
    self.films.pop(index)

    score = film.score()
    if score == -1:
      self.classement[0].append(film)
    else:
      if len(self.classement) <= score+1:
        while len(self.classement) <= score+1:
          self.classement.append([])
      self.classement[score+1].append(film)
    
  def affichage_classement(self):
    for x in self.classement:
      if x!=[]:
        if x[0].vue == False:
          print("TIER n°",x[0].score(),", Films Pas Vue -----------------")
        else:
          print("TIER n°",x[0].score()+1," -----------------")
        for y in x:
          y.affichage()
    
    print("TIER n°",self.films[0].score()+1," Meilleurs Films -----------------")
    for y in self.films:
      y.affichage()
