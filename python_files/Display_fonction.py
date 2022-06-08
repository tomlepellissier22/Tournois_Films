from functools import partial
from tkinter import *
import PIL.ImageTk
from python_files.Constantes import TAILLE_GRANDE_IMAGE, TAILLE_PETIT_IMAGE
from python_files.Film import Film
from python_files.Request import getFilmImage
from python_files.Resultat import Resultat

"""{
    'adult': False,
    'backdrop_path': '/rr7E0NoGKxvbkb89eR1GwfoYjpA.jpg',
    'belongs_to_collection': None,
    'budget': 63000000,
    'genres': [{'id': 18, 'name': 'Drama'}],
    'homepage': 'http://www.foxmovies.com/movies/fight-club',
    'id': 550,
    'imdb_id': 'tt0137523',
    'original_language': 'en',
    'original_title': 'Fight Club',
    'overview': 'A ticking-time-bomb insomniac and a slippery soap salesman channel primal male aggression into a shocking new form of therapy. Their concept catches on, with underground "fight clubs" forming in every town, until an eccentric gets in the way and ignites an out-of-control spiral toward oblivion.',
    'popularity': 53.913,
    'poster_path': '/pB8BM7pdSp6B6Ih7QZ4DrQ3PmJK.jpg',
    'production_companies': [
        {'id': 508, 'logo_path': '/7PzJdsLGlR7oW4J0J5Xcd0pHGRg.png', 'name': 'Regency Enterprises', 'origin_country': 'US'},
        {'id': 711, 'logo_path': '/tEiIH5QesdheJmDAqQwvtN60727.png', 'name': 'Fox 2000 Pictures', 'origin_country': 'US'},
        {'id': 20555, 'logo_path': '/hD8yEGUBlHOcfHYbujp71vD8gZp.png', 'name': 'Taurus Film', 'origin_country': 'DE'},
        {'id': 54051, 'logo_path': None, 'name': 'Atman Entertainment', 'origin_country': ''},
        {'id': 54052, 'logo_path': None, 'name': 'Knickerbocker Films', 'origin_country': 'US'},
        {'id': 4700, 'logo_path': '/A32wmjrs9Psf4zw0uaixF0GXfxq.png', 'name': 'The Linson Company', 'origin_country': 'US'}],
    'production_countries': [{'iso_3166_1': 'DE', 'name': 'Germany'}, {'iso_3166_1': 'US', 'name': 'United States of America'}], 
    'release_date': '1999-10-15',
    'revenue': 100853753,
    'runtime': 139,
    'spoken_languages': [{'english_name': 'English', 'iso_639_1': 'en', 'name': 'English'}],
    'status': 'Released',
    'tagline': 'Mischief. Mayhem. Soap.',
    'title': 'Fight Club',
    'video': False,
    'vote_average': 8.4,
    'vote_count': 24190}"""


def choix_base_de_donnees():

    val = [-1]

    root = create_screen()

    FrameQuestion = Frame(root, borderwidth=2, relief=GROOVE)
    FrameQuestion.pack(padx=20, pady=20)

    Label(FrameQuestion, text="Selectionne la base de donnée souhaité").pack(
        padx=10, pady=10)

    FrameButton = Frame(root)
    FrameButton.pack(padx=20, pady=20)

    Button(FrameButton, text="Grande base de données (environ 1000 films)",
           width=50, command=partial(choose_value, root, val, 1)).pack()

    Button(FrameButton, text="Moyenne base de données (environ 500 films)",
           width=50, command=partial(choose_value, root, val, 2)).pack()

    Button(FrameButton, text="Petite base de données (environ 200 films)",
           width=50, command=partial(choose_value, root, val, 3)).pack()

    mainloop()

    return val[0]


def choix_question(question: str):

    val = [-1]

    root = create_screen()

    FrameQuestion = Frame(root, borderwidth=2, relief=GROOVE)
    FrameQuestion.pack(padx=20, pady=20)

    Label(FrameQuestion, text=question).pack(padx=10, pady=10)

    FrameButton = Frame(root)
    FrameButton.pack(padx=20, pady=20)

    Button(FrameButton, text="Oui", width=20,
           command=partial(choose_value, root, val, 1)).pack()

    Button(FrameButton, text="Non", width=20,
           command=partial(choose_value, root, val, 2)).pack()

    mainloop()

    return val[0]


def display_one_films(Film1: Film, elimination_film_bof: bool):

    val = [-1]

    root = create_screen()

    FrameQuestion = Frame(root, borderwidth=2, relief=GROOVE)
    FrameQuestion.pack(padx=20, pady=20)

    Button(FrameQuestion, text="SAUVEGARDE", command=partial(choose_value,
           root, val, Resultat.SAUVEGARDE)).pack(padx=10, pady=10, side=RIGHT)
    Label(FrameQuestion, text="Selectionne ton film préféré").pack(
        padx=10, pady=10, side=RIGHT)
    Button(FrameQuestion, text="Fin", command=partial(choose_value,
           root, val, Resultat.FIN)).pack(padx=10, pady=10, side=LEFT)

    FrameFilms = Frame(root)
    FrameFilms.pack(padx=20, pady=20)

    #film1Info = getFilmInfo(Film1.id)

    FrameFilm1 = Frame(FrameFilms, borderwidth=2, relief=GROOVE)
    FrameFilm1.pack(side=LEFT, padx=20)

    if Film1.poster_path != "":
        film1Image = getFilmImage(Film1.poster_path, TAILLE_GRANDE_IMAGE)

        imageFilm1 = PIL.ImageTk.PhotoImage(image=film1Image)

        Button(FrameFilm1, image=imageFilm1).pack()
    else:
        print("No poster_path")

    Label(FrameFilm1, text=Film1.titre).pack(padx=10, pady=10)
    if (Film1.titre != Film1.titre_original):
        Label(FrameFilm1, text=Film1.titre_original).pack(padx=10, pady=10)
    else:
        Label(FrameFilm1, text="").pack(padx=10, pady=10)

    FrameButton = Frame(root)
    FrameButton.pack(padx=20, pady=20)

    Button(FrameButton, text="Film Pas Vue => Elimination", width=50,
           command=partial(choose_value, root, val, Resultat.PAS_VUE)).pack()

    if (elimination_film_bof):
        Button(FrameButton, text="Film Vue mais pas fou => Elimination", width=50,
               command=partial(choose_value, root, val, Resultat.NUL)).pack()

    Button(FrameButton, text="Film Vue et bon => Ajout à la liste", width=50,
           command=partial(choose_value, root, val, Resultat.BIEN)).pack()

    mainloop()

    return val[0]


def display_two_films(Film1: Film, Film2: Film, bouton: bool):

    val = [0]

    root = create_screen()

    FrameQuestion = Frame(root, borderwidth=2, relief=GROOVE)
    FrameQuestion.pack(padx=20, pady=20)

    Button(FrameQuestion, text="SAUVEGARDE", command=partial(
        choose_value, root, val, Resultat.SAUVEGARDE)).pack(side=RIGHT)
    Label(FrameQuestion, text="Selectionne ton film préféré").pack(
        padx=10, pady=10, side=RIGHT)
    Button(FrameQuestion, text="Fin", command=partial(
        choose_value, root, val, Resultat.FIN)).pack(side=LEFT)

    FrameFilms = Frame(root)
    FrameFilms.pack(padx=20, pady=20)

    #film1Info = getFilmInfo(Film1.id)
    #film2Info = getFilmInfo(Film2.id)

    FrameFilm1 = Frame(FrameFilms, borderwidth=2, relief=GROOVE)
    FrameFilm1.pack(side=LEFT, padx=20)

    FrameFilm2 = Frame(FrameFilms, borderwidth=2, relief=GROOVE)
    FrameFilm2.pack(side=RIGHT, padx=20)

    if Film1.poster_path != "":
        film1Image = getFilmImage(Film1.poster_path, TAILLE_GRANDE_IMAGE)

        imageFilm1 = PIL.ImageTk.PhotoImage(image=film1Image)

        Button(FrameFilm1, image=imageFilm1, command=partial(
            choose_value, root, val, Resultat.VICTOIRE)).pack()
    else:
        print("No poster_path1")

    if Film2.poster_path != "":
        film2Image = getFilmImage(Film2.poster_path, TAILLE_GRANDE_IMAGE)

        imageFilm2 = PIL.ImageTk.PhotoImage(image=film2Image)

        Button(FrameFilm2, image=imageFilm2, command=partial(
            choose_value, root, val, Resultat.DEFAITE)).pack()
    else:
        print("No poster_path2")

    Label(FrameFilm1, text=Film1.titre).pack(padx=10, pady=10)
    if (Film1.titre != Film1.titre_original):
        Label(FrameFilm1, text=Film1.titre_original).pack(padx=10, pady=10)
    else:
        Label(FrameFilm1, text="").pack(padx=10, pady=10)

    Label(FrameFilm2, text=Film2.titre).pack(padx=10, pady=10)
    if (Film2.titre != Film2.titre_original):
        Label(FrameFilm2, text=Film2.titre_original).pack(padx=10, pady=10)
    else:
        Label(FrameFilm2, text="").pack(padx=10, pady=10)

    if (bouton):
        FrameButton = Frame(root)
        FrameButton.pack(padx=20, pady=20)

        Button(FrameButton, text="Egalité, pas de match joué", width=50,
               command=partial(choose_value, root, val, Resultat.EGALITE)).pack()

        Button(FrameButton, text="Egalité, les deux films ont gagné", width=50,
               command=partial(choose_value, root, val, Resultat.EGALITE_VICTOIRE)).pack()

        Button(FrameButton, text="Egalité, les deux films ont perdu", width=50,
               command=partial(choose_value, root, val, Resultat.EGALITE_DEFAITE)).pack()

    mainloop()

    return val[0]


def choose_value(root: Tk, val: list[int], value: int):
    val[0] = value
    root.destroy()


def create_screen():
    root = Tk()
    root.title("Tournois Films")

    return root


def display_tier_list(liste_films: list[Film]):
    root = create_screen()

    Frame_main = Frame(root, bg="Yellow")
    Frame_main.grid(row=0, sticky="news")

    # Add a canvas in that frame
    canvas = Canvas(Frame_main, bg="yellow")
    canvas.grid(row=0, column=0, sticky="news")

    # Link a scrollbar to the canvas
    vsb = Scrollbar(Frame_main, orient="horizontal", command=canvas.xview)
    vsb.grid(row=1, column=0, sticky='ew')
    canvas.configure(yscrollcommand=vsb.set)

    frame_buttons = Frame(canvas, bg="blue")
    canvas.create_window((0, 0), window=frame_buttons, anchor='nw')

    for ligne in range(len(liste_films)):
        liste_images = []
        liste_label: list[Label] = []
        for colonne in range(len(liste_films[ligne])):
            liste_images.append(getFilmImageForTk(liste_films[ligne][colonne]))
            liste_label.append(Button(canvas, image=liste_images[colonne]))
            liste_label[colonne].grid(row=ligne, column=colonne)

    Frame_main.config(width=1000, height=500)

    root.mainloop()


def getFilmImageForTk(film: Film):
    if film.poster_path != "":
        film1Image = getFilmImage(film.poster_path, TAILLE_PETIT_IMAGE)

        return PIL.ImageTk.PhotoImage(image=film1Image)
    else:
        print("No poster_path1")
