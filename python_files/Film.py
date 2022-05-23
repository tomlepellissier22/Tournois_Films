
class Film:
	def __init__(self, id: int, titre: str):
		self.id: int = id
		self.titre: str = titre
		self.image: str = "Image"
		self.nb_vic: int = 0
		self.nb_def: int = 0

	def affichage(self):
		if self.nb_def == 0 and self.nb_vic == 0:
			print("id: %2d, Titre: %s" %(self.id, self.titre))
		else:
			print("id: %2d, Nb vic: %2d, Nb def: %2d, Titre: %s" %(self.id, self.nb_vic, self.nb_def, self.titre))
	
	def reset_data(self):
		self.nb_vic: int = 0
		self.nb_def: int = 0

