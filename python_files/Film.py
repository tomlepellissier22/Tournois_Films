
class Film:
	def __init__(self, id: int, titre: str, titre_original: str, poster_path: str = "", nb_vic: int = 0, nb_def: int = 0):
		self.id: int = id
		self.titre: str = titre
		self.titre_original: str = titre_original
		self.nb_vic: int = nb_vic
		self.nb_def: int = nb_def
		self.poster_path: str = poster_path

	def toString(self):
		if self.nb_def == 0 and self.nb_vic == 0:
			return "id: %3d, Titre: %s" %(self.id, self.titre)
		else:
			return "id: %3d, Nb vic: %2d, Nb def: %2d, Titre: %s" %(self.id, self.nb_vic, self.nb_def, self.titre)

	def affichage(self):
		print(self.toString())
	
	def reset_data(self):
		self.nb_vic: int = 0
		self.nb_def: int = 0

