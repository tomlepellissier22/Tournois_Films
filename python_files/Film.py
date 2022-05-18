
class Film:
    def __init__(self, id, titre, nb_def, nb_matchs, vue):
      self.id: int = id
      self.titre: str = titre
      self.nb_def: int = nb_def
      self.nb_matchs: int = nb_matchs
      self.vue: bool = vue

    def affichage(self):
        print("id:", self.id, " Titre:",self.titre," ",self.nb_def,"défaites pour",self.nb_matchs,"matchs et vue =",self.vue)

    def score(self):
      if self.vue == False:
        return -1
      else:
        return self.nb_matchs - self.nb_def

