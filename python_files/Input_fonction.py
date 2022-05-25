from python_files.Resultat import Resultat

def Input_fonction(list_texte: list[str], val_min: int, val_max: int):

    while (True):
        try:
            for texte in list_texte:
                print(texte)
            
            val = input()
            if (int(val)>=val_min and int(val)<=val_max):
                print()
                return int(val)
        except ValueError:
            print("The input was not a valid integer")
