from python_files.Constantes import *

def score_classement(classement,etat):
  nb_err = 0
  nb_films_pris_en_compte = 0
  taille_classement = len(classement)
  nb_list = (taille_classement-2)*pourcentage_tier_list_prise_en_compte//100
  ii=0
  for i in range(nb_list):
    nb_films_pris_en_compte += len(classement[taille_classement-i-1])
    max_val = calcul_val_for_err(classement[taille_classement-i-1],etat)
    for y in classement[taille_classement-i-2]:
      if y.id<max_val:
        nb_err += 1
    ii=i
  
  nb_films_pris_en_compte += len(classement[taille_classement-ii-1])
  return (nb_err/nb_films_pris_en_compte)*100
  
def calcul_val_for_err(tier_list,etat):
    max_val = 1
    moy_val = 0
    med_val = 1
    for y in tier_list:
      moy_val += y.id
      if y.id>max_val:
        max_val=y.id
    
    taille = len(tier_list)
    if taille!=0: 
      if taille%2==0:
        med_val = (tier_list[taille//2].id + tier_list[taille//2-1].id)/2
      else:
        med_val = tier_list[taille//2].id
    else:
      taille=1
    
    if etat==1:
      return moy_val/taille
    elif etat==2:
      return med_val
    else:
      return max_val

































