from python_files.Constantes import *
from python_files.Display_fonction import choix_question, display_one_films
from python_files.Film import Film
from python_files.Request import *
from python_files.Resultat import Resultat


def genere_base_de_donne(idListe: int):
    resultat = []
    liste = getAllMoviesFromList(idListe)

    for film in liste["items"]:
        if "poster_path" in film:
            resultat.append(
                Film(film["id"], film["title"], film["original_title"], film["poster_path"]))
        else:
            resultat.append(
                Film(film["id"], film["title"], film["original_title"]))

    return resultat


def ajout_most_popular_film_to_list(idList: int, idListElimine: int):
    page = 1
    val = 1

    liste_film_id = getAllIdFromList(idList)
    liste_film_elimine_id = getAllIdFromList(idListElimine)

    request_token = getRequestToken()
    acceptRequestToken(request_token["request_token"])
    input("Wait accept")
    session = createSession(request_token["request_token"])

    liste_id = []
    for film in liste_film_id:
        liste_id.append(film)
    for film in liste_film_elimine_id:
        liste_id.append(film)

    while (val == 1):
        liste_film_popular = getMostPopularFilms(page)

        for film in liste_film_popular["results"]:
            if not(film["id"] in liste_id):
                val_film = display_one_films(Film(
                    film["id"], film["title"], film["original_title"], film["poster_path"]), True)
                if val_film == Resultat.BIEN:
                    addMovieToList(film["id"], idList, session["session_id"])
                if val_film == Resultat.NUL:
                    addMovieToList(film["id"], idListElimine, session["session_id"])
        
        val = choix_question("Continuer ?")
        page += 1


def ajout_list_in_list(idList1: int, idList2: int, choix: bool):
    liste_film1_id = getAllIdFromList(idList1)
    liste_film2_id = getAllIdFromList(idList2)

    request_token = getRequestToken()
    acceptRequestToken(request_token["request_token"])
    input("Wait accept")
    session = createSession(request_token["request_token"])

    for filmId in liste_film1_id:
        if not(filmId in liste_film2_id):
            if choix == False:
                addMovieToList(filmId, idList2, session["session_id"])
            else:
                film = getFilmInfo(filmId)
                Film1 = Film(film["id"], film["title"], film["original_title"], film["poster_path"])
                val = display_one_films(Film1, True)
                if val == Resultat.BIEN:
                    addMovieToList(filmId, idList2, session["session_id"])
