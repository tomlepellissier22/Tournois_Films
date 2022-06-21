from io import BytesIO
import requests
import PIL.Image

from python_files.Constantes import API_KEY

def getFilmInfo(idFilm: int):
    url = "https://api.themoviedb.org/3/movie/" + str(idFilm) + "?api_key=" + API_KEY + "&language=fr-FR"
    
    return requests.get(url).json()

def getFilmImage(imageUrl: str, taille: int):
    #imageUrl = "/pB8BM7pdSp6B6Ih7QZ4DrQ3PmJK.jpg"

    url = "https://image.tmdb.org/t/p/w" + str(taille) + imageUrl
    
    result = requests.get(url)

    return PIL.Image.open(BytesIO(result.content))

def getMostPopularFilms(pageId: int):
    url = "https://api.themoviedb.org/3/discover/movie?api_key="+ API_KEY +"&sort_by=vote_count.desc&include_adult=true&include_video=false&page="+str(pageId)+"&with_watch_monetization_types=flatrate&language=fr-FR"
    return requests.get(url).json()

def getMoviesFromList(listId: int):
    url = "https://api.themoviedb.org/3/list/"+str(listId)+"?api_key="+ API_KEY + "&language=fr-FR"
    return requests.get(url).json()

def getRequestToken():
    url = "https://api.themoviedb.org/3/authentication/token/new?api_key="+ API_KEY
    return requests.get(url).json()

def acceptRequestToken(request_token: str):
    url = "https://www.themoviedb.org/authenticate/" + request_token
    print(url)

def createSession(request_token: str):
    url = "https://api.themoviedb.org/3/authentication/session/new?api_key="+ API_KEY
    data = {"request_token": request_token}
    return requests.post(url, json=data).json()
    
def addMovieToList(movieId: int, listId: int, sessionId: str):
    url = "https://api.themoviedb.org/3/list/"+str(listId)+"/add_item?api_key="+API_KEY+"&session_id="+sessionId
    data = {"media_id": movieId}
    return requests.post(url, json=data).json()