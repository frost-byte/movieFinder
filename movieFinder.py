from flask import Flask, render_template, request, json
import media
import omdb
from entertainment_center import movieList, isFavorite, getMovie

app = Flask(__name__)

# The root route or index page
@app.route('/')
def index():
    return render_template("fresh_tomatoes.html",movieList=movieList)

# Handle a search Request; This takes in a movie title via a client request and returns the panel containing a list of matching films.
@app.route('/search', methods=['POST'])
def process_search():
    json = request.get_json()
    title = json['title']
    searchResults = omdb.search_movie(title)

    return render_template("search_results.html",searchList=searchResults)

# Provides a view for a movie selected from the Search Panel    
@app.route('/view', methods=['POST'])
def process_view():

    # Retrieve the Request data from the client
    json = request.get_json()
    imdb_id = json['imdb_id']
    
    # Search the Online Movie Database using an IMDB id
    imdbInfo = omdb.imdbid(imdb_id)
    
    #  See if it's already in Favorites
    if isFavorite(imdbInfo.title):
        viewedMovie = getMovie(imdbInfo.title)
    # Movie isn't favored already, so create a new instance
    else:
        viewedMovie = media.Movie(imdbInfo.title,
                                  imdbInfo.plot,
                                  imdbInfo.poster,
                                  None,
                                  imdb_id,
                                  imdbInfo.year)
        # Pull the Trailer Url from TrailerAddict.com
        viewedMovie.set_trailer_info()
    
    # Render the Movie into a view on the Client
    return render_template("movie_view.html",movieInfo=viewedMovie)

# Adds the current Movie being viewed, from a search, to the the list of favorites and updates the primary view.
@app.route('/add', methods=['POST'])    
def add_to_favorites():

    # Retrieve the Movie's information from the Client's request.
    movie = request.get_json()
    
    title = movie['title']
    trailer = movie['trailer_url']
    poster = movie['poster_url']
    
    # Create and Add the New Movie to the Favorites List
    newMovie = media.Movie(title,None,poster,trailer,isFavorite=True)
    movieList.append(newMovie)

    # Update the Primary view which contains the tiles of Favorite movies.
    return render_template("movie_list.html",movieList=movieList)