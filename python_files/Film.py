
class Film:
	def __init__(self, id: int, titre: str):
		self.id: int = id
		self.titre: str = titre
		self.image: str = "Image"
		self.nb_vic: int = 0
		self.nb_def: int = 0

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

