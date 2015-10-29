import webbrowser
import re
import requests
import xmltodict

# Provide a quick way to convert the dictionary containing the movie information to a python object
class TrailerAddictMovie():
    def __init__(self, d):
        self.__dict__ = d['trailers']['trailer']
        
class Movie():
    def __init__(self, movie_title, movie_storyline=None, movie_poster_url=None, movie_trailer_url=None, movie_imdb_id=None, movie_year=None, isFavorite=False):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_url
        self.trailer_url = movie_trailer_url
        self.imdb_id = movie_imdb_id
        self.year = movie_year
        self.isFavorite = isFavorite
        
        self.hyphenated_title = None
        self.trailer_id = None
        
        # Extract the youtube ID from the url (copied from fresh_tomatoes.py)
        if self.trailer_url != None:
            youtube_id_match = re.search(r'(?<=v=)[^&#]+', self.trailer_url)
            youtube_id_match = youtube_id_match or re.search(
                r'(?<=be/)[^&#]+', self.trailer_url)
            
            # Add the youtube ID as a member variable
            self.trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match else None)
    
    def show_trailer(self):
        webbrowser.open(self.trailer_url)
    
    def set_trailer_info(self):
        # Create a hyphenated and lowercase version of the movie title.  Spaces are converted to -
        self.hyphenated_title = self.title.replace(" ", "-").lower()
        
        # Not all Movies follow this pattern, need to add additional checks (i.e. The trailer for Birdman matches /international-trailer and not /trailer)
        # Attempt to get the Web Page from Traileraddict.com that matches the movie we're searching for.
        page = requests.get("http://simpleapi.traileraddict.com/" + self.hyphenated_title + "/trailer")
        
        # TrailerAddict.com provides a simpleapi which returns valid requests in an xml format
        # xmltodict takes the page contents and converts them into a python dictionary
        result = xmltodict.parse(page.content)
        
        # Convert the dictionary into a python object, making it easier to access.
        trailer_addict = TrailerAddictMovie(result)
        
        # Create/assign the TrailerAddict.com url
        self.trailer_id = trailer_addict.trailer_id
        self.trailer_url = "http://v.traileraddict.com/" + self.trailer_id
        