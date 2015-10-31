import webbrowser
import re
import requests
import xmltodict

movieList = []


class TrailerAddictMovie:
    """
    Converts a dictionary containing movie information into an object
    """
    def __init__(self, d):
        self.__dict__ = d['trailers']['trailer']


class Movie(object):
    """
    Represent various information about a Movie.
    """
    def __init__(
            self,
            movie_title,
            movie_storyline=None,
            movie_poster_url=None,
            movie_trailer_url=None,
            movie_imdb_id=None,
            movie_year=None,
            isFavorite=False):

        #: The Title
        self._title = movie_title

        #: The Storyline (Plot)
        self.storyline = movie_storyline

        #: The Url for the Poster
        self.poster_image_url = movie_poster_url

        #: The Url for the Trailer
        self.trailer_url = movie_trailer_url

        #: Internet Movie Database ID
        self.imdb_id = movie_imdb_id

        #: Relase Year
        self.year = movie_year

        #: Is the Movie favorited
        self.isFavorite = isFavorite

        #: Hyphenated Title used for TrailerAddict
        self.hyphenated_title = None

        #: TrailerAddict trailer id
        self.trailer_id = None


    @property
    def title(self):
        '''Retreive the Movie's title'''
        return self._title

    @title.setter
    def title(self, value):
        '''Set the title'''
        self._title = value

    def show_trailer(self):
        '''Open a Web Browser to the Trailer URL'''
        webbrowser.open(self.trailer_url)

    def set_trailer_info(self):
        '''Create the Url for the trailer at TrailerAddict'''
        # Convert spaces to hyphens and make lowercase
        self.hyphenated_title = self.title.replace(" ", "-").lower()

        # Not all Movies follow this pattern.
        # Need to add additional checks:
        # (i.e. Birdman matches /international-trailer and not /trailer)
        # Get the Web Page from Traileraddict.com for this Movie.
        page = requests.get("http://simpleapi.traileraddict.com/" +
                            self.hyphenated_title + "/trailer")

        # TrailerAddict.com provides a simpleapi.
        # The api returns valid requests in xml format
        # xmltodict converts the page contents into a dictionary
        result = xmltodict.parse(page.content)

        # Convert into a python object, making it easier to access.
        trailer_addict = TrailerAddictMovie(result)

        # Create/assign the TrailerAddict.com url
        self.trailer_id = trailer_addict.trailer_id
        self.trailer_url = "http://v.traileraddict.com/" + self.trailer_id


def isFavorite(title):
    '''Is the Movie, specified by it's tile, in the Favorites?'''
    for movie in movieList:
        if movie.title == title:
            movie.isFavorite = True
            return True

    return False


def getMovie(title):
    '''Retrieve a Movie, specified by title, if it is in the Favorites.'''
    for movie in movieList:
        if movie.title == title:
            return movie
    return None
