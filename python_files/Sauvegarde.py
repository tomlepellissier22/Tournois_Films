import pickle

from python_files.Film import Film


def sauvegarde(Liste_Info_General):
    fichier = open("Sauvegarde/Liste_Info_General", 'wb')
    pickle.dump(Liste_Info_General, fichier)
    fichier.close()


def charge_sauvegarde():
    fichier = open("Sauvegarde/Liste_Info_General", 'rb')
    Liste_Info_General = pickle.load(fichier)
    fichier.close()

    return Liste_Info_General


def sauvegarde_tier_liste(Tier_liste: list[list[Film]]):
    fichier = open("Sauvegarde/Tier_liste", 'wb')
    pickle.dump(Tier_liste, fichier)
    fichier.close()


def charge_tier_liste():
    fichier = open("Sauvegarde/Tier_liste", 'rb')
    Tier_List = pickle.load(fichier)
    fichier.close()

    return Tier_List


def sauvegarde_tier_liste_humain(Tier_liste: list[list[Film]]):
    fichier = open("Sauvegarde/Tier_liste_Humain", 'w')
    print("Tier Liste")
    taille = len(Tier_liste)
    for i in range(taille):
        print("TIER n°", taille-i, " -----------------")
        for film in Tier_liste[i]:
            fichier.write("id: "+str(film.id)+" Titre: "+str(film.titre) +
                          " Titre original: "+str(film.titre_original)+"\n")
    fichier.close()


def sauvegarde_elimination(list_info_elimination):
    fichier = open("Sauvegarde/List_info_elimination", 'wb')
    pickle.dump(list_info_elimination, fichier)
    fichier.close()


def charge_sauvegarde_elimination():
    fichier = open("Sauvegarde/List_info_elimination", 'rb')
    list_info_elimination = pickle.load(fichier)
    fichier.close()

    return list_info_elimination.copy()
