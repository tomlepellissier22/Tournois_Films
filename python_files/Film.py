
class Film:
	def __init__(self, id: int, titre: str):
		self.id: int = id
		self.titre: str = titre
		self.image: str = "Image"
		self.nb_vic: int = 0
		self.nb_def: int = 0
		self.vue: bool = True
		self.list_vic: list[Film] = []
		self.list_def: list[Film] = []

	def affichage(self):
		if self.nb_def == 0 and self.nb_vic == 0:
			print("id:", self.id, " Titre:", self.titre)
		else:
			print("id:", self.id, " Titre:", self.titre, " Nb vic:", self.nb_vic, "Nb def:", self.nb_def)
	
	def reset_data(self):
		self.nb_vic: int = 0
		self.nb_def: int = 0
		self.vue: bool = True
		self.list_vic: list[Film] = []
		self.list_def: list[Film] = []

